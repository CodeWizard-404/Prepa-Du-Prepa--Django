from django.urls import path
from .views import register
from django.contrib.auth.views import LoginView,LogoutView
from .views import ProfileView

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', LoginView.as_view(template_name='authentication/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),

]
