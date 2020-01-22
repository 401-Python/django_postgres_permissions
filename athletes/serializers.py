from rest_framework import serializers

from .models import BasketballPlayer, FootballPlayer

class BasketballPlayerSerializer(serializers.ModelSerializer):
  class Meta:
    model = BasketballPlayer
    fields = [
      'id', 'author', 'player_name', 'height', 'weight', 'position'
    ]

class FootballPlayerSerializer(serializers.ModelSerializer):
  class Meta:
    model = FootballPlayer
    fields = [
      'id', 'author', 'player_name', 'height', 'weight', 'fourty_yard_dash', 'wonderlic_score'
    ]