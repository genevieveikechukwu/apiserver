from django.shortcuts import render

# Create your views here.
# from django.shortcuts import render
# from rest_framework import generics
from .models import Serverapi
# from .serializers import ServerapiSerializer
# Create your views here.

from rest_framework.decorators import api_view

from django.http import JsonResponse

@api_view(["GET"])
def home(request, *args, **kwargs):
  header = {"Access-Control-Allow-Origin":"*"}
  data = {
    "slackUsername":"Genevieve",
    "backend":True,
    "age": 18,
    "bio":"your bio"
  }
  return JsonResponse(data, headers=header)
# @api_view(["GET, POST"])
# def calculate(request, *args, **kwargs):
#   header = {"Access-Control-Allow-Origin":"*"}
#   data = {
#     "operation_type":"",
#     "x":
#     "y":
#   }
#   return JsonResponse(data, headers=header)


# class ListServerapi(generics.ListAPIView):
#     queryset = Serverapi.objects.all()
#     serializer_class = ServerapiSerializer

# class DetailServerapi(generics.RetrieveAPIView):
#     queryset = Serverapi.objects.all()
#     serializer_class = ServerapiSerializer