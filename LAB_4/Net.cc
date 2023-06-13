#ifndef NET
#define NET

#include <string.h>
#include <omnetpp.h>
#include <packet_m.h>
#include "hello_m.h"
#define RING_SIZE 8


using namespace omnetpp;

class Net: public cSimpleModule {
private:
    void handleDataPacket(Packet *pkt);
	void reroutePacket(Packet *pkt);
	int getArrivalGateIndex(cMessage *msg);

	// Short Flood Algorithm
	void handleRerouteForShortFlood(Packet *pkt);
    
public:
    Net();
    virtual ~Net();
protected:
    virtual void initialize();
    virtual void finish();
    virtual void handleMessage(cMessage *msg);
};

Define_Module(Net);

#endif /* NET */

Net::Net() {
}

Net::~Net() {
}


void Net::initialize() {
}

void Net::finish() {
}



/*
Llama a la función handleDataPacket() 
para manejar el paquete de datos.
*/

void Net::handleMessage(cMessage *msg) {
    Packet *pkt = (Packet *) msg;
	handleDataPacket(pkt);
}



/*
 Esta función busca el índice de la puerta de entrada 
 en la que llegó el mensaje.
*/
int Net::getArrivalGateIndex(cMessage *msg) {
	for (int i=0; i<par("interfaces").intValue(); i++) {
		if (msg->arrivedOn("toLnk$i", i)) {
			return i;
		}
	}
    //si no se encuentra devuelve -1
	return -1;
}



/*
 Comprueba si el nodo actual es el destino del paquete. 
 Si es así, el paquete se envía al módulo de aplicación. 
 De lo contrario, se llama a handleRerouteForShortFlood(pkt) 
 para manejar el enrutamiento del paquete 
 utilizando el algoritmo de inundación corta.
*/

void Net::handleDataPacket(Packet *pkt) {
	std::cout << "HopCount = " << pkt->getHopCount() << "\n";
	if (pkt->getSource() != this->getParentModule()->getIndex()){
	    pkt->setHopCount(pkt->getHopCount() + 1);
	    std::cout << "HopCount = " << pkt->getHopCount() << "\n";
	}
	std::cout << "handling data packet on node[" << this->getParentModule()->getIndex();
	std::cout << "] with destination of node[" << pkt->getDestination() << "]\n";
    if (pkt->getDestination() == this->getParentModule()->getIndex()) {
    	// We are the destination
    	send(pkt, "toApp$o");
    } else {
    	handleRerouteForShortFlood(pkt);
	}
}



/* SHORT FLOOD FUNCTIONS */

/*
 Comprueba si el nodo actual es el origen del paquete. 
 Si es así, el paquete se envía a través de las puertas de salida 0 y 1 
 del módulo toLnk$o. 
 Si el nodo actual no es el origen y aún hay saltos disponibles
  antes de alcanzar el límite (hopsToLive), el paquete se reenvía 
  a través de la puerta de salida opuesta a la que llegó. 
  Si no hay más saltos disponibles, el paquete se elimina.
*/

void Net::handleRerouteForShortFlood(Packet *pkt) {
	if(pkt->getSource() == this->getParentModule()->getIndex()){
		// Somos el origen
		send(pkt->dup(), "toLnk$o", 0);
		send(pkt, "toLnk$o", 1);
	} else if (par("hopsToLive").intValue() - pkt->getHopCount() > 0) {
		// No somos el origen y todavía hay hops disponibles
		send(pkt, "toLnk$o", 1 - getArrivalGateIndex(pkt));
	} else {
		// No somos el origen y ya no hay hops disponibles
		delete(pkt);
	}
}