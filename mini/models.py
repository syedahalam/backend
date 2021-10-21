from django.db import models
from django.db.models.fields import CharField
from django.contrib.auth.models import User
# from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Movie(models.Model):
    director = models.CharField(max_length=100)
    title = models.CharField(max_length=32)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Rating(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
