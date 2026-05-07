from django.urls import path
from . import views

app_name = 'leituras'

urlpatterns = [
    path('historico/', views.historico, name='historico'),
    path('grafico/', views.grafico, name='grafico'),
    path('receber/', views.receber_leitura, name='receber_leitura'),  # endpoint para o sensor
]
