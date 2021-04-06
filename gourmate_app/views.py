from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.defaultfilters import title
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from gourmate_app.forms import UserForm, UserProfileForm, CommentForm, RecipeForm
from datetime import datetime
from gourmate_app.models import Recipe, UserProfile, Comment, Category
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import datetime

def index(request):
    context_dict = {}
    context_dict['recipes'] = Recipe.objects.all()
    return render(request, 'gourmate/index.html', context=context_dict)


def restricted(request):
    return render(request, 'gourmate/restricted.html')

@login_required
def add_recipe(request, category_name_slug):
    try:
        category = Category.objects.get(slug=category_name_slug)
    except Category.DoesNotExist:
        category = None

    if category is None:
        return redirect(reverse('gourmate:index'))

    form = RecipeForm()
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit = False)
            recipe.user = UserProfile.objects.get(user = request.user)
            recipe.category = category
            recipe.views = 0
            recipe.likes = 0
            recipe.date = datetime.now()
            recipe.save()
            return redirect(reverse('gourmate:show_category', kwargs={'category_name_slug': category_name_slug}))
        else:
            print(form.errors)
    context_dict = {'form': form, 'category': category}
    return render(request, 'gourmate/add_recipe.html', context_dict)


def popular_recipes(request):
    context_dict = {}
    context_dict['recipes'] = Recipe.objects.all()
    return render(request, 'gourmate/popular_recipes.html', context_dict)


def recent_recipes(request):
    context_dict = {'recipes': Recipe.objects.order_by('-date')[:10]}
    return render(request, 'gourmate/recent_recipes.html', context_dict)


def liked_recipes(request):
    context_dict = {'recipes': Recipe.objects.order_by('-likes')[:10]}
    return render(request, 'gourmate/liked_recipes.html', context_dict)

def profile(request, username):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return redirect(reverse('gourmate:index'))
    user_profile = UserProfile.objects.get_or_create(user=user)[0]
    form = UserProfileForm({'picture': user_profile.picture,
                            'bio': user_profile.bio})
    if request.method == 'POST':
        if request.user == user:
            form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
            if form.is_valid():
                form.save(commit=True)
                return redirect('gourmate:profile', user.username)
            else:
                print(form.errors)

    context_dict = {'user_profile': user_profile,
                    'selected_user': user,
                    'form': form}
    return render(request, 'gourmate/profile.html', context_dict)

@login_required
def register_profile(request):
    form = UserProfileForm()
    if request.method == "POST":
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            user_profile = form.save(commit=False)
            user_profile.user = request.user
            user_profile.save()
            return redirect(reverse('gourmate:index'))
        else:
            print(form.errors)

    context_dict = {'form': form}
    return render(request, 'gourmate/profile_registration.html', context=context_dict)

@login_required
def like_recipe(request):
    recipe_id = request.GET["recipe_id"]
    try:
        recipe = Recipe.objects.get(id=int(recipe_id))
    except Recipe.DoesNotExist:
        return HttpResponse(-1)
    except ValueError:
        return HttpResponse(-1)

    recipe.likes = recipe.likes + 1
    recipe.save()
    return HttpResponse(recipe.likes)

@login_required
def like_comment(request):
    comment_id = request.GET["comment_id"]
    try:
        comment = Comment.objects.get(id=int(comment_id))
    except Comment.DoesNotExist:
        return HttpResponse(-1)
    except ValueError:
        return HttpResponse(-1)

    comment.likes = comment.likes + 1
    comment.save()
    return HttpResponse(comment.likes)

def categories(request):
    context_dict = {}
    try:
        context_dict['categories'] = Category.objects.all()
    except Category.DoesNotExist:
        context_dict['categories'] = None

    return render(request, 'gourmate/categories.html', context=context_dict)

def recipe(request, recipe_title):
    context_dict = {}
    try:
        recipe = Recipe.objects.get(title=recipe_title)
        recipe.views += 1
        recipe.save()
        context_dict['recipe'] = recipe
        context_dict['comments'] = Comment.objects.filter(recipe=recipe)
    except Recipe.DoesNotExist:
        recipe = None
        context_dict['recipe'] = None
        context_dict['comments'] = None

    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            if recipe:
                comment = form.save(commit=False)
                user = UserProfile.objects.get_or_create(user=request.user)[0]
                comment.user = user
                comment.recipe = recipe
                comment.date = datetime.now()
                comment.likes = 0
                comment.save()
                return redirect(reverse('gourmate:recipe', kwargs={'recipe_title': recipe_title}))
            else:
                print(form.errors)
    context_dict['form'] = form
    return render(request, "gourmate/recipe.html", context_dict)


def show_category(request, category_name_slug):
    context_dict = {}
    try:
        category = Category.objects.get(slug=category_name_slug)
        recipes = Recipe.objects.filter(category=category).order_by('-views')
        context_dict['recipes'] = recipes
        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['recipes'] = None
        context_dict['category'] = None

    return render(request, 'gourmate/category.html', context=context_dict)

def contact_us(request):
    return render(request, 'gourmate/contact_us.html')






