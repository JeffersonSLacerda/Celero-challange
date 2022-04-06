from rest_framework import serializers
from olimpics.models import Athlete

class AthleteSerializer(serializers.ModelSerializer):
  class Meta:
    model = Athlete
    fields = [
      'id',
      'athlete_id',
      'name',
      'sex',
      'age',
      'height',
      'weight',
      'team',
      'noc',
      'games',
      'year'
    ]