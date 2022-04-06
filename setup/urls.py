from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from olimpics.views import AthleteViewSet

router = routers.DefaultRouter()
router.register('athletes', AthleteViewSet, basename='Athlete')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
