from django.urls import path
from .views import *


urlpatterns = [
    path('', LoginTokerSerializer.as_view(), name='user')
]