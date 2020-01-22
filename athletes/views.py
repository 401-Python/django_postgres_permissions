from .models import BasketballPlayer, FootballPlayer
from rest_framework import generics
from .serializers import BasketballPlayerSerializer, FootballPlayerSerializer
from .permissions import IsAuthorOrReadOnly
# Create your views here.

class BasketballPlayerList(generics.ListCreateAPIView):
  queryset = BasketballPlayer.objects.all()
  serializer_class = BasketballPlayerSerializer

class BasketballPlayerDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = BasketballPlayer.objects.all()
  serializer_class = BasketballPlayerSerializer
  permission_classes = (IsAuthorOrReadOnly,)


class FootballPlayerList(generics.ListCreateAPIView):
  queryset = FootballPlayer.objects.all()
  serializer_class = FootballPlayerSerializer

class FootballPlayerDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = FootballPlayer.objects.all()
  serializer_class = FootballPlayerSerializer
  permission_classes = (IsAuthorOrReadOnly,)
