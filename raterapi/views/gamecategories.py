from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from raterapi.models import GameCategory, Game, Category

# ✅ Serializer correctly mapping gameId/categoryId from JSON to ForeignKey fields
class GameCategorySerializer(serializers.ModelSerializer):
    game = serializers.PrimaryKeyRelatedField(queryset=Game.objects.all())
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())

    class Meta:
        model = GameCategory
        fields = ['id', 'game', 'category']


# ✅ View using the serializer above
class GameCategoryView(ViewSet):
    def list(self, request):
        gameCategories = GameCategory.objects.all()
        serializer = GameCategorySerializer(gameCategories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = GameCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
