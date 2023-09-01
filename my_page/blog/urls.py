from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="starting-page"),
    path("posts", views.posts, name="all-posts-page"),
    path("posts/<slug:slug>", views.single_post, name="single-post-page")
]


