from django.db import models
from django.contrib.auth.models import User
from mongoengine import Document, fields
# from djangotoolbox.fields import EmbeddedModelField

# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    # recipe = models.ForeignKey(Recipes, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    title = models.CharField(max_length=100)
    steps = []
    pictures = []
    # ingredients = models.EmbeddedModelField('Ingredient')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self

