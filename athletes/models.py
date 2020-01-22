from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


bball_positions = (
  ('1', 'PG'),
  ('2', 'SG'),
  ('3', 'SF'),
  ('4', 'PF'),
  ('5', 'C'),
  ('6', 'water boy')
)
class BasketballPlayer(models.Model):
  
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  player_name = models.CharField(max_length=64)
  height = models.DecimalField(max_digits=4, decimal_places=2)
  weight = models.DecimalField(max_digits=5, decimal_places=2)
  position = models.CharField(max_length=20, choices=bball_positions, default='water boy')

  def __str__(self):
     return self.player_name
  

class FootballPlayer(models.Model):
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  player_name = models.CharField(max_length=64)
  height = models.DecimalField(max_digits=4, decimal_places=2)
  weight = models.DecimalField(max_digits=5, decimal_places=2)
  fourty_yard_dash = models.DecimalField(max_digits=3, decimal_places=2)
  wonderlick_score = models.IntegerField(default=1, validators=[
    MaxValueValidator(50),
    MinValueValidator(1)
  ])