from django.shortcuts import render
from django.utils import timezone

def home(request):

    recipes = [
        {
            "title": "torta de Abobora",
            "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis non elementum elit. In quis justo nec nibh tincidunt lacinia ac vitae lacus. Suspendisse nec est tellus. Nunc id magna sed ligula hendrerit tristique. Mauris dignissim non dui sed condimentum. Sed eget vestibulum massa. Nullam scelerisque, felis id iaculis porttitor, nisl velit scelerisque purus, a auctor eros est sed nisi. Donec sit amet magna ac tortor laoreet fermentum in in purus.",
            "preparation_time": 10,
            "preparation_time_unit": 'Minutos',
            "servings": 1,
            "servings_unit": "Prato",
            "cover": {
                "url": 'https://images.pexels.com/photos/7125710/pexels-photo-7125710.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500'
            },
            "author": {
                "first_name": "Luis Felipe",
                "last_nam": "Nunes de Carvalho"
            },
            "category": "Café da manhã",
            "created_at": timezone.now(),
            "preparation_steps": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis non elementum elit. In quis justo nec nibh tincidunt lacinia ac vitae lacus. Suspendisse nec est tellus. Nunc id magna sed ligula hendrerit tristique. Mauris dignissim non dui sed condimentum. Sed eget vestibulum massa. Nullam scelerisque, felis id iaculis porttitor, nisl velit scelerisque purus, a auctor eros est sed nisi. Donec sit amet magna ac tortor laoreet fermentum in in purus."
        },
        {
            "title": "Hamburge",
            "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis non elementum elit. In quis justo nec nibh tincidunt lacinia ac vitae lacus. Suspendisse nec est tellus. Nunc id magna sed ligula hendrerit tristique. Mauris dignissim non dui sed condimentum. Sed eget vestibulum massa. Nullam scelerisque, felis id iaculis porttitor, nisl velit scelerisque purus, a auctor eros est sed nisi. Donec sit amet magna ac tortor laoreet fermentum in in purus.",
            "preparation_time": 8,
            "preparation_time_unit": 'Minutos',
            "servings": 1,
            "servings_unit": "Prato",
            "cover": {
                "url": 'https://images.pexels.com/photos/1639557/pexels-photo-1639557.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500'
            },
            "author": {
                "fisrt_name": "João Felipe",
                "last_nam": "Nunes de Carvalho"
            },
            "category": "Lanche",
            "created_at": timezone.now(),
            "preparation_steps": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis non elementum elit. In quis justo nec nibh tincidunt lacinia ac vitae lacus. Suspendisse nec est tellus. Nunc id magna sed ligula hendrerit tristique. Mauris dignissim non dui sed condimentum. Sed eget vestibulum massa. Nullam scelerisque, felis id iaculis porttitor, nisl velit scelerisque purus, a auctor eros est sed nisi. Donec sit amet magna ac tortor laoreet fermentum in in purus."
        }
    ]


    context = {
        "recipes": recipes
    }

    return render(request, 'recipes/pages/index.html', context)

def recipes(request, id):
    context = {
        "recipe": {
            "id": id,
            "title": "Hamburge",
            "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis non elementum elit. In quis justo nec nibh tincidunt lacinia ac vitae lacus. Suspendisse nec est tellus. Nunc id magna sed ligula hendrerit tristique. Mauris dignissim non dui sed condimentum. Sed eget vestibulum massa. Nullam scelerisque, felis id iaculis porttitor, nisl velit scelerisque purus, a auctor eros est sed nisi. Donec sit amet magna ac tortor laoreet fermentum in in purus.",
            "preparation_time": 8,
            "preparation_time_unit": 'Minutos',
            "servings": 1,
            "servings_unit": "Prato",
            "cover": {
                "url": 'https://images.pexels.com/photos/1639557/pexels-photo-1639557.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500'
            },
            "author": {
                "fisrt_name": "João Felipe",
                "last_nam": "Nunes de Carvalho"
            },
            "category": "Lanche",
            "created_at": timezone.now(),
            "preparation_steps": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis non elementum elit. In quis justo nec nibh tincidunt lacinia ac vitae lacus. Suspendisse nec est tellus. Nunc id magna sed ligula hendrerit tristique. Mauris dignissim non dui sed condimentum. Sed eget vestibulum massa. Nullam scelerisque, felis id iaculis porttitor, nisl velit scelerisque purus, a auctor eros est sed nisi. Donec sit amet magna ac tortor laoreet fermentum in in purus.linebreaksbr¶"
        },
        "is_details": True
    }

    return render(request, 'recipes/pages/recipe-view.html', context)