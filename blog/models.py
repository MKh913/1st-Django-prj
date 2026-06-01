from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class category(models.Model):
    name=models.CharField(max_length=13)

    def __str__(self):
        return self.name

class post(models.Model):
    title=models.CharField(max_length=50)
    content=models.TextField()
    author=models.ForeignKey(User, on_delete=models.CASCADE, default=1) #MKh913
    counted_views=models.IntegerField(default=0)
    status=models.BooleanField(default=False) #Drafted OR Published

    image=models.ImageField(upload_to="blog/", default="default.png")
    category=models.ManyToManyField(category)
    #tag=models.CharField(max_length=25)
    
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)
    published_date=models.DateTimeField(null=True)

    class Meta:
        ordering=["created_date", "author"]
    
    def __str__(self):
        return f"{self.id}; {self.title}"
