from django.shortcuts import render
from rest_framework import generics, viewsets, status
from .serializers import *
from .models import *
from rest_framework.decorators import action
from datetime import datetime
from rest_framework.response import Response
from django.utils import timezone
# Create your views here.



class UserViewSet(viewsets.ModelViewSet):
    """
    User View.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=True, methods=["PATCH"])
    def verify_otp(self, request, pk=None):
        instance = self.get_object()
        if (
            not instance.is_active
            and instance.otp == request.data.get("otp")
            and instance.otp_expiry
            and timezone.now() < instance.otp_expiry
        ):
            instance.is_active = True
            instance.otp_expiry = None
            instance.save()
            return Response(
                "Successfully verified the user.", status=status.HTTP_200_OK
            )

        return Response(
            "User active or Please enter the correct OTP.",
            status=status.HTTP_400_BAD_REQUEST,
        )