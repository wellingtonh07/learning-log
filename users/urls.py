from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    # Página de login
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),  # Usando a LogoutView do Django
    path('register/', views.register, name='register'),
]
