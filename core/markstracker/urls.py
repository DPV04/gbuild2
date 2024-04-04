from django.urls import path
from . import views
from .views import *

urlpatterns=[
    # path('main/', views.main,name='main'),
    path('', views.index,name='studentdetail'),
    # path('detail/', views.student_detail,name='student_detail')
]