from django.contrib.auth.models import User
from django.db import models

class Category(models.Model):
    name = models.CharField(
        max_length=196
    )

    def __str__(self):
        return self.name
    



class Recipe(models.Model):
    title = models.CharField(
        max_length=96
    )

    description = models.CharField(
        max_length=196
    )

    slug = models.SlugField()

    preparation_time = models.IntegerField()

    preparation_time_unit = models.CharField(
        max_length=96
    )

    servings = models.IntegerField()

    servings_unit = models.CharField(
        max_length=96
    )

    preparation_steps = models.TextField()

    preparation_steps_is_html = models.BooleanField(default=False)
 
    create_at = models.DateTimeField(
        auto_now_add=True
    )

    update_at = models.DateTimeField(
        auto_now=True
    )

    is_published = models.BooleanField(
        default=False
        )

    cover = models.ImageField(
        upload_to='recipes/cover/%Y/%m/%d/'
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    author = models.ForeignKey(
        User,
          on_delete=models.SET_NULL,
        null=True        
    )
    
    def __str__(self):
        return self.title
    
