
from django.urls import path
from .views import TopUsersView
urlpatterns = [
   path('top-users/<str:date>/', TopUsersView.as_view(), name='top-users'),
]
