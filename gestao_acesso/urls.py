from django.urls import path, include

from gestao_acesso.views import diversos, sistemas

app_name = 'gestao_acesso'

sistemas_patterns = [
    path('', sistemas.SistemaListView.as_view(), name='index'),
    path('create/', sistemas.SistemaCreateView.as_view(), name='create'),
    path('update/<int:pk>/', sistemas.SistemaUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', sistemas.SistemaDeleteView.as_view(), name='delete')
]

urlpatterns = [
    path('', diversos.AboutView.as_view(), name='about'),
    path('sistemas/', include((sistemas_patterns, 'sistemas'))),
]