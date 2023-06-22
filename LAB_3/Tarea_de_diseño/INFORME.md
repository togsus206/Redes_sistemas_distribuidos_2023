### CAPA DE TRANSPORTE: PROBLEMAS DE FLUJO Y CONGESTIÒN
## Simulaciòn discreta y analisis sobre el problema y sus soluciones

## Resumen
  Analizaremos el trafico de redes mediante la simulaciòn discreta generada con Omnet++, para observar y proponer soluciones a los
  problemas que se presentan en la Capa de Transporte. Se simulara una red constituida por varios nodos que transportan paquetes 
  entre ellos. Se realizaron experimentaciones para obtener datos, que fueron gràficados para su analisis y ver el impacto de algunas 		  variables que pueden alterar el flujo de los paquetes.


# INTEGRANTES:
    -Agustín Molina
    -Bruno Volpini
    -Matias Valle
=============================

## INTRODUCCIÒN
  Las redes estan compuestas por nodos que transmiten paquetes entre si. Estos generan una carga en la red al ser transportados hacia un nodo y tambien la generan sobre el receptor del paquete. 
  La capa de transporte, encontrada en cada uno de estos nodos, debe asegurarse de no generar una carga que exceda la capacidad de la red o del receptor, esto generaria perdida de paquetes.
  La capa de transporte se enfrenta a dos problemas:
  1. Control de flujo: el receptor no es capaz de satisfacer la tasa de transmisiòn de los datos del emisor.
  2. Congestion de la red: La red no es capaz de soportar la tasa de transmisiòn de los emisores, es decir, acepta màs trafico del que puede aceptar.  
  
  Simulamos estor problemas usando Omnet++, donde nos permite crear simulaciones discretas de una red constrituida por nodos que se transmiten paquetes entre si. Usamos simulaciones para evitar costos y tiempo que llevaria hacerlo sobre un sistema fisico real.

  La simulaciòn discreta nos permite reproducir 2 casos que ejemplifican los problemas de Control de Flujo y Congestiòn de Red.
  Mediremos la cantidad de paquetes recibidos durante la simulaciòn, observaremos cuantos paquetes fueron recibidos y cuantos fueron perdidos durante la transferencia.

=============================

## TAREA ANALISIS ##

#Caso 1

- Exponential(0.1)

