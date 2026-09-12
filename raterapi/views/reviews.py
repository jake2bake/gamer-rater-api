from django.http import HttpResponseServerError
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from raterapi.models import Review, Game
from django.utils import timezone

class ReviewView(ViewSet):
    def list(self, request):
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def create(self, request):
        try:
            game = Game.objects.get(pk=request.data['gameId'])
        except Game.DoesNotExist:
            return Response({"message": "Game not found"}, status=status.HTTP_404_NOT_FOUND)
        review = Review(
            gameId = game,
            userId = request.auth.user,
            rating = request.data['rating'],
            comment = request.data['comment'],
            date=timezone.now(),
            imgUrl=request.data.get("imgUrl", "")
        )    

        review.save()
        
        serialized = ReviewSerializer(review)
        return Response(serialized.data, status=status.HTTP_201_CREATED)
        

class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ( 'id', 'gameId', 'userId', 'rating', 'comment',  )