from rest_framework import serializers
from .models import Leagues, GameDateTimes
from django.contrib.auth.models import User

class LeaguesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leagues
        fields = ['id', 'league', 'location', 'sport', 'teamName', 'scheduleLink']

class GameDateTimesSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameDateTimes
        fields = ['id', 'leagueId', 'gameDateTime']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =  ['username', 'password']