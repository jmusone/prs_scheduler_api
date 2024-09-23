from rest_framework import serializers
from .models import Leagues, GameDateTimes

class LeaguesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leagues
        fields = ['id', 'league', 'location', 'sport', 'teamName', 'scheduleLink']

class GameDateTimesSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameDateTimes
        fields = ['id', 'leagueId', 'gameDateTime']