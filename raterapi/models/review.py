from django.db import models
from django.contrib.auth.models import User

class Review(models.Model):
    gameId = models.ForeignKey("Game", on_delete=models.CASCADE, related_name='reviews')
    userId = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField()
    comment = models.TextField()
    date = models.DateTimeField()
    imgUrl = models.URLField(max_length=200, blank=True)