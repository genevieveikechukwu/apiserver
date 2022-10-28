from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import generics
from .models import Serverapi
from .serializers import ServerapiSerializer
# Create your views here.

class ListServerapi(generics.ListAPIView):
    queryset = Serverapi.objects.all()
    serializer_class = ServerapiSerializer

class DetailServerapi(generics.RetrieveAPIView):
    queryset = Serverapi.objects.all()
    serializer_class = ServerapiSerializer