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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        most_view = Blog.objects.order_by('-view_count')[:4]
        context['blogs'] = most_view

        return context


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        article = self.get_object()
        article.view_count += 1 # ko'rishlar soniga 1 qo'shildi
        article.save() #blogni saqladik
        

        # Oldingi maqola (created_date bo‘yicha)
        prev_article = (
            Blog.objects
            .filter(created_date__lt=article.created_date)
            .order_by('-created_date')
            .first()
        )

        # Keyingi maqola (created_date bo‘yicha)
        next_article = (
            Blog.objects
            .filter(created_date__gt=article.created_date)
            .order_by('created_date')
            .first()
        )

        context['prev_article'] = prev_article
        context['next_article'] = next_article
        return context