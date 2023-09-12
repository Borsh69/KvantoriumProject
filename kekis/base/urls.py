from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name="home"),
    path('projects/', views.projects, name="projects"),
    path('project/<str:pk>/', views.project, name="project"),
    path('account/<str:pk>/', views.account, name="account_home"),
    path('login/', views.login, name="login"),
    path('shop/', views.shop, name="shop"),
    path('buy/<str:pk>/', views.buy, name="buy"),
    path("rating/", views.rating, name="rating"),
    path("competitions/", views.competitions, name="competitions"),
    path("liked/", views.liked, name="liked"),
    path("unliked/", views.unliked, name="unliked"),


]