from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework import serializers
from raterapi.models import Game


class GameSerializer(serializers.ModelSerializer):
    # categories = CategorySerializer(many=True)

    class Meta:
        model = Game
        fields = ['id', 'title', 'description', 'designer', 'year_released', 'players', 'completion_time', 'min_age']


class GameViewSet(viewsets.ViewSet):

    def list(self, request):
        games = Game.objects.all()
        serializer = GameSerializer(games, many=True, context={'request': request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            game = Game.objects.get(pk=pk)
            serializer = GameSerializer(game, context={'request': request})
            return Response(serializer.data)

        except Game.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        # Get the data from the client's JSON payload
        title = request.data.get('title')
        description = request.data.get('description')
        designer = request.data.get('designer')
        year_released = request.data.get('year_released')
        players = request.data.get('players')
        completion_time = request.data.get('completion_time')
        min_age = request.data.get('min_age')

        game = Game.objects.create(
            title= title,
            description = description,
            designer = designer,
            year_released = year_released,
            players = players,
            completion_time = completion_time,
            min_age = min_age)
            

        # Establish the many-to-many relationships
        # category_ids = request.data.get('categories', [])
        # game.categories.set(category_ids)

        serializer = GameSerializer(game, context={'request': request})
        return Response(serializer.data, status=status.HTTP_201_CREATED)




#     Table Games {
#   id int pk
#   title varchar
#   description varchar
#   designer varchar
#   year_released number
#   players int
#   completion_time number
#   age number 
# }
        # Create a book database row first, so you have a