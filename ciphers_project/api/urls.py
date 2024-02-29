from django.urls import path
from .views import greetings, encode

urlpatterns = [
    path('', greetings),
    path('caesar/<str:plain_text>/<int:shift>', encode)
]