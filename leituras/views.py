from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


def historico(request):
    """
    Exibe o histórico de leituras do sensor em uma tabela.
    No futuro: buscar do banco de dados todas as leituras do dia.
    """
    # Dados fictícios para estrutura inicial
    leituras_exemplo = [
        {'temperatura': 28.5, 'umidade': 65.0, 'data_hora': '06/05/2025 08:00'},
        {'temperatura': 29.1, 'umidade': 63.5, 'data_hora': '06/05/2025 09:00'},
        {'temperatura': 30.2, 'umidade': 61.0, 'data_hora': '06/05/2025 10:00'},
        {'temperatura': 31.0, 'umidade': 58.5, 'data_hora': '06/05/2025 11:00'},
        {'temperatura': 31.8, 'umidade': 56.0, 'data_hora': '06/05/2025 12:00'},
    ]
    contexto = {
        'leituras': leituras_exemplo,
        'total': len(leituras_exemplo),
    }
    return render(request, 'leituras/historico.html', contexto)


def grafico(request):
    """
    Exibe o gráfico de variação de temperatura e umidade ao longo do dia.
    Utiliza Chart.js para renderizar o gráfico no frontend.
    """
    return render(request, 'leituras/grafico.html')


@csrf_exempt
def receber_leitura(request):
    """
    Endpoint que recebe os dados do sensor via requisição HTTP POST.
    O sensor (ESP32/Arduino) envia: temperatura e umidade em formato JSON.

    Exemplo de payload:
    {
        "temperatura": 28.5,
        "umidade": 65.0
    }
    """
    if request.method == 'POST':
        try:
            dados = json.loads(request.body)
            temperatura = dados.get('temperatura')
            umidade = dados.get('umidade')

            # Validação básica
            if temperatura is None or umidade is None:
                return JsonResponse({'erro': 'Campos temperatura e umidade são obrigatórios.'}, status=400)

            # No futuro: salvar no banco de dados
            # Leitura.objects.create(temperatura=temperatura, umidade=umidade)

            return JsonResponse({
                'status': 'ok',
                'mensagem': 'Leitura recebida com sucesso!',
                'temperatura': temperatura,
                'umidade': umidade,
            })

        except json.JSONDecodeError:
            return JsonResponse({'erro': 'JSON inválido.'}, status=400)

    return JsonResponse({'erro': 'Método não permitido. Use POST.'}, status=405)
