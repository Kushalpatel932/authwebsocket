from django.urls import path
from authw2.views import google_login

urlpatterns = [
    path('auth/login/', google_login, name='google_login'),
]
