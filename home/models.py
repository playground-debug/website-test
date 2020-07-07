from django.db import models
from django.contrib import auth
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class User(models.Model):
    user = models.OneToOneField(auth.models.User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    age = models.IntegerField(validators=[MinValueValidator(10),
                                          MaxValueValidator(999)])
