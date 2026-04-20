from app.views import HelloWorldView
from django.urls import path


urlpatterns = [
    path('hello/', HelloWorldView.as_view(), name='hello_world'),
]