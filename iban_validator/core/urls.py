from django.urls import include, path
from rest_framework import routers
from core import views

router = routers.DefaultRouter()
router.register(r'users', views.User)
router.register(r'ibans', views.IBAN)

urlpatterns = [
   path('', include(router.urls))
]