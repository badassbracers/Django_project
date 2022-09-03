from django.urls import path
from . import views

urlpatterns = [
    path('1', views.proverka_shablona1),
    path('2', views.proverka_shablona2, name='shop/2')
]