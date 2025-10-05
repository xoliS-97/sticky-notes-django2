from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Homepage view
    path('products/', views.product_list, name='product_list'),  # Product listing
    path('register/', views.register_user, name='register'),  # User registration
    path('login/', views.login_user, name='login'),  # User login
    path('logout/', views.logout_user, name='logout'),  # User logout
]
