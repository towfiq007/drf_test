from .views import TestJwtClass
from django.urls import path

urlpatterns = [
    path("", TestJwtClass.as_view(),name='test_jwt'),
]
