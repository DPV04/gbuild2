from django.urls import path
from . import views
from .views import *
from django.contrib import admin
from django.urls import path
from .views import*
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns=[
    path('students/',students,name="students"),
    # path('books/', views.book_list, name='book_list'),
    # path('up/', views.upload_book, name='upload_book'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

    urlpatterns +=staticfiles_urlpatterns()