from django.shortcuts import render


def home_page(request):
    return render(request=request, template_name="index.html")

def contact_page(request):
    return render(request=request,template_name='contact.html')

def about_page(request):
    return render(request=request,template_name='about.html')