import json
from pathlib import Path

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect, render


BASE_DIR = Path(__file__).resolve().parent.parent
ARCHIVO_JSON = BASE_DIR / "productos.json"


def cargar_productos():
    """Lee los productos desde el archivo JSON."""
    with open(ARCHIVO_JSON, "r", encoding="utf-8") as archivo:
        return json.load(archivo)


def guardar_productos(productos):
    """Guarda los productos en el archivo JSON."""
    with open(ARCHIVO_JSON, "w", encoding="utf-8") as archivo:
        json.dump(productos, archivo, ensure_ascii=False, indent=2)


def inicio(request):
    """Vista mínima para comprobar que la aplicación funciona."""
    return HttpResponse("Catálogo funcionando correctamente")


def lista_productos(request):
    """Muestra todos los productos del catálogo."""
    productos = cargar_productos()
    total_productos = len(productos)
    productos_con_stock = sum(1 for producto in productos if producto["stock"] > 0)

    contexto = {
        "productos": productos,
        "total_productos": total_productos,
        "productos_con_stock": productos_con_stock,
    }

    return render(request, "catalogo/lista.html", contexto)


def detalle_producto(request, producto_id):
    """Muestra el detalle de un producto según su índice en la lista."""
    productos = cargar_productos()

    try:
        producto_encontrado = productos[producto_id]
    except (IndexError, TypeError):
        producto_encontrado = None

    if producto_encontrado is None:
        return render(
            request,
            "catalogo/detalle.html",
            {"producto": None, "no_encontrado": True, "producto_id": producto_id},
            status=404,
        )

    return render(
        request,
        "catalogo/detalle.html",
        {"producto": producto_encontrado, "no_encontrado": False, "producto_id": producto_id},
    )


def registro(request):
    """Registra usuarios normales para comprar productos."""
    if request.user.is_authenticated:
        return redirect("lista_productos")

    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "")
        password2 = request.POST.get("password2", "")

        if not username or not password:
            messages.error(request, "Debes completar usuario y contraseña.")
        elif password != password2:
            messages.error(request, "Las contraseñas no coinciden.")
        elif User.objects.filter(username=username).exists():
            messages.error(request, "Ese nombre de usuario ya existe.")
        else:
            usuario = User.objects.create_user(username=username, password=password)
            login(request, usuario)
            messages.success(request, f"Usuario {username} registrado correctamente.")
            return redirect("lista_productos")

    return render(request, "catalogo/registro.html")


def iniciar_sesion(request):
    """Inicia sesión para un usuario registrado."""
    if request.user.is_authenticated:
        return redirect("lista_productos")

    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "")
        usuario = authenticate(request, username=username, password=password)

        if usuario is not None:
            login(request, usuario)
            messages.success(request, f"Bienvenido/a, {usuario.username}.")
            return redirect("lista_productos")

        messages.error(request, "Usuario o contraseña incorrectos.")

    return render(request, "catalogo/login.html")


def cerrar_sesion(request):
    """Cierra la sesión del usuario actual."""
    logout(request)
    messages.info(request, "Sesión cerrada correctamente.")
    return redirect("lista_productos")


@login_required(login_url="iniciar_sesion")
def comprar_producto(request, producto_id):
    """Reduce el stock del producto al comprarlo."""
    productos = cargar_productos()

    try:
        producto = productos[producto_id]
    except (IndexError, TypeError):
        messages.error(request, "Producto no encontrado.")
        return redirect("lista_productos")

    if request.method != "POST":
        return redirect("detalle_producto", producto_id=producto_id)

    cantidad = int(request.POST.get("cantidad", 1) or 1)

    if cantidad < 1:
        messages.error(request, "La cantidad debe ser mayor o igual a 1.")
        return redirect("detalle_producto", producto_id=producto_id)

    if producto["stock"] < cantidad:
        messages.error(request, "No hay suficiente stock para esa compra.")
        return redirect("detalle_producto", producto_id=producto_id)

    producto["stock"] -= cantidad
    guardar_productos(productos)

    compras = request.session.get("compras", [])
    compras.append(
        {
            "usuario": request.user.username,
            "producto": producto["nombre"],
            "cantidad": cantidad,
            "precio_total": producto["precio"] * cantidad,
        }
    )
    request.session["compras"] = compras

    messages.success(
        request,
        f"Compra realizada: {cantidad} unidad(es) de {producto['nombre']}.",
    )
    return redirect("lista_productos")


@user_passes_test(lambda user: user.is_authenticated and user.is_staff, login_url="iniciar_sesion")
def stock_admin(request):
    """Permite al administrador aumentar o reducir el stock de los productos."""
    productos = cargar_productos()

    if request.method == "POST":
        producto_id = int(request.POST.get("producto_id", 0) or 0)
        cantidad = int(request.POST.get("cantidad", 1) or 1)
        accion = request.POST.get("accion", "sumar")

        if cantidad < 1:
            messages.error(request, "La cantidad debe ser mayor o igual a 1.")
        else:
            try:
                producto = productos[producto_id]
            except (IndexError, TypeError):
                messages.error(request, "Producto no encontrado.")
            else:
                if accion == "sumar":
                    producto["stock"] += cantidad
                    mensaje = f"Se aumentó el stock de {producto['nombre']} en {cantidad} unidades."
                else:
                    producto["stock"] = max(0, producto["stock"] - cantidad)
                    mensaje = f"Se redujo el stock de {producto['nombre']} en {cantidad} unidades."
                guardar_productos(productos)
                messages.success(request, mensaje)

    return render(request, "catalogo/admin_stock.html", {"productos": productos})
