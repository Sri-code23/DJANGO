from django.db import models
from django.utils.text import slugify

# Create your models here. 

class category_table(models.Model):
    c_name=models.CharField( max_length=50)

    def __str__(self):
        return self.c_name

class User_database(models.Model):
    #id=models.CharField(max_length=999,unique=True)
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    #content=models.TextField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    img_url=models.URLField(max_length=100,null=True)
    #Adding Slug column in the table
    slug=models.SlugField(unique=True)
    #adding category tabel as a foreign key
    category_id=models.ForeignKey(category_table, on_delete=models.CASCADE, null=True)


    def save(self,*args,**kwargs):
        self.slug = slugify(self.username)
        super().save(*args,**kwargs)


    def __str__(self):
        return self.username

