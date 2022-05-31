from django.db import models
from helpers.models import TrackingModel
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

# Create your models here.

class User(TrackingModel, AbstractBaseUser,PermissionsMixin):
    pass