from django.db import models

# Create your models here.
class post(models.Model):
    title=models.CharField(max_length=50)
    content=models.TextField()
    #author=models.CharField(max_length=25)
    counted_views=models.IntegerField(default=0)
    status=models.BooleanField(default=False) #Drafted OR Published

    #image=models.CharField(max_length=100)
    #category=models.CharField(max_length=25)
    #tag=models.CharField(max_length=25)
    
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)
    published_date=models.DateTimeField(null=True)

    class Meta:
        ordering=["created_date"]#, "author"]
    
    def __str__(self):
        return f"{self.id}; {self.title}"
