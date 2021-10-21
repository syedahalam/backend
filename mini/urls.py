from django.urls import path
from . import views

urlpatterns = [
    path('movies/', views.MovieList.as_view(),
    name="movie_list"),
    path('movies/<int:pk>', views.MovieDetail.as_view(),
    name="movie_detail"),
    path('ratings/', views.RatingList.as_view(),
    name="rating_list"),
    path('ratings/<int:pk>', views.RatingDetail.as_view(),
    name="rating_detail")
]
