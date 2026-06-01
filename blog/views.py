from django.shortcuts import render, get_object_or_404
import blog.models as models

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.core import paginator

# Create your views here.
from templates import*

def home(request, **kwargs):
    if kwargs.get("cat_name")!=None: #categories func
        posts=models.post.owbjects.filter(status=1, category__name=kwargs["cat_name"])
    
    if kwargs.get("auth_username")!=None: #authors func
        posts=models.objects.filter(status=1, author__username=kwargs["auth_username"])

    else: #main
        posts=models.post.objects.filter(status=1)
    
    posts=Paginator(posts, 3)
    
    try:
        page_num=request.GET.get("page")
        posts=posts.get_page(page_num)
    
    except PageNotAnInteger: 
        posts=posts.get_page(1)
    
    except EmptyPage:
        posts=paginator.page(paginator.num_pages)

    context={"posts": posts}
    return render(request, "blog/home.html", context)

def single(request, id):
    post=get_object_or_404(models.post, pk=id, status=1)
    context={"post": post}

    return render(request, "blog/single.html", context)

''' (This view has expanded to home func)
def category(request, name):
    posts=models.post.objects.filter(status=1, category__name=name)
    context={"posts": posts}

    return render(request, "blog/home.html", context)
''' 

''' (This view has expanded to home func)
def author(request, username):
    posts=models.objects.filter(status=1, author__username=username)
    context={"posts": posts}

    return render(request, "blog/home.html", context)
'''

def search(request):
    posts=models.post.objects.filter(status=1)
    if request.method=="GET":
        if s:=request.GET.get('s'):
            posts=posts.filter(content__contains=s)

    context={"posts": posts}
    return render(request, "blog/home.html", context)
