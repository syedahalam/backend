from django.contrib import admin
from .models import Movie, Rating
from mini.models import Rating

# Register your models here.
admin.site.register(Movie)
admin.site.register(Rating)
