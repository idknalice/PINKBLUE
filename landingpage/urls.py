from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sucesso/', views.sucesso, name='sucesso'),
    path('respostas/', views.respostas, name='respostas'),  # Página de respostas
    path('acesso_negado/', views.acesso_negado, name='acesso_negado'),  # Página de acesso negado
]