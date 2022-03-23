from django.shortcuts import get_object_or_404, get_list_or_404, render
from django.utils import timezone
from recipes.models import Recipe

def home(request):

    recipes = Recipe.objects.filter(is_published=True).order_by('create_at')

    context = {
        "recipes": recipes
    }

    return render(request, 'recipes/pages/index.html', context)

def category(request, category_id):

    recipe = get_list_or_404(Recipe.objects.filter(category__id=category_id, is_published=True).order_by('create_at'))


    context = {
        "recipes": recipe,
        "category":  recipe[0].category
    }

    return render(request, 'recipes/pages/category.html', context)

def recipe(request, id):

    recipe = get_object_or_404(Recipe, id=id)

    context = {
        "recipe": recipe,
        "is_details": True
    }

    return render(request, 'recipes/pages/recipe-view.html', context)