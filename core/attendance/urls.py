from django.urls import path
from . import views
from .views import *

urlpatterns=[
    # path('main/', views.main,name='main'),
    path('main/', views.attendance_view,name='attendance_view')
]