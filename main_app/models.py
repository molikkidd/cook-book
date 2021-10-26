from os import name
from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.forms.forms import Form
from django.forms import ModelForm

class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Recipe(models.Model):
    title = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ingredients = models.ManyToManyField(Ingredient)
    def __str__(self):
        return self.title
# recipe form with steps
class RecipeSteps(models.Model):
    recipe = models.ForeignKey(Recipe)
    steps = models.CharField()

class RecipeForm(forms.ModelForm):
    title = forms.CharField(label="Title", max_length=100, required=True)
    steps_0 = forms.CharField(label="Steps", max_length=100, required=True)
    steps_1 = forms.CharField(label="Steps", max_length=100, required=True)
    steps_2 = forms.CharField(label="Steps", max_length=100, required=True)
    def save(self):
        Recipe = self.instance
        Recipe.title = self.cleaned_data[title]

        # recipe.steps_set.all().delete()
        # For i in range(3):
        #     steps = self.cleaned_data[“steps_{}”.format(i)]
        #     RecipeSteps.objects.create(recipe=recipe, steps=steps)
