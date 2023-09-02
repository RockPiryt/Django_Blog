from datetime import date
from django.shortcuts import render

my_posts = [
    {
        "slug": "sleeping-cat",
        "image": "cat3.jpg",
        "author": "Paulina",
        "date": date(2023, 9, 1),
        "title": "Cats behaviors",
        "excerpt":"Cats love to eat raw meat.",
        "content": """Cats love sleep, neque dolor morbi, id semper parturient mauris rutrum integer, urna quam. Purus in praesent nec scelerisque odio, a eu nisl, fermentum odio et amet, bibendum dolor aliquam molestie vitae. Malesuada at nisl dui nulla. Sed morbi, sapien fringilla, accumsan velit dolor neque, vel ut ut voluptatibus, pellentesque dui. Suscipit integer, mi sodales in, non ac augue ridiculus velit ac malesuada, sit quam facilisi odio ac et. 

        Lorem ipsum dolor sit amet, neque dolor morbi, id semper parturient mauris rutrum integer, urna quam. Purus in praesent nec scelerisque odio, a eu nisl, fermentum odio et amet, bibendum dolor aliquam molestie vitae. Malesuada at nisl dui nulla. Sed morbi, sapien fringilla, accumsan velit dolor neque, vel ut ut voluptatibus, pellentesque dui. Suscipit integer, mi sodales in, non ac augue ridiculus velit ac malesuada, sit quam facilisi odio ac et. 
        
        Lorem ipsum dolor sit amet, neque dolor morbi, id semper parturient mauris rutrum integer, urna quam. Purus in praesent nec scelerisque odio, a eu nisl, fermentum odio et amet, bibendum dolor aliquam molestie vitae. Malesuada at nisl dui nulla. Sed morbi, sapien fringilla, accumsan velit dolor neque, vel ut ut voluptatibus, pellentesque dui. Suscipit integer, mi sodales in, non ac augue ridiculus velit ac malesuada, sit quam facilisi odio ac et. """

    },
    {
        "slug": "cat-are-funny",
        "image": "cat4.jpg",
        "author": "Paulina",
        "date": date(2022, 7, 21),
        "title": "Funny cats",
        "excerpt": "Tellus amet sed, malesuada velit ut penatibus eget elit sit, vestibulum est id. .",
        "content": """
          Cats are funny adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    },
    {
        "slug": "programming-is-fun",
        "image": "coding.jpg",
        "author": "Paulina",
        "date": date(2021, 3, 10),
        "title": "Programming Is Great!",
        "excerpt": "Did you ever spend hours searching that one error in your code? Yep - that's what happened to me yesterday...",
        "content": """
          I love programming consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    },
]

def get_date(element):
    # return post.get("date")
    return element["date"]

# Create your views here.

def starting_page(request):
    # Sort list my_post, key is function (return value for key date)
    sorted_posts = sorted(my_posts, key=get_date)
    # Reverse list
    latest_post = sorted_posts[-3:]
    return render(request, "blog/index.html", {
        "html_posts": latest_post,
    })

def posts(request):
    return render(request, "blog/all-posts.html", {
        "html_all_posts": my_posts,
    })

def single_post(request, slug):
    # List comprehension and next()
    # post_detail = next(post for post in my_posts if post["slug"]==slug)
    #Standard for loop
    for post in my_posts:
        if post["slug"] == slug:
            post_detail = post
    return render(request, "blog/post-detail.html",{
        "html_post":post_detail,
    })