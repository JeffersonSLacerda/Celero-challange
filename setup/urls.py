from django.contrib import admin
from django.urls import path

from olimpics.views import atletic

urlpatterns = [
    path('admin/', admin.site.urls),
    path('atletics/', atletic),
]
