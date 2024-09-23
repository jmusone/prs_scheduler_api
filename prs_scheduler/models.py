from django.db import models

# Create your models here.
class Leagues(models.Model):
    league = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    sport = models.CharField(max_length=100)
    teamName = models.CharField(max_length=100)
    scheduleLink = models.TextField()

class GameDateTimes(models.Model):
    leagueId = models.ForeignKey(Leagues, related_name="Leagues_id", on_delete=models.CASCADE)
    gameDateTime = models.DateTimeField()