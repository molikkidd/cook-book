from django.shortcuts import render, redirect
from .models import Recipe, Ingredient
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from cookbook.settings import db
import json

########### USER #############
def login_view(request):
    if request.method == 'POST':
        # try to log the user in
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = authenticate(username = u, password = p)
            if user is not None:
                if user.is_active:
                    login(request, user) # log the user in by creating a session
                    return redirect('/user/'+u)
                else:
                    print('The account has been disabled.')
                    return redirect('/login')
        else:
            print('The username and/or password is incorrect.')
            return redirect('/login')
    else: # it was a GET request so send the empty login form
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('/cats')

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/user/'+str(user))
        else:
            return HttpResponse('<h1>Try Again</h1>')
    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})

@login_required
def profile(request, username):
    user = User.objects.get(username=username)
    recipes = Recipe.objects.filter(user=user)
    return render(request, 'profile.html', {'username': username,'recipes': recipes})

############# CATS ###############

# django will make a create cat form for us!
@method_decorator(login_required, name='dispatch')
class RecipeCreate(CreateView):
    model = Recipe
    fields = '__all__'
    success_url = '/recipes/'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        print('!!!!! SELF.OBJECT:', self.object)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect('/cats')

class RecipeUpdate(UpdateView):
    model = Recipe
    fields = ['title', 'steps', 'pictures', 'ingredients']

    def form_valid(self, form): # this will allow us to catch the pk to redirect to the show page
        self.object = form.save(commit=False) # don't post to the db until we say so
        self.object.save()
        return HttpResponseRedirect('/recipes/'+str(self.object.pk))

class RecipeDelete(DeleteView):
    model = Recipe
    success_url = '/recipes'

def recipe_index(request):
    # Get all cats from the db
    recipes = Recipe.objects.all()
    return render(request, 'recipe/index.html', {'recipes': recipes})

def recipe_show(request, cat_id):
    recipes = Recipe.objects.get(id=cat_id)
    ingredients = Ingredient.objects.all()
    return render(request, 'recipe/show.html', {'recipes': recipes, 'ingredients': ingredients})

########## CATTOYS ################

def ingredients_index(request):
    ingredients = Ingredient.objects.all()
    return render(request, 'ingredients/index.html', {'ingredients': ingredients})

def ingredients_show(request, ingredient_id):
    ingredients = Ingredient.objects.get(id=ingredient_id)
    return render(request, 'ingredients/show.html', {'ingredients': ingredients})

class IngredientCreate(CreateView):
    model = Ingredient
    fields = '__all__'
    success_url = '/cattoys'

class IngredientUpdate(UpdateView):
    model = Ingredient
    fields = ['name', 'type', 'category']
    success_url = '/ingredients'

class IngredientDelete(DeleteView):
    model = Ingredient
    success_url = '/ingredients'

def associate_toy(request, recipe_id, ingredient_id):
    Recipe.objects.get(id=recipe_id).ingredients.add(ingredient_id)
    # return HttpResponseRedirect('/cats/'+str(cat_id)+'/')
    return redirect('recipes_show', recipe_id=recipe_id)

def unassociate_toy(request, recipe_id, ingredient_id):
    Recipe.objects.get(id=recipe_id).ingredients.remove(ingredient_id)
    return HttpResponseRedirect('/recipes/'+str(recipe_id)+'/')

########### DEFAULT ###################

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def all_users(request):
    all_users = db.users.find()
    newList = list(all_users)
    # print(newList)
    
    for users in range(0,5):
        print(users['id'])
        # counters = newList[users].get(u'newListCounters', {})
        # if hasattr(counters, 'get'):
        #     print users, "inOctets", counters.get(u'inOctets', {}), "outOctets:", counters.get(u'outOctets',  {})
        return users['id']
    # all_users = list(getattr(all_users,'firstName'))
    # all_users = str(all_users)
    # all_users = json.dumps(all_users)
    return all_users