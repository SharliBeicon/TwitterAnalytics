#-*- coding: utf-8 -*-
#Bibliotecas necesarias.
import time
import zmq
import json

import TwitterRecolect
from TwitterRecolect import *

#Creación del socket para la comunicación con el cliente.
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

#Esperamos que un cliente establezca una conexión con el servidor.
print "[*] Esperando conexión.."
while True:
    message = socket.recv()
    time.sleep(1)

    socket.send(b"[*] Información recolectandose correctamente")
    if(len(message) != 0):
        break

#Captamos los Tweets según el hashtag desado.
print "[*] Hashtag captado"
twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track = [message])

#Procesamiento de campos del json
f = open('abcd.json', 'r')
for line in f:
    try:
        tweet = json.loads(line) # load it as Python dict
        print(tweet['id'])
    except (ValueError, KeyError) as e:
        continue
f.close()
