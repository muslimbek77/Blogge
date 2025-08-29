from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm
from django.views.generic import DetailView, ListView
from .models import Blog

# def home_page(request):
#     articles = Blog.objects.all()
#     context = {'articles':articles}
#     return render(request=request, template_name="index.html",context=context)

class HomePageView(ListView):
    model = Blog
    context_object_name = 'articles'
    template_name = 'index.html'
    paginate_by = 7


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


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'single-blog.html'
    context_object_name = 'blog'