from django.http import HttpResponse

# Create your views here.
from rest_framework import generics
from API.models import Sede
from API.serializers import SedeSerializer

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

class SedeList(generics.ListAPIView):
    queryset = Sede.objects.all()
    serializer_class = SedeSerializer

class SedeList(generics.ListAPIView):
    queryset = Sede.objects.all()
    serializer_class = SedeSerializer