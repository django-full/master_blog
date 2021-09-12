from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('blog/<int:blogger>/', views.blog , name = 'blog'),
    path('category/<str:detail>/', views.category , name = 'categoris'),
]

