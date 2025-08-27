from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm

def home_page(request):
    return render(request=request, template_name="index.html")

def contact_page(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Murojatingiz muvaffaqiyatli yuborildi  🎉")
            return redirect('home-page')
    return render(request=request,template_name='contact.html')

def about_page(request):
    return render(request=request,template_name='about.html')


def blog_detail_page(request):
    return render(request=request,template_name='single-blog.html')