from django.db import models
from ckeditor.fields import RichTextField

class Contact(models.Model):
    name = models.CharField(max_length= 255,verbose_name="Ism")
    email = models.EmailField(max_length=255,verbose_name="Email")
    message = models.TextField(verbose_name="Xabar")

    def __str__(self):
        return f"{self.name} - {self.email}"
    class Meta:
        verbose_name = ("Kontakt")
        verbose_name_plural = ("Kontaktlar")



class Category(models.Model):
    name = models.CharField(max_length=255,verbose_name="Kategoriya nomi")
    
    def __str__(self) -> str:
        return self.name
    class Meta:
        verbose_name = ("Kategoriya")
        verbose_name_plural = ("Kategoriyalar")


class Blog(models.Model):
    title = models.CharField(max_length=255,verbose_name="Sarlavha")
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
    author = models.CharField(max_length=255,verbose_name="Avtor")
    created_date = models.DateTimeField(auto_now=True,verbose_name="Yaratilgan sana")
    main_photo = models.ImageField(upload_to="BlogPhotos/",verbose_name="Rasm")
    content = RichTextField(verbose_name="Maqola matni")
    view_count = models.IntegerField(default=0,verbose_name="Ko'rishlar soni") #ko'rishlar soni

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = ("Blog")
        verbose_name_plural = ("Bloglar")

