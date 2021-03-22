from django import forms
from rango.models import Recipe

class RecipeForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text="Please enter the title of the recipe.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    img = forms.ImageField()
    text = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Recipe
        fields = ('title', 'img', 'text', 'tags',)