from django.contrib import admin
from gourmate_app.models import Category, Recipe

# Register your models here.
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('category', 'title', 'views', 'likes', 'tags')

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())

admin.site.register(Recipe, RecipeAdmin)

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Category, CategoryAdmin)
