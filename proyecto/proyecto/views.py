from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
import time

from django.shortcuts import render

#Para primer boton Obtener Datos
def test_view(request):
    # Simulamos un retraso de un segundo
    time.sleep(1)

    # Luego, devolvemos una respuesta en forma de JSON
    response_json = {
        "message": "¡Hola desde Django!",
        "status": "OK"
    }
    return JsonResponse(response_json)

"""
    Hacer una vista que devuelva usuarios
    Llamar a esa vista desde el index con JS
    Escribir esos datos en una tabla o varios div...
"""
# La parte crear la tabla sin JS -> si no actualizas la pagina no ves los cambios realizados

    # Creamos nueva función para sacar los datos de usuarios: nombre de usuario, email

def get_usuarios():
    #Importamos antes de eso modelo User de django, no tenemos el modelo creado
    usuarios = User.objects.all() 
    #Creamos la lista para guardar los datos
    usuarios_data = []

    #El bucle para guardar los datos en la lista usuarios_data
    for usuario in usuarios:
        usuario_info = {
            'username': usuario.username,
            'email': usuario.email
        }
        usuarios_data.append(usuario_info)
    return usuarios_data

    # La funcion get_usuarios usamos en nueva funcion mostrar_usuarios
def mostrar_usuarios(request):

    usuarios_data = get_usuarios()

    # Luego, devolvemos una respuesta en forma de JSON

    return JsonResponse(usuarios_data, safe=False)

# Declarar funciones antes de usar en la pagina (por ejemplo: todas func-s se declaran de index)

    # Metemos sin JS debes conectar view con templeate a mano -> poner q va a devolver index

def get_usuario_id():
    

def index(request):
    usuarios_list = get_usuarios()
    dict_ = {
        "usuarios":  usuarios_list
    }
    dict2 = {
        "test": "dato"
    }
    print(dict_)
    return render(request, 'index.html', dict_)

'''
[X] GET all de lista                        -> mostrar_usuarios
    + GET all de lista (JS con fetch)
    - (AJAX) 
    - (jQuery)
[ ] GET de un User por id                   -> mostrar_usuarios/{:id}
[ ] POST crear un usuario nuevo             -> crear_usuario
[ ] PUT o POST para editar por id un user   -> editar_usuario/{:id}
[ ] DELETE borrar user por id               -> borrar_usuario/{:id}

JS con fetch
AJAX / jQuery
'''

"""Ejemplo de codigo de Arturo 
from django.shortcuts import redirect

from A_DB.models import Cliente


def crear_cliente(request):
    datos = request.POST
    try:
        Cliente.objects.create(
            alias = datos.get('alias'),
            email = datos.get('email'),
            telefono1 = datos.get('telefono1'),
            telefono2 = datos.get('telefono2'),
            #estado = datos.get('estado'),
            observaciones = datos.get('observaciones'),
        )
    except Exception as e:
        print(e, 'error')
    return redirect(request.headers['Referer'])
    #return JsonResponse({'status': 'ok'})"""
