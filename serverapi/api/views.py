import re
from rest_framework.parsers import JSONParser
from rest_framework import status, response
from rest_framework.decorators import parser_classes
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from .models import Calculatorapi
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework import generics
from .serializers import CalculatorInputSerializer
#   if request.method == 'POST':
#       return JsonResponse({"message": "Got some data!", "data": JSONParser().parse(request.data)})
#   return Response({"message": "Hello, world!"})

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

bad_chars = ['?', '!', '@', '.', '#', '%', '&' ',' ']', '[', '[]', ]    
operation_add = ['add', 'addition', 'increment', '+', 'sum']
operation_sub = ['subtract', 'minus', 'remove', '-']
operation_multiply = ['multiply', 'multiplicattion', 'product', '*']

class CalculateView(GenericAPIView):
    serializer_class = CalculatorInputSerializer

    def post(self, request, *args, **kwargs):
        header = {
          "Access-Control-Allow-Origin":"*"
        }
        operation_type = self.request.data['operation_type']
        for i in bad_chars:
            operation_type = operation_type.replace(i, '')
        operation_sentence_list = self.request.data['operation_type'].split()
        if(self.request.data['x'] == ''):
            regex = '\d+'
            match = re.findall(regex, operation_type)

            request.data._mutable=True
            self.request.data['x'] = ''.join(map(str, match[0]))
            float(self.request.data['x'])

        if (self.request.data['y'] == ''):
            regex = '\d+'
            match = re.findall(regex, operation_type)
  
            request.data._mutable=True
            self.request.data['y'] = ''.join(map(str, match[1]))
            float(self.request.data['y'])
      
        x = self.request.data['x']
        y = self.request.data['y']
        check1 = any(item in operation_add for item in operation_sentence_list)
        check2 = any(item in operation_sub for item in operation_sentence_list)
        check3 = any(item in operation_multiply for item in operation_sentence_list)
        result = ''
        if check1 is True:
           result = float(x) + float(y)
           operation_type = 'Addition'
          #  print(result)
        elif check2 is True:
           result = float(x) - float(y)
           operation_type = 'Subtraction'
        elif check3 is True:
           result = float(x) * float(y)
           operation_type = 'Multiplication'
        else:
            return response.Response({ 'error':'invalid operator'}, status=status.HTTP_400_BAD_REQUEST, headers = header) 
        return response.Response({ "slackUsername": 'Genevieve_', 'operation_type':operation_type , 'result':result}, status=status.HTTP_200_OK, headers = header)




# class CreateView(generics.CreateAPIView):

#   serializer_class = CalculatorInputSerializer

#   def create(self, request, *args, **kwargs):
#     serializer = CalculatorInputSerializer(data=request.POST)
#     serializer.is_valid(raise_exception=True)
#     self.perform_create(serializer)
#     headers = self.get_success_headers(serializer.data)
#     response = CalculatorOutputSerializer(Calculatorapi).data
#     return Response(response, status=status.HTTP_201_CREATED, headers=headers)

# class RetrieveView(generics.RetrieveAPIView):
#   serializer_class = CalculatorOutputSerializer

#   def retrieve(self, request, *args, **kwargs):

#        serializer = CalculatorOutputSerializer(data=request.GET)
#        return Response(request.data, status=status.HTTP_200_OK)


