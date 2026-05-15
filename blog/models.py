from django.db import models

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=50)
    content=models.TextField()
    #author=models.CharField(max_length=25)
    counted_views=models.IntegerField(default=0)
    status=models.BooleanField(default=False) #Drafted OR Published

    #image=models.CharField(max_length=100)
    #category=models.CharField(max_length=25)
    #tag=models.CharField(max_length=25)
    
    created_date=models.DateField(auto_now_add=True)
    updated_date=models.DateField(auto_now=True)
    published_date=models.DateField(null=True)
