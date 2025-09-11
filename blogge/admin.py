from django.contrib import admin
from .models import Contact,Blog,Category
from django.utils.html import format_html
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ["img","title","category"]
    readonly_fields = ["view_count","created_date"]
    list_filter=["category"]
    search_fields = ["title"]
    
    def img(self, obj):
         return format_html('<img width="100" src="{}" />'.format(obj.main_photo.url))


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
     list_display = ["name","email"]
admin.site.register(Category)
