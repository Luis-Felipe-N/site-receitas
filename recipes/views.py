from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

def home(request):
    context = {

    }

    return render(request, 'recipes/index.html', context)
