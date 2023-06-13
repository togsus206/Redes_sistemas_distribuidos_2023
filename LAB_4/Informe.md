### CAPA DE RED: ********
## Simulaciòn discreta y análisis sobre el problema y sus soluciones

## Resumen



# INTEGRANTES:
    -Agustín Molina
    -Bruno Volpini
    -Matías Valle
=============================


## INTRODUCCIÒN

En este laboratorio se estudia el comportamiento de una red representada en un modelo de anillo de 8 nodos, unidos con dos posibles vecinos por el modelo full-dúplex. Cada nodo está formado por dos capas de enlace, una de red y una de aplicación.

La capa de enlace y la capa de aplicación tienen generadores de tráfico y bufferes respectivamente.

Un escenario se envía desde 2 nodos con igual distancia al nodo de destino y en otro todos los nodos, exceptuando el destinatario, envían paquetes, resultando así en diferentes distancias al nodo de destino.

## TAREA ANÁLISIS ##

se implementó 4 vectores que permitieron visualizar cuántos paquetes envía cada nodo, tamaño del buffer, delay del paquete y cantidad de saltos que hace un paquete

Buffer: este vector permite ver el tamaño del buffer de cada nodo. En el caso 1 podemos ver que se usan solo buffers del nodo 0 y 2 donde el buffer del nodo 0 es el que más se llena y el de otros nodos donde el paquete viaja, mantienen un tamaño mínimo. En el caso 2 se usan todos los buffers salvo el del nodo 4 que usa un solo buffer. En conclusión no se está aprovechando todo el potencial


Delay: este vector permite saber el delay del paquete hasta llegar a su destino. En el caso 1 podemos apreciar que el delay llega hasta un máximo de 104 esto puede suceder debido a que se envía el paquete por un solo canal en sentido horario por lo tanto en el peor caso, el delay puede ser alto. En el caso 2 el delay es con un máximo de 184, esto pasa ya que en el peor caso(nodo 4) el paquete tiene que atravesar muchos nodos para llegar al destino además del tiempo que tarda en pasar por un nodo que no es el destino y reenviarlo por el otro canal


Jumps: este vector guarda la cantidad de saltos que hizo un paquete hasta llegar a su destino. En el caso 1 tenemos que estos jumps son 3 (nodo 0) y 5 (nodo 2)
en el caso 2 tenemos varios jumps donde el máximo es 7 (nodo 4 enviando a nodo 5) 


## TAREA DISEÑO ##

Se implementó un algoritmo de inundación que al recibir un paquete revisa si es para él, caso contrario lo manda por sus 2 salidas full-duplex.

## Pasos del algoritmo

1. Cuando un `nodo x` *(nodo de origen)* necesita mandar un paquete a un destino `nodo y`, se inicializa el contador de saltos (`hops`) en 0 y envía el paquete a sus 2 vecinos, generando así un paquete en sentido anti-horario y otro en sentido horario.

2. Por cada nodo que se recibe el paquete, si no es el destino, el hoops aumenta en uno y se compara el valor de este:
    - Si `hoops < 4` => se pasa al siguiente nodo.
    - Si `hoops >= 4` => se descarta ese paquete.
    > `Cantidad máxima de hoops = cantidad de nodos / 2 = 4`

Este proceso ocurre sucesivamente hasta encontrar el nodo de destino `y`.

3. Cuando el paquete llega al nodo de destino `y`, lo consume la capa de aplicación.


La *cantidad de máxima de hoops* permite que la inundación utilice los mínimos recursos posibles mientras también se garantiza que un paquete llegue a cualquier destino del anillo.


### Hipótesis sobre el algoritmo

En este algoritmo se utiliza la idea de inundación selectiva, esto debería provocar una mejora en el *delay medio* de los paquetes, ya que no solo se tiene en cuenta la ruta en sentido horario sino también en sentido anti-horario, esto implica un aprovechamiento de los canales `full-duplex`.

De la misma manera, congestionará la red por naturaleza de la inundación, aumentando así la utilización de los buffers de todos los nodos.

Comparando con el algoritmo original debería haber una mínima mejora en la congestión o ninguna, dependiendo el caso, gracias a la característica de los paquetes de ser eliminados después de cierta cantidad de saltos.

### Análisis de algoritmo

Usando los mismos vectores para la parte de análisis podemos obtener buenos resultados:

##caso1
Los jumps son como máximo 3, el delay es como máximo 96, reduciendo un poco comparado con el algoritmo anterior

##caso2
Los jumps son como máximo 4 y el delay es de 187, que es mayor que el algoritmo anterior,(esto podría  ser incorrecto ya que podría estar calculando el delay de un paquete que no fue por el camino correcto y terminó dando saltos innecesarios y la capa de app está guardando en el vector) esto puede ser causa de el uso completo de la red por lo que un paquete podría tardar en desencolar hasta ser enviado al próximo nodo.
 
En ambos casos se utiliza toda la capacidad de la red para enviar paquetes por lo tanto en el caso 2 tenemos que todos los buffers están siendo usados.

###Posibles mejoras

A pesar de que el algoritmo dio un buen resultado, se podría implementar un algoritmo que pueda decidir por que canal enviar, una idea sería que se ejecute el algoritmo de Dijkstra para saber el costo de enviar un paquete a ambos canales para cada nodo y que el el nodo al enviar el paquete pueda saber qué camino conviene mejor.

