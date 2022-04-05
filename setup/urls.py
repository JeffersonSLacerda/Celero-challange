from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from olimpics.views import AtleticViewSet

router = routers.DefaultRouter()
router.register('atletics', AtleticViewSet, basename='Atletic')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
