from django.db import models
from django.template.defaultfilters import slugify
from taggit.managers import TaggableManager

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Recipe(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    img = models.ImageField(upload_to='recipe_images')
    text = models.TextField()
    tags = TaggableManager()

    def __str__(self):
        return self.title