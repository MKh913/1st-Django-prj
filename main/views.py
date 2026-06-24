from django.shortcuts import render
from django.core.paginator import Paginator

# Create your views here.
from blog.models import post
def index(request):
    posts=post.objects.filter(status=1).order_by("-published_date")[:6]
    posts=Paginator(posts, 3)

    page_number=request.GET.get("page")
    posts=posts.get_page(page_number)

    context={"posts": posts}
    return render(request, "main/index.html", context)

def contact(request):
    return render(request, "main/contact.html")

def about(request):
    return render(request, "main/about.html")

def elements(request):
    return render(request, "main/elements.html")