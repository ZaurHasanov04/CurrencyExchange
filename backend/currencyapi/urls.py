from django.urls import path
from .views import *


urlpatterns = [
    path('api', CurrencyApiView.as_view(), name='currency')
]