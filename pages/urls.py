from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('lanu', views.lanu,name='lanu'),
    path('blog', views.blog,name='blog'),
    path('youtube', views.youtube,name='youtube'),
    path('gallery', views.gallery,name='gallery'),
    path('models', views.models,name='models'),
    path('research', views.research,name='research'),
    path('download-pdf/', views.download_pdf, name='download-pdf'),
]