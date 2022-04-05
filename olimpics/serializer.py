from rest_framework import serializers
from olimpics.models import Atletic

class AtleticSerializer(serializers.ModelSerializer):
  class Meta:
    model = Atletic
    fields = [
      'id',
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