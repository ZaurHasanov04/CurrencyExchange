from django.shortcuts import render
import requests
import xmltodict
from .models import *
import re
import datetime
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.




class CurrencyApiView(APIView):

    def get(self, request):

        currency = Currency.objects.all().order_by('-value','code')
        
        serializer = CurrencySerializer(currency, many=True)

        return Response(serializer.data)


