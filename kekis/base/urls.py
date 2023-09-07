from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name="home"),
    path('project/<str:pk>/', views.project, name="project"),
    path('kvantum/', views.kvantum, name="kvantum"),
    path('account/<str:pk>/', views.account, name="account_home"),
    path('login/', views.login, name="login"),
    path('shop/', views.shop, name="shop"),
    path('buy/<str:pk>/', views.buy, name="buy"),
    path("rating/", views.rating, name="rating"),
    path("competitions/", views.competitions, name="competitions"),


]