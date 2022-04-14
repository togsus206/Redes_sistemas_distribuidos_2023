# Laboratorio 1: Aplicación  Cliente #

Cátedra de Redes y Sistemas Distribuidos.

### Tarea Estrella


Qué mecanismos permiten funcionar a nombres de dominio como:

● http://中文.tw/

● https://💩.la2

#### Respuesta

Un nombre de dominio internacionalizado es un nombre de dominio que contiene caracteres que no son ascii. Por ejemplo los acentos, o caracteres de escritura no latinos, como el arabe o chino no son ascii.

Sin embargo el estándar para nombres de dominio no permite caracteres no ascii. Los nombres de dominio con caracteres no ascii no pueden ser manejados por la estructura existente de resolución de nombres de dominio.

Por lo tanto, para permitir nombres de dominio internacionalizados,  había que cambiar toda la estructura existente de resolución de nombres de dominio o encontrar una manera de convertir los nombres de dominio internacionalizados en nombres de dominio ascii y seguir usando toda la estructura existente..  

La forma que se adoptó para mantener la compatibilidad con toda la estructura de internet existente fue codificar los nombres de dominio unicode, esto es con caracteres no ascii, en nombres de dominio que solo tienen caracteres ascii. La codificación que se usa para convertir caracteres unicode a ascii es punycode y los RFC relacionados con los nombres de dominio internacionalizados son RFC 3454 (Stringprep), RFC 3490 (IDNA), RFC 3491 (Nameprep), RFC 3492 (Punycode).

De esta forma los navegadores, o los servidores de correo, o cualquier otra aplicación de usuario, que tenga que manejar nombres de dominio internalizados primero convierte los nombres de dominio en nombres de dominio equivalentes que solo contienen cadena ascii y luego  resuelven el nombre de dominio. 

Del mismo modo los registradores de nombre de dominio pueden registrar nombres de dominio internacionalizados pero los servidores dns usan la conversión en ascii para resolver los nombres de dominio.

Como ejemplo la cadena unicode 中文.tw se codifica con punycode en la cadena aschii xn--fiq228c.tw y la cadena unicode 💩.la en la cadena ascii xn--ls8h.la. 

Uno puede ingresar en la barra de direcciones del navegador la cadena unicode 中文.tw y el navegador hace la transformación y luego resuelve el nombre de dominio. O uno puede ingresar directamente la codificacion en ascii xn--fiq228c.tw  le la cadena unicode 中文.tw y el navegador resuelven el mismo nombre de dominio y muestra la misma página. 

Del mismo modo uno podría registrar el nombre de dominio 中文.tw  o podría registrar el nombre de dominio equivalente xn--fiq228c.tw 


–

### Comentarios con detalles del codigo agregado:

#### clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

Se crea el socket de cliente.
El primer parámetro indica que la red subyacente está utilizando IPv4 y
el segundo parámetro indica que el socket es de tipo SOCK_STREAM,
lo que significa que se trata de un socket TCP.


#### ip_address = socket.gethostbyname(server_name)

Se resuelve el nombre de dominio encontrándose
la dirección ip correspondiente al nombre de dominio.

#### clientSocket.connect((ip_address, serverPort))

Se inicia la conexión TCP entre el cliente y el servidor.
El parámetro del método connect() es una tupla (dirección ip, puerto) y
es la dirección del lado del servidor de la conexión.

Después de ejecutarse esta línea, se lleva a cabo el proceso de acuerdo en tres fases y se establece una conexión TCP entre el cliente y el servidor.

#### return clientSocket

La funcion connect_to_server(server_name) recibe como parámetro  un nombre de dominio y devuelve un objeto socket.
