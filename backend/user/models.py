from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)
from django.core.validators import RegexValidator, validate_email
# Create your models here.


class UserManager(BaseUserManager):
    """
    User Manager.
    To create superuser.
    """

    def create_user(self,username, email, password=None):
        user = self.model(username=username, email=email)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email,password):
        user = self.create_user(
            username=username,
            email=email,
            password=password
        )
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user



class User(AbstractBaseUser, PermissionsMixin):
    """
    Custom User model.
    """

    username = models.CharField(max_length=20, unique=True ,blank=False, null=False)
    email = models.EmailField(
        max_length=50,
        blank=True,
        null=True,
        validators=[validate_email],
    )
    otp = models.CharField(max_length=6)
    otp_expiry = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    user_registered_at = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS=['email']
    objects = UserManager()

    def __str__(self):
        return self.username

