from django.urls import path
from portfolio import views

urlpatterns = [
  path('', views.PostView.as_view(), name = 'home')
]