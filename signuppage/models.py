from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import *
from django.utils.translation import ugettext_lazy as _

# Create your models here.


class signuppage(AbstractUser):

    Business_Type = models.CharField(max_length=100)
    Nature_of_Business = models.CharField(max_length=100)
    Country = models.CharField(max_length=100)
    UserType = models.CharField(max_length=100)
    Phone = models.CharField(max_length=30)

    def __str__(self):
        return self.email
