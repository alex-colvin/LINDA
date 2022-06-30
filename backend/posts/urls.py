from django.urls import path, include
from posts import views

urlpatterns = [
    path('', views.user_posts),
    path('all/', views.get_all_posts),
    path('link/<int:pk>/', views.send_to_linkedin),

]
