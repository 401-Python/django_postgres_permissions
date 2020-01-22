from django.urls import path
from .views import *

urlpatterns = [
  path('bball-players/', BasketballPlayerList.as_view(), name='bball_list'),
  path('bball-players/<int:pk>/', BasketballPlayerDetail.as_view(), name='bball_detail'),
  path('football-players/', FootballPlayerList.as_view(), name='football_list'),
  path('football-players/<int:pk>', FootballPlayerDetail.as_view(), name='football_detail'),
]