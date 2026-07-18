from django.db import models
from django.contrib.auth.models import User
class Game(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    designer = models.CharField(max_length=100)
    playerCount = models.IntegerField()
    totalTime = models.IntegerField(help_text="Total game time in minutes")
    ageRequired = models.IntegerField()
    avgRating = models.IntegerField()
    userId = models.ForeignKey(User, on_delete=models.CASCADE, related_name='games_created')

