from django import template
from blog.models import post
register=template.Library()

@register.inclusion_tag("blog/last_posts.html")
def last_posts(cnt=4):
    posts=post.objects.filter(status=1).order_by("published_date")[:cnt]
    return {"posts": posts}

from blog.models import category
@register.inclusion_tag("blog/posts_categories.html")
def categories(cnt=4):
    posts=post.objects.filter(status=1)
    categories=category.objects.all()

    dct={}
    for name in categories:
        dct[name]=post.objects.filter(name).count

    return {"categories": dct}