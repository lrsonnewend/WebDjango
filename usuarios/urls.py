from django.urls import path
from django.contrib.auth import views as auth_views
from .views import UsuarioCreate
#Import Views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='usuarios/form-check-auth.html'), name='login'),   
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('registrar/usuario', UsuarioCreate.as_view(), name='registrar-usuario'),
    
]