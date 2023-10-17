from django.urls import path
from .views import slide


urlpatterns = [
    path('', slide, name='slide')
]