from django.contrib import admin
from olimpics.models import Atletic

class Atletics(admin.ModelAdmin):
  list_display = (
    'id',
    'name',
    'sex',
    'age',
    'height',
    'weight',
    'team',
    'noc',
    'games',
    'year',
    'season',
    'city',
    'sport',
    'event',
    'medal'
  )

  list_display_links = ('id', 'name')
  search_fields = ('name',)
  list_per_page = 30
  
admin.site.register(Atletic,  Atletics)