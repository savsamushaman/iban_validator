# myapp/urls.py
from django.urls import path
from ui.views import my_page

urlpatterns = [
    path('', my_page, name='my_page'),
]