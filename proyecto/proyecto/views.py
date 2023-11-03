from django.http import HttpResponse, JsonResponse
import time

from django.shortcuts import render


def test_view(request):
    # Simulamos un retraso de un segundo
    time.sleep(1)

    # Luego, devolvemos una respuesta en forma de JSON
    response_json = {
        "message": "¡Hola desde Django!",
        "status": "OK"
    }
    return JsonResponse(response_json)

def index(request):
    return render(request, 'index.html')