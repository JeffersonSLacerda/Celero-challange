from rest_framework import viewsets
from olimpics.models import Athlete
from olimpics.serializer import AthleteSerializer

from rest_framework.pagination import PageNumberPagination

class AthleteSetPagination(PageNumberPagination):
    page_size = 25
    page_size_query_param = 'page_size'

class AthleteViewSet(viewsets.ModelViewSet):
  "Showing all athletes"
  queryset = Athlete.objects.all()
  serializer_class = AthleteSerializer
  pagination_class = AthleteSetPagination
  
  