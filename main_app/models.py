from django.db import models
from django.contrib.auth.models import User
# from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

# Create your models here.
# class User(AbstractUser): 
#    email = models.CharField(max_length=100, unique=True)
#    password_copy = models.CharField(max_length=50)

class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    def __str__(self):
        return self

class Recipe(models.Model):
    title = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ingredients = models.ManyToManyField(Ingredient)
    def __str__(self):
        return self.title
    