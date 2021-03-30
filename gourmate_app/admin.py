from django.contrib import admin
from gourmate_app.models import Recipe, UserProfile, Comment

# Register your models here.
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'views', 'likes', 'tags')

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(UserProfile)
admin.site.register(Comment)