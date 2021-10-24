from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('recipes/', views.recipes_index, name='recipes_index'),
    path('recipes/<int:recipe_id>/', views.recipes_show, name='recipes_show'),
    path('recipes/create/', views.RecipeCreate.as_view(), name='recipes_create'),
    path('recipes/<int:pk>/update/', views.RecipeUpdate.as_view(), name='recipes_update'),
    path('recipes/<int:pk>/delete/', views.RecipeDelete.as_view(), name='recipes_delete'),
    path('user/<username>/', views.profile, name='profile'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_view, name='signup'),
    path('ingredients/', views.ingredients_index, name='ingredients_index'),
    path('ingredients/<int:ingredient_id>', views.ingredients_show, name='ingredients_show'),
    path('ingredients/create/', views.IngredientCreate.as_view(), name='ingredients_create'),
    path('ingredients/<int:pk>/update/', views.IngredientUpdate.as_view(), name='ingredients_update'),
    path('ingredients/<int:pk>/delete/', views.IngredientDelete.as_view(), name='ingredients_delete'),
    path('recipes/<int:recipe_id>/assoc_ingredient/<int:ingredient_id>', views.associate_ingredient, name='associate_ingredient'),
    path('recipes/<int:recipe_id>/unassoc_ingredient/<int:ingredient_id>', views.unassociate_ingredient, name='unassociate_ingredient'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
