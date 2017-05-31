from celery import Celery, task
import os

import TwitterRecolect
import DropboxUpload
from DropboxUpload import *
from TwitterRecolect import *

app = Celery("tasks", backend="rpc://", broker="pyamqp://guest:guest@127.0.0.1//")

@app.task(no_ack=True)
def hashtag(mensaje, tiempo):
    os.system('mkdir subidas')
    archivo = 'subidas/'+ mensaje + '.json'

    twitter_stream = Stream(auth, MyListener(archivo, tiempo))
    twitter_stream.filter(track = [mensaje])

    MyDropbox().upload(archivo)
    os.system('rm '+archivo)
    return 'Hashtag obtenido.'

@app.task(no_ack=True)
def procesar(mensaje):
    os.system('mkdir descargas')
    ntweets = 0
    archivo = mensaje + '.json'
    ruta = '/subidas/' + archivo

    MyDropbox().download(archivo, ruta)
    procesarTweets(archivo)

    return 'json procesado.'
