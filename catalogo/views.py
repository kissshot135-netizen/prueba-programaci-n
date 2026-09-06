from django.shortcuts import render

# Create your views here.
import json

from pathlib import Path

from django.conf import settings
from django.shortcuts import render


def inicio(request):
    ruta = Path(settings.BASE_DIR) / "datos" / "productos.json"

    with open(ruta, "r", encoding="utf-8") as archivo:
        productos = json.load(archivo)

    return render(request, "catalogo/inicio.html", {
        "productos": productos
    })