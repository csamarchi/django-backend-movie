from django.urls import path
from .views import movies

urlpatterns = [
    path('movies/', Movies.as_view())
]
