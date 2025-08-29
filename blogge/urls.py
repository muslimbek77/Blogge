from django.urls import path
from .views import HomePageView,contact_page,about_page,BlogDetailView

urlpatterns = [
    path('', HomePageView.as_view(), name='home-page'),
    path('about/', about_page, name='about-page'),
    path('contact/', contact_page, name='contact-page'),
    path('blog/<int:pk>/',BlogDetailView.as_view(),name='single-blog'),
]