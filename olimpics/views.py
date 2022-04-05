from rest_framework import viewsets
from olimpics.models import Atletic
from olimpics.serializer import AtleticSerializer

class AtleticViewSet(viewsets.ModelViewSet):
  "Showing all atletics"
  queryset = Atletic.objects.all()
  serializer_class = AtleticSerializer
  
  