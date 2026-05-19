from django.shortcuts import render, get_object_or_404
import blog.models as models

# Create your views here.
from templates import*

def home(request):
    posts=models.post.objects.filter(status=1)
    context={"posts":posts}

    return render(request, "blog/home.html", context)

def single(request, id):
    post=get_object_or_404(models.post, pk=id, status=1)
    context={"post":post}

    return render(request, "blog/single.html", context)
