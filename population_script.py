import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gourmate.settings')

import django
django.setup()

from gourmate_app.models import Recipe, Category, User, UserProfile, Comment
from datetime import datetime


def add_category(name):
    category = Category.objects.get_or_create(name = name)[0]
    category.save()
    return category

def add_user(username, password, image, bio):
    user = User.objects.get_or_create(username = username)[0]
    user.set_password(password)
    user.save()
    user_profile = UserProfile.objects.get_or_create(user = user, picture = image, bio = bio)[0]
    user_profile.save()
    return user_profile

def add_recipe(category, user, title, views, likes, image, date, text):
    recipe = Recipe.objects.get_or_create(category = category, user = user, title = title, views = views, likes = likes,
                                          img = image, date = date, text = text)[0]
    recipe.save()
    return recipe

def add_comment(user, recipe, text, date, likes):
    comment = Comment.objects.get_or_create(user = user, recipe = recipe, text = text, date = date, likes = likes)[0]
    comment.save()
    return comment


def populate():

    categories = ['Italian', 'Mexican', 'American', 'French']

    users = [
        {'username': 'Homer',
         'password': 'password',
         'image': 'profile_images/homer.jpg',
         'bio': "Trying is the first step towards failure"},
        {'username': 'Bart',
         'password': 'password',
         'image': 'profile_images/bart.jpg',
         'bio': "I'm Bart Simpson. Who the hell are you?"},
        {'username': 'Lisa',
         'password': 'password',
         'image': 'profile_images/lisa.jpg',
         'bio': "Shut up, brain. I got friends now. I don't need you anymore."},
        {'username': 'Marge',
         'password': 'password',
         'image': 'profile_images/marge.jpeg',
         'bio': "Oh I’ve always wanted to use rosemary in something!"},
        {'username': 'Abe',
         'password': 'password',
         'image': 'profile_images/abe.jpg',
         'bio': "I used to be with it, but then they changed what it was."}
    ]

    recipes = [
        {'category': 'Italian',
         'user': 'Homer',
         'title': 'Classic Lasagne',
         'views': 200,
         'likes': 33,
         'date': '2021-01-26',
         'img': 'recipe_images/las.jfif',
         'text': """Step 1. Heat the oil in a large saucepan. Use kitchen scissors to snip the bacon into small pieces, 
         or use a sharp knife to chop it on a chopping board. Add the bacon to the pan and cook for just a few mins until starting to turn golden. 
         Add the onion, celery and carrot, and cook over a medium heat for 5 mins, stirring occasionally, until softened."""},
        {'category': 'Mexican',
         'user': 'Bart',
         'title': 'Burritos',
         'views': 44,
         'likes': 3,
         'date': '2021-01-14',
         'img': 'recipe_images/bur.jfif',
         'text': """STEP 1. Heat the oil in a large pan – a casserole is ideal. Fry the onions for 8 mins, then add the garlic, 
         spices and oregano and cook for 1 min. Crumble over the mince and sizzle for 5 mins, stirring, until browned. 
         Stir in the sugar and leave for a minute, then splash in the vinegar and pour in the tomatoes."""},
        {'category': 'American',
         'user': 'Abe',
         'title': 'Crispy Chicken',
         'views': 3010,
         'likes': 60,
         'date': '2021-01-23',
         'img': 'recipe_images/chicken.jfif',
         'text': """STEP 1. Heat the oven to 200C/fan 180C/gas 6. Put the potatoes in a large roasting tray, 
         add 2 tbsp of olive oil and season. Toss everything to coat then roast for 20 minutes."""},
        {'category': 'American',
         'user': 'Marge',
         'title': 'Perfect Pumpkin Pie',
         'views': 4300,
         'likes': 420,
         'date': '2021-01-10',
         'img': 'recipe_images/pie.jfif',
         'text': """STEP 1. Place the pumpkin in a large saucepan, cover with water and bring to the boil. 
         Cover with a lid and simmer for 15 mins or until tender. Drain pumpkin; let cool."""},
        {'category': 'American',
         'user': 'Homer',
         'title': 'Homemade New York Style Pizza',
         'views': 6100024,
         'likes': 50032,
         'date': '2021-01-03',
         'img': 'recipe_images/pizza.jfif',
         'text': """Pizza dough is a yeasted dough which requires active dry yeast. Make sure the check the 
         expiration date on the yeast package! Yeast that is too old may be dead and won't work. You can use all 
         purpose flour instead of the bread flour that is called for in the recipe, but bread flour is higher in gluten
          than all-purpose flour and will make a crispier crust for your pizza."""},
        {'category': 'French',
         'user': 'Lisa',
         'title': 'Healthy Salad',
         'views': 610,
         'likes': 1,
         'date': '2021-01-07',
         'img': 'recipe_images/salad.jfif',
         'text': """STEP 1. Put the potatoes in a pan of salted water, bring to the boil, then cover and simmer 
         for 8-10 mins or until cooked through – a cutlery knife should easily pierce them. Drain and leave to cool in a colander."""},
        {'category': 'French',
         'user': 'Lisa',
         'title': 'Autumn Vegetable Soup',
         'views': 696930,
         'likes': 11001,
         'date': '2021-01-06',
         'img': 'recipe_images/soup.jfif',
         'text': """STEP 1. Heat a large saucepan and dry-fry 2 tsp cumin seeds and a pinch of chilli flakes for 1 min, 
         or until they start to jump around the pan and release their aromas."""},
        {'category': 'American',
         'user': 'Bart',
         'title': 'Garlic Steak',
         'views': 14701,
         'likes': 11,
         'date': '2021-01-03',
         'img': 'recipe_images/steak.jfif',
         'text': """STEP 1. Sprinkle steak with salt and pepper. In a large skillet, heat remaining butter over medium heat. Add 
         steak; cook until meat reaches desired doneness (for medium-rare, a thermometer should read 135°; medium, 140°; medium-well,
          145°), 4-7 minutes per side. Serve with garlic butter."""}
    ]
    
    comments = [
        {'user': 'Marge',
         'recipe_title': 'Classic Lasagne',
         'text': 'Yum!',
         'date': '2021-02-03',
         'likes': '2'},
        {'user': 'Abe',
         'recipe_title': 'Classic Lasagne',
         'text': 'Like my mother used to make',
         'date': '2021-02-04',
         'likes': '1'},
        {'user': 'Homer',
         'recipe_title': 'Homemade New York Style Pizza',
         'text': 'I want it now',
         'date': '2021-02-05',
         'likes': '0'},
        {'user': 'Bart',
         'recipe_title': 'Healthy Salad',
         'text': 'Lame',
         'date': '2021-02-05',
         'likes': '0'},
        {'user': 'Lisa',
         'recipe_title': 'Burritos',
         'text': 'Real original title Bart',
         'date': '2021-02-05',
         'likes': '3'},
        {'user': 'Bart',
         'recipe_title': 'Autumn Vegetable Soup',
         'text': 'ew looks gross',
         'date': '2021-02-06',
         'likes': '1'},
        {'user': 'Marge',
         'recipe_title': 'Autumn Vegetable Soup',
         'text': 'Looks amazing sweetie',
         'date': '2021-02-06',
         'likes': '3'},
        {'user': 'Abe',
         'recipe_title': 'Autumn Vegetable Soup',
         'text': 'My favourite',
         'date': '2021-02-06',
         'likes': '2'},
        {'user': 'Homer',
         'recipe_title': 'Garlic Steak',
         'text': 'Turned out great',
         'date': '2021-02-08',
         'likes': '1'},
        {'user': 'Homer',
         'recipe_title': 'Perfect Pumpkin Pie',
         'text': 'mmmmhm pumpkin',
         'date': '2021-02-10',
         'likes': '2'},
        {'user': 'Lisa',
         'recipe_title': 'Perfect Pumpkin Pie',
         'text': 'kinda burnt it but it still tasted great!',
         'date': '2021-02-11',
         'likes': '0'},
        {'user': 'Homer',
         'recipe_title': 'Crispy Chicken',
         'text': 'Love this recipe',
         'date': '2021-02-01',
         'likes': '4'}
    ]

    print("Clearing the database")
    User.objects.all().delete()
    UserProfile.objects.all().delete()
    Category.objects.all().delete()
    Recipe.objects.all().delete()
    Comment.objects.all().delete()

    print("Adding categories")
    for category in categories:
        cat = add_category(category)
        print(f"{cat} category added")

    print("Adding users")
    for user in users:
        u = add_user(user['username'], user['password'], user['image'], user['bio'])
        print(f"User: {u} added")

    print("Adding recipes")
    for recipe in recipes:
        user_profile = UserProfile.objects.get(user__username = recipe['user'])
        category = Category.objects.get(name = recipe['category'])
        r = add_recipe(category, user_profile, recipe['title'], recipe['views'], recipe['likes'], recipe['img'], recipe['date'], recipe['text'])
        print(f"Recipe: {r} added")

    for comment in comments:
        user_profile = UserProfile.objects.get(user__username = comment['user'])
        recipe = Recipe.objects.get(title = comment['recipe_title'])
        com = add_comment(user_profile, recipe, comment['text'], comment['date'], comment['likes'])
        print(f"Comment: '{com}' added")

if __name__ == '__main__':
    print('Starting gourmate population script')
    populate()
