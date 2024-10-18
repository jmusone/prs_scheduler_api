from rest_framework import status
#from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.reverse import reverse

from datetime import datetime, timedelta
from django.utils import timezone

from .models import Leagues, GameDateTimes
from .serializers import LeaguesSerializer, GameDateTimesSerializer
from . import scraper

# Create your views here.
class Health(APIView):
    def get(self, request, format=None):
        return Response({
            'Leagues': reverse('leagues-view', request=request, format=format),
            'Games': reverse('schedule-view', request=request, format=format)
        })

class LeaguesGenericView(APIView):
    def get(self, request, format=None):
        leagues = Leagues.objects.all()
        serializer = LeaguesSerializer(leagues, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = LeaguesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            league_id = serializer.instance.id
            url = serializer.instance.scheduleLink
            gameDateTimes = scraper.getAllGameTimesAndDates(url)
            for game in gameDateTimes:
                gameSerializer = GameDateTimesSerializer(data={"leagueId": league_id, "gameDateTime": game})
                if gameSerializer.is_valid():
                    gameSerializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def get_object(self, league_id):
        try:
            return Leagues.objects.get(id = league_id)
        except Leagues.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class LeaguesByIdView(APIView):
    def get_object(self, league_id):
        try:
            return Leagues.objects.get(id = league_id)
        except Leagues.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
    def get(self, request, league_id, format=None):
        league = self.get_object(league_id)
        serializer = LeaguesSerializer(league)
        return Response(serializer.data)
    
    def put(self, request, league_id, format=None):
        league = self.get_object(league_id)
        serializer = LeaguesSerializer(league, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, league_id, format=None):
        league = self.get_object(league_id)
        league.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class GameDateTimesGenericView(APIView):
    def get(self, request, format=None):
        games = GameDateTimes.objects.all()
        serializer = GameDateTimesSerializer(games, many=True)
        return Response(serializer.data)
    
class GameDateTimeByIdView(APIView):
    def get_object(self, league_id):
        try:
            return GameDateTimes.objects.filter(leagueId = league_id)
        except GameDateTimes.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def get(self, request, league_id, format=None):
        games = self.get_object(league_id)
        serializer = GameDateTimesSerializer(games, many=True)
        return Response(serializer.data)

class NextGameDateTime(APIView):
    def get_next(self, games):
        currDate = timezone.now()
        postCurrentDates = filter(lambda g: g.gameDateTime > currDate, games)
        closestGame = min(postCurrentDates, key = lambda g: g.gameDateTime)
        return closestGame

    def get(self, request):
        games = GameDateTimes.objects.all()
        nextGame = self.get_next(games)
        serializer = GameDateTimesSerializer(nextGame)
        return Response(serializer.data)
    
class NextGameDateTimeById(APIView):  
    def get_object(self, league_id):
        try:
            return GameDateTimes.objects.filter(leagueId = league_id)
        except GameDateTimes.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get_next(self, games):
        currDate = timezone.now()
        postCurrentDates = filter(lambda g: g.gameDateTime > currDate, games)
        closestGame = min(postCurrentDates, key = lambda g: g.gameDateTime)
        return closestGame
        
    def get(self, request, league_id, format=None):
        games = self.get_object(league_id)
        nextGame = self.get_next(games)
        serializer = GameDateTimesSerializer(nextGame)
        return Response(serializer.data)
    
class GameDateTimeIn(APIView):
    def get(self, request, days, format=None):
        startDate = datetime.today()
        endDate = startDate + timedelta(days=days)
        games = GameDateTimes.objects.all().filter(gameDateTime__range = (startDate, endDate))
        serializer = GameDateTimesSerializer(games, many=True)
        return Response(serializer.data)