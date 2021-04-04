from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from gourmate.forms import UserForm, UserProfileForm, CommentForm, RecipeForm
from datetime import datetime
from gourmate.models import Recipe, UserProfile, Comment


def index(request):
    context_dict = {}
    context_dict['visits'] = request.session['visits']
    return render(request, 'gourmate/popular_recipes.html', context=context_dict)


def restricted(request):
    return render(request, 'gourmate/restricted.html')


def recipe(request):
    context_dict = {}
    context_dict['Recipe'] = Recipe.objects.all()
    recipe = Recipe.objects.all()
    views = Recipe.views
    return render(request, 'gourmate/recipe.html')

@login_required
def add_recipe(request):
    if request.method == 'POST':
        add_recipe = RecipeForm(request.POST)
    return render(request, 'gourmate/add_recipe.html')




'['