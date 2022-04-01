import uuid
from django.db import models

class Atletic(models.Model):
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
  name = models.CharField(max_length=50, blank=False)
  sex = models.CharField(max_length=1, choices=SEX, blank=True)
  age = models.IntegerField()
  height = models.IntegerField()
  weight = models.IntegerField()
  team = models.CharField(max_length=50)
  noc = models.CharField(max_length=3)
  games = models.CharField(max_length=50)  
  year = models.IntegerField()
  season = models.CharField(max_length=10)
  city = models.CharField(max_length=50)
  sport = models.CharField(max_length=50)
  event = models.CharField(max_length=50)
  medal = models.CharField(max_length=2, choices=PODIUM, blank=False, default='NA')

  def __str__(self):
    return self.name