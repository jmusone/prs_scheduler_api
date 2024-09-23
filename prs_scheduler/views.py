from rest_framework import status
#from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Leagues, GameDateTimes
from .serializers import LeaguesSerializer, GameDateTimesSerializer
from . import scraper

# Create your views here.
class Health(APIView):
    def get(self, request, format=None):
        return Response(status=status.HTTP_204_NO_CONTENT)
  
class LeaguesGenericView(APIView):
    def get(self, request, format=None):
        leagues = Leagues.objects.all()
        serializer = LeaguesSerializer(leagues, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = LeaguesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
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
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class GameDateTimeByIdView(APIView):
    def get_object(self, league_id):
            try:
                return Leagues.objects.get(id = league_id)
            except Leagues.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
    
    def get(self, request, league_id, format=None):
        return Response(status=status.HTTP_204_NO_CONTENT)