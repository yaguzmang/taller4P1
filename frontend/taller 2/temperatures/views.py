from django.shortcuts import render, HttpResponse
import requests
# Create your views here.
def temperatures(request):
    if 'valor' in request.GET:
        valor = request.GET['valor']
        codigos = request.GET['codigos']
        fecha = request.GET['fecha']
        origen = request.GET['origen']
        observacion = request.GET['observacion']

        # Verifica si el value no esta vacio
        if valor:
            # Crea el json para realizar la petición POST al Web Service
            args = {'fecha': fecha, 'origen': origen, 'valor': valor, 'codigos': codigos, 'observacion': observacion}
            print(args)
            response = requests.post('http://127.0.0.1:8000/temperatures/', args)
            # Convierte la respuesta en JSON
            temperature_json  = response.json()

    # Realiza una petición GET al Web Services
    response = requests.get('http://127.0.0.1:8000/temperatures/')
    # Convierte la respuesta en JSON
    temperatures = response.json()
    # Rederiza la respuesta en el template measure
    return render(request, "temperatures/temperatures.html", {'temperatures': temperatures})