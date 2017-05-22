#-*- coding: utf-8 -*-
#Bibliotecas necesarias.
import time
import zmq
import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener

#Asignacion de las claves para la API de Twitter
consumer_key = 'kRNH81VeTyDeCHo6v5x2EWbzm'
consumer_secret = 'EHp5PUIqC6CXXEoofez5CDaNIIsBCrcISYCd7Sk4VDwunahUQ4'
access_token = '243348295-R1plXZdp6n1PjqnZYhFinhwVHmj76zJqSuqVS7IT'
access_secret = '4UEkdO0i984kFn2n7bgnsNuPybJeFB0fctqqf7mzv5PeE'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

#Creación del socket para la comunicación con el cliente.
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

#Clase recolectora de datos de Twitter.
class MyListener(StreamListener):
    def __init__(self, time_limit=120):
        self.start_time = time.time()
        self.limit = time_limit
        self.saveFile = open('abcd.json', 'a')
        super(MyListener, self).__init__()

    def on_data(self, data):
        if(time.time() - self.start_time) < self.limit:
            self.saveFile.write(data)
            self.saveFile.write('\n')
            return True
        else:
            self.saveFile.close()
            return False

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
