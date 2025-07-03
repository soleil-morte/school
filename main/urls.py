from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView

urlpatterns=[
    path('index/',Index),
    path('teachers/',Teachers),
    path('groups/',Groups),
    path('subjects/',Subjects),
]