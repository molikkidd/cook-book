from django.contrib import admin
from .models import Recipe, Ingredient
from django.contrib.auth.admin import UserAdmin

from .forms import MyUserCreationForm
from .models import User

# Register your models here.
admin.site.register(Recipe)
admin.site.register(Ingredient)