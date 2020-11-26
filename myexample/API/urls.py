from django.urls import path

from . import views
from API.views import SedeList

urlpatterns = [
    path('sedes', SedeList.as_view(), name='List-sedes'),
]