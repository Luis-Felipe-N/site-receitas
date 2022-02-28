from django.shortcuts import render

def home(request):
    context = {

    }

    return render(request, 'recipes/pages/index.html', context)

def recipes(request, id):
    context = {
        "id": id
    }

    return render(request, 'recipes/pages/recipe-view.html', context)