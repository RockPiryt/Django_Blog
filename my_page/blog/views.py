# from datetime import date
from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views import View
from django.urls import reverse
from django.http import HttpResponseRedirect

from .models import Post
from .forms import CommentForm



# Create your views here.
#-------------------------------------------------------------class Views
class StartingPageView(ListView):
    template_name = "blog/index.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "html_posts"

    def get_queryset(self):
        default_queryset = super().get_queryset()
        sliced_data = default_queryset[:3]
        return sliced_data

class AllPostView(ListView):
    template_name = "blog/all-posts.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "html_all_posts"

class SinglePostView(View):
    def get(self, request, aslug):
        single_post = Post.objects.get(slug=aslug)
        html_context={
            "html_post": single_post,
            "html_tags_for_post": single_post.tags.all(),
            "html_comment_form": CommentForm(),
            "html_comments":single_post.aacomments.all().order_by("-id"),
        }
        return render(request, "blog/post-detail.html", html_context)

    def post(self, request, aslug):
        post_comment_form = CommentForm(request.POST)
        psingle_post = Post.objects.get(slug=aslug)

        #Valid ok
        if post_comment_form.is_valid():
            user_comment = post_comment_form.save(commit=False)
            user_comment.cpost = psingle_post
            user_comment.save()
            return HttpResponseRedirect(reverse("single-post-page", args=[aslug]))
        
        # Error valid
        phtml_context={
            "html_post": psingle_post,
            "html_tags_for_post": psingle_post.tags.all(),
            "html_comment_form": post_comment_form,
            "html_comments":psingle_post.aacomments.all().order_by("-id"),
        }
        return render(request, "blog/post-detail.html", phtml_context)

    
#------------------------------------------------------only GET method
# class SinglePostView(DetailView):
#     template_name = "blog/post-detail.html"
#     model = Post
#     context_object_name = "html_post"

#     def get_context_data(self, **kwargs):
#         default_context = super().get_context_data(**kwargs)
#         default_context["html_tags_for_post"] = self.object.tags.all()
#         default_context["html_comment_form"] = CommentForm()
#         return default_context


#------------------------------------------------------------------------def
# def starting_page(request):
#     #Last added post on top (only 3 post from database)
#     latest_posts = Post.objects.all().order_by("-date")[:3]
    
#     return render(request, "blog/index.html", {
#         "html_posts": latest_posts,
#     })

# def posts(request):
#     all_posts = Post.objects.all().order_by("-date")
#     return render(request, "blog/all-posts.html", {
#         "html_all_posts": all_posts,
#     })

# def single_post(request, aslug):
#     #Get single post from db or 404
#     post_detail = get_object_or_404(Post, slug=aslug)
#     # post_detail = Post.objects.get(slug=aslug)

#     #Get tags for single post
#     tags_for_post= post_detail.tags.all()
    
#     return render(request, "blog/post-detail.html",{
#         "html_post":post_detail,
#         "html_tags_for_post":tags_for_post,
#     })

# ######################WITHOUT DATABASE- DATA FROM LIST#############
# my_posts = []

# def get_date(element):
#     # return post.get("date")
#     return element["date"]

# def starting_page(request):
#     # Sort list my_post, key is function (return value for key date)
#     sorted_posts = sorted(my_posts, key=get_date)
#     # Reverse list
#     latest_post = sorted_posts[-3:]
#     return render(request, "blog/index.html", {
#         "html_posts": latest_post,
#     })

# def posts(request):
#     return render(request, "blog/all-posts.html", {
#         "html_all_posts": my_posts,
#     })

# def single_post(request, slug):
#     # List comprehension and next()
#     # post_detail = next(post for post in my_posts if post["slug"]==slug)
#     #Standard for loop
#     for post in my_posts:
#         if post["slug"] == slug:
#             post_detail = post
#     return render(request, "blog/post-detail.html",{
#         "html_post":post_detail,
#     })