# encoding: utf-8
# Revisión 2019 (a Python 3 y base64): Pablo Ventura
# Copyright 2014 Carlos Bederián
# $Id: connection.py 455 2011-05-01 00:32:09Z carlos $

import socket
from constants import *
from base64 import b64encode
import os
from os.path import join, getsize

def is_number(n):
    try:
        int(n)
    except:
        return False
    return True


class Connection(object):
    """
    Conexión punto a punto entre el servidor y un cliente.
    Se encarga de satisfacer los pedidos del cliente hasta
    que termina la conexión.
    """

    def __init__(self, socket, directory):
        # FALTA: Inicializar atributos de Connection
        
        #Inicializacion de los atributos para la conexion
        self.sock = socket
        self.dir = directory

        #Lo que llega desde el cliente
        self.buffer_in = ''

        #Lo que se envia al cliente 
        self.buffer_out = ''

        #Variable para saber si la conexion esta activa
        self.is_connection_active = True

    #Envia strings al cliente
    def send_to_buff(self):
        while(self.buffer_out):
            # send_bytes = self.sock.send(str.encode(self.buffer_out))
            send_bytes = self.sock.send(bytes(self.buffer_out, 'ascii'))
            assert send_bytes > 0
            self.buffer_out = self.buffer_out[send_bytes:]

    ######################################################
    ## METODOS PARA EL MANEJO DE ERRORES

    # Mensaje de todo correcto
    def all_ok(self):
        self.buffer_out += str(CODE_OK)
        self.buffer_out += space + error_messages[CODE_OK] + EOL
        self.send_to_buff()

    # Mensaje de caracter "r\n" fuera de un pedido EOL
    def bad_eol(self):
        self.buffer_out += str(BAD_EOL)
        self.buffer_out += space + error_messages[BAD_EOL] + EOL
        self.send_to_buff()

    # Mensaje de pedido mal formado
    def bad_request(self):
        self.buffer_out += str(BAD_REQUEST)
        self.buffer_out += space + error_messages[BAD_REQUEST] + EOL
        self.send_to_buff()

    # Mensaje de error interno del servidor
    def internal_error(self):
        self.buffer_out += str(INTERNAL_ERROR)
        self.buffer_out += space + error_messages[INTERNAL_ERROR] + EOL
        self.send_to_buff()
        self.quit()

    # Mensaje de argunmentos invalidos
    def unknown_command(self):
        self.buffer_out += str(INVALID_COMMAND)
        self.buffer_out += space + error_messages[INVALID_COMMAND] + EOL
        self.send_to_buff()

    # Mensaje de argumentos invalidad
    def wrong_argue(self):
        self.buffer_out += str(INVALID_ARGUMENTS)
        self.buffer_out += space + error_messages[INVALID_ARGUMENTS] + EOL
        self.send_to_buff()

    # Mensaje de archivo inexistente
    def file_not_found(self):
        self.buffer_out += str(FILE_NOT_FOUND)
        self.buffer_out += space + error_messages[FILE_NOT_FOUND] + EOL
        self.send_to_buff()

    # Mensaje de posicion inexistente en un archivo
    def bad_offset(self):
        self.buffer_out += str(BAD_OFFSET)
        self.buffer_out += space + error_messages[BAD_OFFSET] + EOL
        self.send_to_buff()


    ########################################################################
    # METODOS PARA EL MANEJO DE ARCHIVOS Y SALIDA

    #Listar los archivos de un directorio
    def get_file_listing(self):
        print("Request: get_file_listing")
        # Mensjae de estado OK
        self.sock.send(bytes('0 OK'+EOL, 'ascii'))
        files =  os.listdir(self.dir+"/")
        for fil in files:
            # Enviamos cada nombre de los archivos
            self.sock.send(bytes(fil+EOL, 'ascii'))
        # Enviamos fin de respuesta
        self.sock.send(bytes(EOL, 'ascii'))
        


    # Obtiene los datos de un archivo
    def get_metadata(self, filename):
        try:
            print("Request: get_metadata")
            if len(filename) > 2**20:
                raise FileNotFoundError
            file_stats = os.stat(self.dir+"/"+filename)
            self.sock.send(bytes('0 OK'+EOL, 'ascii'))
            self.sock.send(str(file_stats.st_size).encode())
            self.sock.send(bytes(EOL, 'ascii'))
        except ValueError:
            self.file_not_found()
        except FileNotFoundError:
            self.file_not_found()
        except:
            self.internal_error()



    # Obtioene una parte de un archivo
    def get_slice(self, _file, _offset, _size):
        if (is_number(_offset) == False or is_number(_size) == False):
            self.wrong_argue()
            return

        offset = int(_offset)
        size = int(_size)
        filename = str(_file)


        len_file = os.path.getsize(self.dir+"/"+filename)
        over_size = (offset+size) > len_file


        #Si se pide mas del largo de archivo levanta excepcion
        if over_size:
            self.bad_offset()
            return
        
        is_file = os.path.exists(self.dir+"/"+_file)
        if(is_file == False):
            self.file_not_found()
            return
            
    
        open_file = open(self.dir+'/' + _file, "rb")

        #situamos el puntero del archivo desde donde queremos leer
        open_file.seek(offset)
        # Leemos fragmento del archivo
        file_read = open_file.read(size)
        b64file = b64encode(file_read)
        formato = b64file.decode('ascii')
        open_file.close()
        self.sock.send(bytes('0 OK'+EOL, 'ascii'))
        self.sock.send((formato+EOL).encode())
        

    


    # Cierra la conexion
    def quit(self):
        print("Request: quit")
        self.sock.send(bytes('0 OK'+EOL, 'ascii'))
        print("Cerrando la conexion...")
        while self.is_connection_active:
            self.is_connection_active = False
            self.sock.close()

    
    ##############################################################


    def analize_request(self, req_commmand):
        commands = req_commmand.split(sep="\\r\\n")

        if commands[len(commands)-1] == '':
            commands.pop()
        
        for mini_req in commands:
            #Dividimos los pedidos recibidos
            temp_command = mini_req.split(space)

            if (temp_command[0] == 'get_file_listing'):
                if (len(temp_command) == 1):
                    self.get_file_listing()
                else: 
                    self.wrong_argue()

            elif (temp_command[0] == 'get_metadata'):
                if (len(temp_command) != 2 or temp_command == ''):
                    self.wrong_argue()
                else: 
                    self.get_metadata(temp_command[1])

            elif (temp_command[0] == 'get_slice'):
                if (len(temp_command) == 4):
                    self.get_slice(temp_command[1], temp_command[2], temp_command[3])
                else: 
                    self.wrong_argue()
            

            elif (temp_command[0] == 'quit'):
                if len(temp_command) == 1:
                    self.quit()
                else: 
                    self.wrong_argue()
            else: 
                self.unknown_command()



    def handle(self):
        """
        Atiende eventos de la conexión hasta que termina.
        """
        while self.is_connection_active:
            #Recibe datos hasta un EOL(end of line)
            while EOL not in self.buffer_in:
                #Recibe datos del socket en bytes
                reception_text = self.sock.recv(READ_SIZE)
                
                #Como se reciben datos en bytes, los decodificamos 
                #para pasarlos a una string y poder compararlos
                reception_text_decode = reception_text.decode("ascii")
                self.buffer_in += reception_text_decode

            #Separamos el primer pedido de los demas
            request, self.buffer_in = self.buffer_in.split(EOL,1)

            #Revisamos que no haya un " \n" fuera de lugar
            if new_line in request:
                self.bad_eol()
            #Caso contrario analizamos el primero pedido recibido
            else: 
                self.analize_request(request)
        #Finalmente, cerramos el socket
        self.sock.close()
