from django.urls import path
from . import views
from .views import *

urlpatterns=[
    path('upload/', views.upload, name='upload'),
    path('books/', views.book_list, name='book_list'),
    path('up/', views.upload_book, name='upload_book'),
]