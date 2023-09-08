from django.urls import path
from . import views

urlpatterns = [
    path("", views.starting_page, name="starting-page"),
    path("posts", views.posts, name="all-posts-page"),
    path("posts/<slug:aslug>", views.single_post, name="single-post-page")
]


