from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView
from gestao_acesso.views import diversos, sistemas

app_name = 'gestao_acesso'

usuarios_patterns = [
    path('login/', LoginView.as_view(template_name='usuarios/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]

sistemas_patterns = [
    path('', sistemas.SistemaListView.as_view(), name='index'),
    path('create/', sistemas.SistemaCreateView.as_view(), name='create'),
    path('update/<int:pk>/', sistemas.SistemaUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', sistemas.SistemaDeleteView.as_view(), name='delete')
]

urlpatterns = [
    path('home/', TemplateView.as_view(template_name='diversos/home.html'), name='home'),
    path('usuarios/', include(usuarios_patterns)),
    path('sistemas/', include((sistemas_patterns, 'sistemas'))),
]