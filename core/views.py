from django.shortcuts import render


def home(request):
    contexto = {
        'temperatura': '--',
        'umidade': '--',
        'ultima_atualizacao': 'Aguardando leitura do sensor...',
        'status_sensor': 'offline',  # 'online' quando o sensor estiver enviando dados
    }
    return render(request, 'core/home.html', contexto)


def sobre(request):
    """
    Página com informações sobre o sistema SensorView.
    """
    return render(request, 'core/sobre.html')
