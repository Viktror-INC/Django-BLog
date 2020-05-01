#blog1 url

from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    path('', views.blog1, name = 'home'),
    path('create_post/', views.create_post, name = 'create_post'),
    path('about/', views.about, name = 'about'),
    path('<slug:slug>/', views.blog_det , name = 'blog_det'),
    path('create_post/upload_done/', views.upload_done, name = 'upload_done'),

]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)