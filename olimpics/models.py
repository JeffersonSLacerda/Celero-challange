import uuid
from django.db import models

class Athlete(models.Model):
  SEX = (
    ('M', 'Male'),
    ('F', 'Famale'),
    ('O', 'Other')
  )
  
  PODIUM = (
    ('G', 'Gold'),
    ('S', 'Silver'),
    ('B', 'Bronze'),
    ('NA', 'None')
  )
  
  id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
  athlete_id = models.IntegerField()
  name = models.CharField(max_length=256, blank=False)
  sex = models.CharField(max_length=1, choices=SEX, blank=True)
  age = models.IntegerField(null=True)
  height = models.IntegerField(null=True)
  weight = models.FloatField(null=True)
  team = models.CharField(max_length=256)
  noc = models.CharField(max_length=3)
  games = models.CharField(max_length=256)  
  year = models.IntegerField(blank=True)
  season = models.CharField(max_length=10)
  city = models.CharField(max_length=256)
  sport = models.CharField(max_length=256)
  event = models.CharField(max_length=256)
  medal = models.CharField(max_length=10, choices=PODIUM, blank=False, default='NA')

  def __str__(self):
    return self.name