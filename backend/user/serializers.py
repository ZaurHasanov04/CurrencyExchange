from rest_framework import serializers
from .models import *
import random
from datetime import datetime, timedelta
from rest_framework.validators import UniqueValidator
from django.conf import settings
from .utils import send_otp


class UserSerializer(serializers.ModelSerializer):
    """
    User Serializer.

    Used in POST and GET
    """

    password_first = serializers.CharField(
        write_only=True,
        min_length=settings.MIN_PASSWORD_LENGTH,
        error_messages={
            "min_length": "Password must be longer than {} characters".format(
                settings.MIN_PASSWORD_LENGTH
            )
        },
    )
    password_second = serializers.CharField(
        write_only=True,
        min_length=settings.MIN_PASSWORD_LENGTH,
        error_messages={
            "min_length": "Password must be longer than {} characters".format(
                settings.MIN_PASSWORD_LENGTH
            )
        },
    )

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "email",
            "password_first",
            "password_second"
        )
        read_only_fields = ("id",)

    def validate(self, data):
        """
        Validates if both password are same or not.
        """

        if data["password_first"] != data["password_second"]:
            print(data)
            raise serializers.ValidationError("Passwords do not match")
        return data
    

    def create(self, validated_data):
        """
        Create method.

        Used to create the user
        """
        otp = random.randint(1000, 9999)
        otp_expiry = datetime.now() + timedelta(minutes = 10)
        print(validated_data['username'])
        user = User(
            username = validated_data['username'],
            email=validated_data["email"],
            otp=otp,
            otp_expiry=otp_expiry,
        )
        
        user.set_password(validated_data["password_first"])
        print(user)
        user.save()
        send_otp(validated_data["email"], otp)
        return user