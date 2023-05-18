INFORME: 
LABORATORIO 2: HFTP


INTEGRANTES:
    -Agustín Molina
    -Bruno Volpini
    -Matias Valle
=============================

Para elobaror el laboratorio, se crearon los comandos a los cuales el usuario tendra acceso, los cuales estan modularizados dentro del archivo *connection.py*, para asi dejar lo mas legible posible el metodo *handle*.
Estas metodos son:
- get_file_listing()
- get_metadata()
- get_slice()

Los cuales su funcionamiento seran explicados mas adelante.
Para el manejo de errores se definieron diferentes metodos para cada error, caso sea necesario usar algun codigo de error, simplemente se llama al metodo correspondiente. Esto hace, que en caso de tener que cambiar el mensaje o codigo de error, solo haya que hacerlo dentro del metodo llamado.


server.py
---------------------------------
En este modulo creamos el socket del servidor y se configura para conectarlo al puerto 19501 y se mantanga en interaccion con los pedidos de un solo cliente.
Ademas, se encarga de aceptar la conexion, creando asi el socket del cliente, generando la conexion que sera manejada por el metodo handle dentro del modulo *connection.py*.
Estos sockets permiten la interaccion entre cliente y servidor, enviando y respondiendo pedidos respectivamente, hasta la desconexión del cliente.


connection.py
---------------------------------
Este es el modulo principal para manejar la conexion entre cliente y servidor. En este modulo, se definen los diferentes comandos a los cuales tendra acceso el usuario, como tambien metodos que se encargaran de verificar cualquier malescritura por parte del cliente, asi como el manejo de caracteres no permitidos. Esto dice, que ante cualquier pedido que no este dentro del protcolo, se manejara esta entrada invalida para no permitir que se caiga el servidor y la conexion se mantenga estable.
El manejo de pedido y respuestas, es manejado por el metodo *handle*, el cual respondera los pedidos del cliente uno a la vez. Para ello implementamos un campo de entrada *buffer_in*, que es quien se encarga de recibir todos los pedidos, tomar el primero, analizarlo y dar una respuesta, y asi con los siguientes pedidos.
Para verificar que los pedidos fueron hechos de manera correcta, se usa el metodo *analize_request*, quien analiza si el pedido es un comando valido(analizando los argumentos que tiene el comando del pedido), y que en caso de no serlo, responder con el error correspondiente.
Si es correcto, se llama al metodo especificado, y se ejecuta el pedido devolviendo la respuesta al cliente, mediante un buffer de salida llamado *buffer_out*, que es quien almacena la respuesta para el cliente. En caso de que el pedido no sea correcto o este malformado, se responde con un mensaje de error.
Finalmente el metodo *send_to_buff()* se encarga de mandar todas las respuestas al cliente, dejando vacio el buffer de salida.


constant.py
--------------------------------
Definimos las siguientes variables dentro del archivo que nos ayudo
al manejo de estas constantes tan usadas:

space = ' '
new_line = '\n'
SIZE_READ = 1024


### Recepcion de pedidos y envio de respuestas

## Metodos implementados


# get_file_listing
Este metodo es el encargado de listar todos los archivos disponibles en el directorio. Este metodo funciona de manera dinamica, es decir que si se agregan o eliminan archivos del directorio, el servidor modificara la respuesta dependiendo de los archivos que se encuentren disponibles a la hora de hacer el pedido, sin necesidad de cortar la conexion.

# get_metadata
Este metodo toma como argunmento un archivo y devuelve la cantidad de bytes que ocupa el archivo. 
En caso de no existir, se responde al pedido con un mensaje de error.Tambien revisa que el pedido no incluya caracteres no permitidos.


# get_slice
Recibe 3 argumentos, el nombre de un archivo, un OFFSET y un tamaño. Se encarga de leer y mostrar en pantalla los datos de un archivo en particular dependiendo del offset+size ingresado.
En este metodo, se incluyo control de errores para manejar cualquier incoveniente que pueda ocurrir antes un pedido malformado.


# quit
Se encarga de cerrar la conexion con el cliente una vez que este lo pide, pero el servidor sigue estando activo esperando otra conexion de otro cliente.




Deciciones de diseño
-------------------------------
>Se decidio modularizar los manejos de codigo de error en diferentes funciones
>Se utilizo un metodo *analize_request*, que decide si un pedido por parte del cliente esta bien formado y como proceder caso positivo o negativo
>Se declaro un metodo *send_to_buff()* para mostrar la respuesta del pedido al cliente.
> 


## Preguntas

**1) ¿Qué estrategias existen para poder implementar este mismo servidor pero con capacidad de atender múltiples clientes simultáneamente?**
thread es un módulo de python que permite el manejo de hilos, la idea sería destinar un hilo desde el bucle principal para cada cliente conectado. También limitar la cantidad de hilos generados y poner en espera los clientes que no consigan u ser atendidos hasta que un hilo termine con su trabajo.

**2)  ¿Qué diferencia hay si se corre el servidor desde la IP “localhost”, “127.0.0.1” o la ip “0.0.0.0”?**
No existe una diferencia notable.


## Reglas para su uso

**En una terminal ejecutar el servidor:**

python3 server.py

**En otra terminal usar el comando:**

telnet localhost 19501
