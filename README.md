## 👋 ¡Bienvenidos usuarios a mi proyecto! carrito de compras

<img src="imagen_presentacion.png" alt="Presentación" width="205" align="left" style="margin-right:20px; border-radius:5px;">  
<p style="text-align: justify;">

Este proyecto consiste en la simulación de un carrito de compras desarrollado en Python. El sistema permite almacenar productos y sus precios utilizando un diccionario como estructura principal de datos.

El usuario puede agregar productos al carrito, eliminarlos si lo desea y visualizar el contenido completo junto con el total a pagar. El programa funciona mediante un menú interactivo en consola, lo que permite una experiencia dinámica y continua hasta que el usuario decida salir.

Cada producto se guarda como clave dentro del diccionario, mientras que su precio se almacena como valor. Esta estructura permite acceder rápidamente a los datos, modificarlos y realizar cálculos de manera eficiente.

#
### 🧑‍💻 Lenguaje de programacion
- Python

#
### 🎯 Objetivos del proyecto
- Implementar diccionarios para almacenar información.
- Aplicar funciones para modularizar el programa.
- Utilizar bucles para crear un menú interactivo.
- Validar datos ingresados por el usuario.
- Calcular el total de compra mediante operaciones matemáticas.
- Simular el funcionamiento básico de un carrito digital.

#
### 🧠 Temas que se a aplicado
- Diccionarios
- Funciones
- Condicionales (`if`, `elif`, `else`)
- Bucles `while`
- Bucles `for`
- Manejo de excepciones (`try` / `except`)
- Operaciones matemáticas
- Validación de datos

#
### ⚙️ Funcionamiento
1. Se crea un diccionario llamado `carrito` donde:
   - La clave representa el nombre del producto.
   - El valor representa el precio del producto.

2. El sistema muestra un menú con las siguientes opciones:
   - Agregar producto.
   - Eliminar producto.
   - Mostrar carrito.
   - Salir.

3. Cuando se agregan productos:
   - Se valida que el precio sea numérico y mayor que cero.
   - El producto se almacena en el diccionario.

4. Al mostrar el carrito:
   - Se recorren los productos usando un bucle `for`.
   - Se calcula el total acumulado.
   - Se muestra el resumen completo en pantalla.

5. El programa se ejecuta de manera continua hasta que el usuario seleccione la opción de salir.

#
### ▶️ Cómo usar el proyecto
Tienes dos opciones para obtener el código:
1. **Descargar directamente:**
   Haz clic en el botón verde code y selecciona download zip.

2. **Clonar con git:**
   ```bash
   git clone https://github.com/tu-usuario/tu-repositorio.git
   ```