from django.contrib import admin
from gourmate_app.models import Category, Recipe

# Register your models here.
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'views', 'likes')

admin.site.register(Recipe, RecipeAdmin)

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Category, CategoryAdmin)