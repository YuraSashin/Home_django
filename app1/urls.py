from django.urls import path
from .views import index, index_home, about

urlpatterns = [
    path('', index, name='index'),
    path('index_home/', index_home, name='index_home'),
    path('about/', about, name='about'),
]