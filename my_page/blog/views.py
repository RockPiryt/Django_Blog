# from datetime import date
from django.shortcuts import render, get_object_or_404
from .models import Post



# Create your views here.

def starting_page(request):
    #Last added post on top (only 3 post from database)
    latest_posts = Post.objects.all().order_by("-date")[:3]
    
    return render(request, "blog/index.html", {
        "html_posts": latest_posts,
    })

def posts(request):
    all_posts = Post.objects.all().order_by("-date")
    return render(request, "blog/all-posts.html", {
        "html_all_posts": all_posts,
    })

def single_post(request, aslug):
    #Get single post from db or 404
    post_detail = get_object_or_404(Post, slug=aslug)
    # post_detail = Post.objects.get(slug=aslug)

    #Get tags for single post
    tags_for_post= post_detail.tags.all()
    
    return render(request, "blog/post-detail.html",{
        "html_post":post_detail,
        "html_tags_for_post":tags_for_post,
    })

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