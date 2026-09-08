from django.urls import path

from . import views


urlpatterns = [
    path("", views.lista_productos, name="lista_productos"),
    path("registro/", views.registro, name="registro"),
    path("login/", views.iniciar_sesion, name="iniciar_sesion"),
    path("logout/", views.cerrar_sesion, name="cerrar_sesion"),
    path(
        "producto/<int:producto_id>/",
        views.detalle_producto,
        name="detalle_producto"
    ),
    path(
        "comprar/<int:producto_id>/",
        views.comprar_producto,
        name="comprar_producto"
    ),
    path("admin-stock/", views.stock_admin, name="stock_admin"),
]