Grafica del Delay --> [Link](https://postimg.cc/LYvSZ3CR)
Grafica de dropeados-recibidos --> [Link](https://postimg.cc/GT2CPTVD)
Grafica de Enviados-Recibidos --> [Link](https://postimg.cc/238rNgy5)
Grafica de tamaño de Buffers --> [Link](https://postimg.cc/Z07Zbjvx)

En este caso podemos ver que primero, hay muchisimos packets dropeados en la queue del NodoRx, debido a que el datarate es la mitad del que maneja el NodoTx y la queue. Por lo tanto el buffer se llena y dropea packets, ademas no es la misma cantidad de enviados y recibidos
y el tamaño del buffer del nodoRx llega hasta 200 y es constante. Todo esto debido a que la tasa de transferencia es muy alta y la cantidad de packets enviados es demasiado rapido para procesarlos.

- Exponential(0.2)

Grafica Tamaño de Buffer Tx -->[Link](https://postimg.cc/TpVzy9ps)
Grafica Delay -->[Link](https://postimg.cc/NKQWRHXj)
Grafica Tamaño de Buffer Rx -->[Link](https://postimg.cc/8jzY5Sg7)

En este caso se puede ver que primero el buffer del NodoTx empieza a cambiar, tiene picos de paquetes en el buffer pero se alivia al instante.  el delay baja comparado con el caso del Exponential (0.1).El tamaño del buffer del NodoRx, no llega al punto de dropear paquetes pero si tiene un pequeño pico de paquetes. No hay ocurrencias de paquetes dropeados(No se agrego la grafica de enviados-recibidos, debido a que la diferencia es minima,  hay 12 paquetes generados de mas que los recibidos, posiblemente quedaron en queue)

- Exponential(0.3)

Grafica Tamaño de Buffer Rx -->[Link](https://postimg.cc/jWMwRPHw)
Grafica Delay -->[Link](https://postimg.cc/Vr5Svvg7)

en este caso podemos ver que el buffer del Nodo Rx tiene picos pero se alivia al instante a diferencia de casos anteriores y el delay lo mismo, tiene picos de delay pero se alivia al instante. No hay dropeados, el tamaño del buffer de Tx es similar a el caso anterior,(No se agrego la grafica de enviados-recibidos, debido a que la diferencia es minima,  hay 4 paquetes generados de mas que los recibidos, posiblemente quedaron en queue)

- Exponential (0.4)

Grafica Delay -->[Link](https://postimg.cc/HVjCN5xv)

en este caso no se incluyo la misma cantidad de graficas porque, la cantiadad de paquetes en los NodoRx y NodoTx son muy similares, con un maximo de 3 paquetes en cola para ambos nodos que se alivian al instante, la cantidad de recibidos es igual que la de enviados, no hay paquetes dropeados y el delay a lo sumo es de 1 por lo tanto este caso es bastante estable

- Exponential (0.5)

en este caso es muy similar a el caso anterior, el delay tiene un maximo de 1, el tamaño del buffer del NodoTx tiene a lo maximo 2 paquetes y se alivia y el NodoRx tiene como maximo 3 paquetes, la cantidad de enviados se diferencia de 1 con los recibidos(puede haber quedado en el queue), No hay Dropeados

- Exponential (0.6)

en este caso el delay tiene un maximo de 0.8, el tamaño del buffer de ambos nodos tiene como maximo 2 paquetes, No hay dropeados y la cantidad de recibdos se diferencia de 2 con los enviados(quedaron en queue)

- Exponential (0.7)

en este caso el delay tiene un maximo de 0.8, el tamaño del buffer de ambos nodos tiene como maximo 2 paquetes, No hay dropeados y la cantidad de recibdos es igual a los enviados

- Exponential (0.8),(0.9) y 1

en todos estos casos es muy similar al caso de Exponential (0.7), salvo en el Exponential (1) que el buffer del NodoRx es constante 1.

#Caso 2

- Exponential (0.1)

Grafica del Delay --> [Link](https://postimg.cc/fVfcG3kp)
Grafica de dropeados-recibidos --> [Link](https://postimg.cc/XrbK1KN9)
Grafica de Enviados-Recibidos --> [Link](https://postimg.cc/XpFcg1WV)
Grafica de tamaño de Buffers --> [Link](https://postimg.cc/BtRBH9dY)

en este caso podemos apreciar un caso similar al caso 1 con Exponential(0.1) tenemos un delay creciente, y alto, hay muchos paquetes dropeados comparado de los recibidos, hay mas enviados que recibidos. La diferencia es que en este caso, la cantidad de paquetes de la queue entre NodeRx y NodeTx es el problema, se llena y empieza a dropear paquetes y es debido a que reducimos la tasa de transferencia a la mitad que manejan los nodos


- Conclusion:
    en los proximos casos de Exponential podemos ver lo mismo que pasa en el caso 1, solo que el problema radica en la queue intermedia que es mas lenta que los anteriores nodos.

*****************************************************************************

**¿QUE ESTA PASANDO?!?!?**

la explicacion a estos casos son que en caso 1 tenemos un problema de control de flujo, tenemos un emisor muy rapido y un receptor lento.
en el caso 2 tenemos un problema de control de congestion, el trafico intermedio entre los nodos es lento.


-----------------------------------------------------------------------------------------------------------

## TAREA DISEÑO ##

### Explicacion de como se maneja el tema de control de congestion y flujo:

## Control de Flujo

Cuando la utilizacion del buffer del receptor es mayor a 96% (Fijado con la variable EMERGENCY_PERCENT_BUFF), se envian unos paquetes de emergencia de flujo por la queue que se usa como canal de retroalimentacion.
Cuando el emisor recibe este mensaje, lo que hace es introducir un retardo (acumulable) en el envio de los paquetes (FLOW_DELAY_RATE) durante un tiempo especifico (FLOW_TIMER).
(Este FLOW_TIMER se reestablece cada vez que llega un mensaje de emergencia de flujo).

## Control de Congestion

El emisor lleva una cuenta de los paquetes que le ha enviado al receptor, y de igual forma el receptor lleva una cuenta de los paquetes recibidos por el emisor.
Cada un tiempo (STATUS_PKT_TIMER) el receptor envia un paquete de control con su tamaño de buffer, paquetes recibidos y la utilizacion en cantidad de paquetes.
Entonces el emisor al recibir el paquete de control y calcula la diferencia entre paquetes enviados y recibidos por el receptor(gracias al paquete de control).
Si esta diferencia es mayor a 85 paquetes (CONGESTION_PKTS_DIFF_TOLERANCE), se inicializa un temporizador de congestion y se agrega un retardo acumulable a la emision de paquetes.
EL temporizador de congestion se reestablece si llega otro paquete de control.

Tambien existe un mecanismo de seguridad que elimina el retardo introducido por el control de flujo cuando se detecta que el receptor tiene un buffer con menos de
MIN_FAILSAFE_BUFFERSIZE_FLOW (45 paquetes) indicado por el paquete de control. Esto es por si se calibra mal el temporizador o el retardo acumulable.


*** Introduccion del algoritmo ***

### NodeTx: ###
 Este módulo es un nodo de transmisión en la red. Contiene un generador (gen) y un módulo de transmisión (transTx). El generador crea paquetes y los envía al módulo de transmisión para su posterior procesamiento. El nodo de transmisión tiene una puerta de salida (toOut) que está conectada a otras partes de la red.

 El método handleMessage(cMessage *msg) se llama cuando se recibe un mensaje. Este método implementa la lógica de transmisión y gestión de la congestión:

        # Si el mensaje tiene getKind() == 1, se trata de un paquete de flujo de emergencia y se actualiza el retraso de flujo y el temporizador de flujo.

        # Si el mensaje tiene getKind() == 2, se trata de un paquete de retroalimentación y se realizan varias operaciones, como la comprobación de la diferencia entre los paquetes enviados y los paquetes recibidos, el restablecimiento del retraso de flujo en caso de que el tamaño del búfer sea demasiado pequeño y la detección de posible congestión.

        # Si el mensaje tiene getKind() == 0, se trata de un paquete de datos para transmitir. Se realizan operaciones adicionales como el restablecimiento de los temporizadores de congestión y flujo, la comprobación del tamaño del búfer, la inserción del paquete en el búfer, la programación del evento de finalización del servicio si no está programado y el envío del paquete.

### NodeRx: ### 
Este módulo es un nodo de recepción en la red. Contiene un módulo de recepción (transRx) y un destino final (sink). Los paquetes recibidos por el módulo de recepción se envían al destino final para su procesamiento. Al igual que el nodo de transmisión, también tiene una puerta de entrada y salida para conectarse a otros módulos de la red.

El método handleMessage(cMessage *msg) se llama cuando se recibe un mensaje. Este método implementa la lógica de recepción y el envío de retroalimentación y paquetes de control.

    # Si el mensaje tiene getKind() == 0, se trata de un paquete de datos recibido. Se realizan operaciones como la inserción del paquete en el búfer, la programación del evento de finalización del servicio si no está programado y el envío del paquete al módulo de la aplicación.

    # Se crea un objeto FeedbackPkt para enviar retroalimentación y paquetes de control. Se configura el tipo de paquete según las condiciones del búfer y se envía al módulo de salida correspondiente.


**Antecedentes:**
Inicialmente, la simulación contaba con los módulos `TransportTx` y `TransportRx` que se encargaban del envío y recepción de paquetes respectivamente. Sin embargo, no existía una comunicación directa entre estos módulos para intercambiar información sobre el estado de la red. Esto limitaba la capacidad del sistema para adaptarse y tomar decisiones basadas en el estado actual de la transmisión.

### Implementado

Se ha implementado una funcionalidad de retorno de retroalimentación desde el módulo receptor (`TransportRx`) hacia el módulo transmisor (`TransportTx`). Esta adición permite mejorar el funcionamiento global de la simulación y optimizar el flujo de paquetes a través de la red.


**Objetivo:**
El objetivo principal de esta mejora era implementar un mecanismo de retroalimentación entre los módulos `TransportTx` y `TransportRx` para intercambiar información vital sobre el estado de la red. Con esta información, el módulo transmisor podría ajustar su comportamiento y tomar decisiones adecuadas para mejorar el rendimiento general del sistema.

**Implementación:**
Para lograrlo se introdujo la clase de mensaje `FeedbackPkt` que actúa como un paquete de retroalimentación. Esta clase de mensaje contiene dos tipos de información clave: `pktReceived_info` y `bufferSize_info`. El primero indica la cantidad de paquetes recibidos por el módulo receptor (`TransportRx`), mientras que el segundo indica el tamaño del búfer en el receptor.

Se agregaron secciones de código en los módulos `TransportTx` y `TransportRx` para enviar y recibir paquetes de retroalimentación. En el módulo `TransportRx`, se verificó periódicamente el estado de la red y se generaron paquetes de retroalimentación en función de ciertos criterios, como el nivel de ocupación del búfer. Estos paquetes de retroalimentación se enviaron al módulo `TransportTx` a través de la conexión establecida.

En el módulo `TransportTx`, se implementó la lógica para procesar los paquetes de retroalimentación recibidos. Estos paquetes proporcionaban información valiosa sobre el estado de la red, como posibles congestiones o diferencias entre los paquetes enviados y recibidos. Basándose en esta información, el módulo `TransportTx` tomaba decisiones inteligentes para ajustar la velocidad de envío de paquetes o detectar posibles problemas en la red.

**Beneficios y Conclusiones:**
La adición del retorno de retroalimentación desde el módulo `TransportRx` al módulo `TransportTx` ha mejorado significativamente el funcionamiento de la simulación. Al recibir información en tiempo real sobre el estado de la red, el módulo transmisor puede ajustar su comport




-----------------------------------------------------------------------------------------------------------


Para esta seccion solo nos vamos a concentrar en los casos que causan mas problemas de flujo y congestion, estos son respectivamente el caso 1 Exponential(0.1) y caso 2 Exponential (0.1)


#Caso 1
Exponential (0.1)

Grafica de Delay --> [Link](https://postimg.cc/18r3pn21)
Grafica de Enviados-Recibidos --> [Link](https://postimg.cc/Bj0vLchC)
Grafica de Tamaño De buffers --> [Link](https://postimg.cc/HcpbC88p)

Comparando la grafica de enviados-recibidos de la tarea de analisis podemos concluir dos cosas, la primera es que se recibieron 100 paquetes menos en sink y segundo no tenemos registro de packet drops, la mayoria de los paquetes quedaron en el buffer del nodoTx ya que ahi almacenamos los paquetes a ser enviados, por la grafica del tamaño del buffer, los paquetes restantes a ser recibidos quedaron en el buffer del nodoTx por lo tanto evitamos tener packet drops a costa de usar el buffer de nodeTx para almacenar los paquetes. Esto tambien explica un delay alto ya que mucho de los paquetes quedan almacenados en el buffer del nodoTx tardarian un tiempo en llegar al nodoRx para no congestionar la red.


#Caso 2
Exponential (0.1)

Grafica de Delay --> [Link](https://postimg.cc/t74FSPHk)
Grafica de Enviados-Recibidos --> [Link](https://postimg.cc/Bj0vLchC)
Grafica de Tamaño De buffers --> [Link](https://postimg.cc/N2FTKhxS)

En este caso apreciamos lo mismo que el caso 1, nuestro algoritmo evita la congestion limitando cuantos paquetes envia por la red, recibiendo feedback del nodoRx. El delay y Enviados-recibidos es el mismo por lo explicado anteriormente y el buffer del nodoRx nunca llega a 200 para evitar packet drops


--------------------------------------------

#Carga util vs. carga ofrecida


para la proximas graficas aclaramos algunas cosas, los paquetes usados son la suma de los que se usaron mas los que estan en las queue que asumimos que estos paquetes eventualmente van a ser usados en algun tiempo de ejecucion ademas se añadio un caso con generationInterval=exponential(0.05)


Grafica de casos superpuestos -->[Link](https://postimg.cc/BtB3wNtQ)



