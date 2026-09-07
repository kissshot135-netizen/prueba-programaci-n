import json
from pathlib import Path

from django.http import HttpResponse
from django.shortcuts import render


# Ubicación del archivo productos.json
BASE_DIR = Path(__file__).resolve().parent.parent
ARCHIVO_JSON = BASE_DIR / "productos.json"  # esta es la ruta correcta de tu carpeta de datos


def cargar_productos():
    "Lee los productos desde el archivo JSON."
    with open(ARCHIVO_JSON, "r", encoding="utf-8") as archivo:
        return json.load(archivo)


def inicio(request):
    "Vista mínima para comprobar que la aplicación funciona."
    return HttpResponse("Catálogo funcionando correctamente")


def lista_productos(request):
    "Muestra todos los productos del catálogo."

    productos = cargar_productos()

    total_productos = len(productos)

    productos_con_stock = sum(
        1 for producto in productos
        if producto["stock"] > 0
    )

    contexto = {
        "productos": productos,
        "total_productos": total_productos,
        "productos_con_stock": productos_con_stock,
    }

    return render(
        request,
        "catalogo/lista.html",
        contexto
    )


def detalle_producto(request, producto_id):
    "Muestra el detalle de un producto según su índice en la lista."

    productos = cargar_productos()

    # obtenemos el producto usando el índice numérico de la URL
    try:
        producto_encontrado = productos[producto_id]
    except (IndexError, TypeError):
        producto_encontrado = None

    if producto_encontrado is None:
        return render(
            request,
            "catalogo/detalle.html",
            {
                "producto": None,
                "no_encontrado": True,
            },
            status=404
        )

    return render(
        request,
        "catalogo/detalle.html",
        {
            "producto": producto_encontrado,
            "no_encontrado": False,
        }
    )
