from django.urls import path
from gourmate_app import views

app_name = 'gourmate'

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/<username>/', views.profile, name='profile'),
    path('register_profile/', views.register_profile, name='register_profile'),
    path('like_recipe/', views.like_recipe, name='like_recipe'),
    path('contact_us/', views.contact_us, name='contact_us'),
    #path('categories/', views.categories, name='categories'),
    path('category/<slug:category_name_slug>/', views.show_category, name='show_category'),
    #path('category/<slug:category_name_slug>/<recipe_title>/', views.recipe, name='recipe'),
    path('<recipe_title>/', views.recipe, name='recipe'),
    path('category/<slug:category_name_slug>/add_recipe/', views.add_recipe, name='add_recipe'),
    path('recent_recipes/', views.recent_recipes, name='recent_recipes'),
    path('liked_recipes/', views.liked_recipes, name='liked_recipes'),
    path('popular_recipes/', views.popular_recipes, name='popular_recipes')
]


