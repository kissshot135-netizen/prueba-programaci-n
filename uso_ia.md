Documento de uso de IA


--- 

Parte 1: Registro de consultas


Prompt realizado a la IA:

> al realizar los codigos y luego implementar el html y el json constantemente ocurrian errores de escritura, le pedia la ia que arreglara mis errores, a la hora de modificar los codigos



--- Resumen de la respuesta:---

La IA proporcionó una explicación sobre cómo implementar la funcionalidad solicitada y entregó un ejemplo de código.

--- Uso o modificaciones realizadas antes de integrar la respuesta: ---

Se revisó el código proporcionado, se adaptaron los nombres de variables y funciones al proyecto y se realizaron modificaciones para ajustarlo a la estructura existente.

---

parte 2: bugs 

Prompt realizado a la IA:

> el css no funcionaba, y el formato de las imagenes no coincidian, le pedi a la ia que modifique el codigo, para que funcione y sea mas atractivo visualmente

---Resumen de la respuesta: ---

La IA explicó cómo solucionar el problema y proporcionó una posible implementación.

---Uso o modificaciones realizadas antes de integrar la respuesta: ---

Se utilizó la idea propuesta como referencia y se modificó el código para adaptarlo a los requerimientos del proyecto.

---

Parte 3: optimisacion de catalogo

Prompt realizado a la IA:

> habia que recrear una catalo de 40 productos con sus respectivas imagenes, se le pidio a la ia que generara los 40 productos que fueron  utilizados en el proyecto

--- Resumen de la respuesta: ---

La IA entregó recomendaciones y ejemplos relacionados con la implementación.

--- Uso o modificaciones realizadas antes de integrar la respuesta: ---

La respuesta fue revisada y modificada antes de incorporarla al proyecto.

---

Parte 4: Sistema de usuarios, compras y control de stock

Prompt realizado a la IA:

> crea un sistema donde pueda registrarme como usuario para comprar productos y que al comprar se reduzca el stock; ademas crea un usuario admin con una contraseña sencilla para poder aumentar o disminuir stock del catalogo

--- Resumen de la respuesta: ---

La IA explicó cómo implementar autenticación con Django, registro de usuarios, inicio de sesión y una vista de administración para modificar el stock. Además, propuso una estructura para que cada compra reduzca la cantidad disponible del producto y para que el usuario administrador pueda controlar el inventario.

--- Uso o modificaciones realizadas antes de integrar la respuesta: ---

Se adaptó el flujo a la estructura actual del proyecto. Se agregaron rutas para registro, login, cierre de sesión y compras en `catalogo/urls.py`. En `catalogo/views.py` se implementaron las funciones de registro, autenticación, compra y administración de stock. Se crearon plantillas HTML para login, registro y panel de administración, y se actualizó el CSS para dar estilo al sistema.

--- Funcionalidades agregadas: ---

- Registro de usuarios normales para acceder al catálogo.
- Inicio de sesión con usuario y contraseña.
- Compra de productos desde la vista de detalle.
- Reducción automática del stock al confirmar una compra.
- Validación de disponibilidad de stock antes de vender.
- Usuario administrador con credenciales:
  - usuario: `admin`
  - contraseña: `admin123`
- Panel de administración para aumentar o disminuir el stock de cualquier producto.
- Mensajes de error y éxito para mejorar la experiencia del usuario.

--- Archivos principales modificados: ---

- `catalogo/views.py`
- `catalogo/urls.py`
- `catalogo/templates/catalogo/base.html`
- `catalogo/templates/catalogo/lista.html`
- `catalogo/templates/catalogo/detalle.html`
- `catalogo/templates/catalogo/registro.html`
- `catalogo/templates/catalogo/login.html`
- `catalogo/templates/catalogo/admin_stock.html`
- `catalogo/static/catalogo/css/estilos.css`
- `catalogo/management/commands/create_admin.py`



