from django.contrib import admin
from gourmate_app.models import Recipe, UserProfile, Comment, Category

class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'views', 'likes')

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(UserProfile)
admin.site.register(Comment)
admin.site.register(Category)