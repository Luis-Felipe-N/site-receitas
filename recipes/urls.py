from unicodedata import name
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="index"),
    path('recipes/<int:id>/', views.recipe, name="recipes"),
    path('recipes/category/<int:category_id>/', views.category, name="category"),
]



