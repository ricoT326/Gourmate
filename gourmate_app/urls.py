from django.urls import path
from gourmate import views

app_name = 'gourmate'

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('home/', views.home, name = 'home'),
    path('logout/', views.user_logout, name='logout'),
    path('contact us', views.contact_us, name='contact us'),
    path('categories', views.categories, name = 'categories')
]

