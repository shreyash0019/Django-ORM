from django.urls import path
from .views import orm_query

urlpatterns = [
    path('orm/', orm_query),
]
