from django.urls import path
from . import views

urlpatterns = [
    # path("", views.starting_page, name="starting-page"),
    # path("posts", views.posts, name="all-posts-page"),
    # path("posts/<slug:aslug>", views.single_post, name="single-post-page"),
    path("", views.StartingPageView.as_view(), name="starting-page"),
    path("posts", views.AllPostView.as_view(), name="all-posts-page"),
    path("posts/<slug:aslug>", views.SinglePostView.as_view(), name="single-post-page"),
]


