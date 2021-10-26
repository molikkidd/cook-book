from django.shortcuts import render, redirect
from .models import Recipe, Ingredient
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import NewSignUpForm, RecipeForm
from .forms import MyUserCreationForm
from cookbook.settings import db
import json



########### USER #############
def login_view(request):
    if request.method == 'POST':
        # try to log the user in
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            print('username', u)
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
    return redirect('/')

def signup_view(request):
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            email = form.data.get('email')
            password = form.data.get('password')
            username = form.data.get('username')
            new_user = User.objects.create(username=username, password=password, email=email)
            new_user.save()
            login(request, new_user)
            return redirect('/user' + str(new_user))
        else:
            return HttpResponse('<h1>Try Again</h1>')
    else:
        # form = NewSignUpForm()
        form = MyUserCreationForm()
        # form.order_fields(["email", "password"])
        # print('userform', form)
        return render(request, 'signup.html', {'form': form})

@login_required
def profile(request, username):
    user = User.objects.get(username=username)
    recipes = Recipe.objects.filter(user=user)
    return render(request, 'profile.html', {'username': username,'recipes': recipes})

############# RECIPES ###############

# django will make a create recipe form for us!
@method_decorator(login_required, name='dispatch')
class RecipeCreate(CreateView):
    model = Recipe
    fields = '__all__'
    success_url = '/recipes/'

    form = RecipeForm()
    print('new recipe form', form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        print('!!!!! SELF.OBJECT:', self.object)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect('/recipes')

class RecipeUpdate(UpdateView):
    model = Recipe
    fields = ['name', 'breed', 'description', 'age', 'ingredients']

    def form_valid(self, form): # this will allow us to catch the pk to redirect to the show page
        self.object = form.save(commit=False) # don't post to the db until we say so
        self.object.save()
        return HttpResponseRedirect('/recipes/'+str(self.object.pk))

class RecipeDelete(DeleteView):
    model = Recipe
    success_url = '/recipes'

def recipes_index(request):
    # Get all cats from the db
    recipes = Recipe.objects.all()
    return render(request, 'recipes/index.html', {'recipes': recipes})

def recipes_show(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    ingredients = Ingredient.objects.all()
    return render(request, 'recipes/show.html', {'recipe': recipe, 'ingredients': ingredients})

########## INGREDIENTS ################

def ingredients_index(request):
    ingredients = Ingredient.objects.all()
    return render(request, 'ingredients/index.html', {'ingredients': ingredients})

def ingredients_show(request,  ingredient_id):
    ingredient = Ingredient.objects.get(id=ingredient_id)
    return render(request, 'ingredients/show.html', {'ingredient': ingredient})

class IngredientCreate(CreateView):
    model = Ingredient
    fields = '__all__'
    success_url = '/ingredients'

class IngredientUpdate(UpdateView):
    model = Ingredient
    fields = ['name', 'color']
    success_url = '/ingredients'

class IngredientDelete(DeleteView):
    model = Ingredient
    success_url = '/ingredients'

def associate_ingredient(request, recipe_id, ingredient_id):
    Recipe.objects.get(id=recipe_id).ingredients.add(ingredient_id)
    # return HttpResponseRedirect('/cats/'+str(cat_id)+'/')
    return redirect('recipes_show', recipe_id=recipe_id)

def unassociate_ingredient(request, recipe_id, ingredient_id):
    Recipe.objects.get(id=recipe_id).ingredients.remove(ingredient_id)
    return HttpResponseRedirect('/recipes/'+str(recipe_id)+'/')

########### DEFAULT ###################

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def seedingreds(request):
    Spices = [
        "Cardamom", 
        "Cayenne", 
        "Cinnamon", 
        "Clove",
        "Coriander", 
        "Ginger", 
        "Juniper", 
        "Vanilla",
        "Turmeric", 
        "Anise", 
        "Peppercorn", 
        "Fenugreek",
        "Cumin", 
        "Mace", 
        "Salt", 
        "Allspice",
        "Saffron", 
        "Licorice",
    ]
    # for spice in Spices:
    #     ingred = {
    #             'type': 'Spices',
    #             'category': 'vegan',
    #         }
    #     ingred.__setitem__("name", spice)
    #     # print('list of herbs',ingred)
    #     new_ingred = Ingredient.objects.create(type=str(ingred.get("type")), category=str(ingred.get("category")), name=str(ingred.get("name")))
    #     # new_ingred.save()
    #         # print('list of veggies',ingred)
    # all_ingreds = Ingredient.objects.all()
    # print(list(all_ingreds))