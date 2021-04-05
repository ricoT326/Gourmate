from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from gourmate_app.forms import UserForm, UserProfileForm, CommentForm, RecipeForm
from datetime import datetime
from gourmate_app.models import Recipe, UserProfile, Comment


def index(request):
    context_dict = {}
    context_dict['recipes'] = Recipe.objects.all()
    return render(request, 'gourmate/popular_recipes.html', context=context_dict)


def restricted(request):
    return render(request, 'gourmate/restricted.html')

@login_required
def recipe(request, num):
    context_dict = {}
    context_dict['recipes'] = Recipe.objects.all()
    recipe = Recipe.objects.get(num = num)
    context_dict['recipe'] = recipe
    context_dict['comments'] = Comment.objects.all().filter(recipe = context_dict['recipe'])
    recipe.views += 1
    recipe.save()
    return render(request, 'gourmate/recipe.html')

@login_required
def add_recipe(request):
    if request.method == 'POST':
        add_recipe = RecipeForm(request.POST)
        if add_recipe.is_valid():
            recipe = add_recipe.save(commit = False)
            user = UserProfile.objects.get(user = request.user)

    return render(request, 'gourmate/add_recipe.html')


def popular_recipes(request):
    context_dict={}
    #context_dict=['recipe'] = Recipe.objects.all()
    context_dict['popular recipes'] = {'Popular Recipes': Recipe.order_by('likes')}
    return render(request, 'gourmate/popular_recipes.html', context = context_dict)





