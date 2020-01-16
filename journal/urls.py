from django.urls import path
from . import views


urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('article/<int:pk>/', views.post_details, name='post_details'),
    path('article/new/', views.post_new, name='post_new'),
    path('article/<int:pk>/edition/', views.post_edition, name='post_edition'),

]