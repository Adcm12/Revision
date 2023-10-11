    Ejercicio 1: Gestor de tareas

Crea una clase llamada Tarea que tenga los siguientes atributos:

nombre: El nombre de la tarea.
descripcion: Una descripción de la tarea.
fecha_inicio: La fecha de inicio de la tarea.
fecha_fin: La fecha de finalización de la tarea.

Crea un método crear_tarea() que cree una nueva instancia de la clase Tarea.

Crea un método listar_tareas() que liste todas las tareas creadas.

Crea un método completar_tarea() que marque una tarea como completada.

    Ejercicio 2: Gestor de usuarios

Crea una clase llamada Usuario que tenga los siguientes atributos:

nombre: El nombre del usuario.
apellidos: Los apellidos del usuario.
correo_electronico: El correo electrónico del usuario.
contrasena: La contraseña del usuario.
Crea un método crear_usuario() que cree una nueva instancia de la clase Usuario.

Crea un método autenticar_usuario() que autentique un usuario con su correo electrónico y contraseña.

    Ejercicio 3: Gestor de ventas

Crea una clase llamada Venta que tenga los siguientes atributos:

producto: El producto vendido.
precio: El precio del producto.
cantidad: La cantidad de productos vendidos.
Crea un método crear_venta() que cree una nueva instancia de la clase Venta.

Crea un método listar_ventas() que liste todas las ventas realizadas.

Crea un método obtener_ventas_por_producto() que liste todas las ventas realizadas por un producto.

Ejercicio 4: Conexión a una base de datos

Crea una clase llamada BaseDeDatos que se conecte a una base de datos MySQL.

La clase debe tener los siguientes métodos:

conectar(): Conecta a la base de datos.
desconectar(): Desconecta de la base de datos.
insertar_registro(): Inserta un registro en la base de datos.
actualizar_registro(): Actualiza un registro en la base de datos.
eliminar_registro(): Elimina un registro de la base de datos.
listar_registros(): Lista todos los registros de la base de datos.
Para conectar a la base de datos, la clase debe usar la siguiente información:

El nombre del host.
El nombre de la base de datos.
El nombre de usuario.
La contraseña.