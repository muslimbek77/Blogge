from django.db import models
from ckeditor.fields import RichTextField

class Contact(models.Model):
    name = models.CharField(max_length= 255)
    email = models.EmailField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.email}"

class Category(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
    author = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now=True)
    main_photo = models.ImageField(upload_to="BlogPhotos/")
    content = RichTextField()
    view_count = models.IntegerField(default=0) #ko'rishlar soni

    def __str__(self) -> str:
        return self.title

