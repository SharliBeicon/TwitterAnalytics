from web import *
import tasks
import DropboxUpload
from DropboxUpload import *
from bottle import *
from json import dumps

@get("<filepath:re:.*\.css>")
def css(filepath):
    return static_file(filepath, root="estilo/")

@get("<filepath:re:.*\.(eot|otf|svg|ttf|woff|woff2?)>")
def font(filepath):
    return static_file(filepath, root="./")

@get("<filepath:re:.*\.(jpg|png|gif|ico|svg)>")
def img(filepath):
    return static_file(filepath, root="estilo/")

@get("<filepath:re:.*\.json>")
def json(filepath):
    return static_file(filepath, root="./")

@get('/hashtag')
def operacion():
    return cargarweb()

@post('/hashtag')
def do_operacion():
    hashtag = request.forms.get("hashtag")
    tiempo = request.forms.get("tiempo")
    result = tasks.hashtag.delay(hashtag, float(tiempo))
    res1 = result.get()
    result2 = tasks.procesar.delay(hashtag)
    res2 = result2.get()

    if result2.successful():
        jsonLocalizacion = 'geo_data_'+hashtag[1:len(hashtag)]+'.json'
        MyDropbox().downloadLocation(jsonLocalizacion, '/subidas/'+jsonLocalizacion)

        return cargarwebmapa(jsonLocalizacion)
    else:
        print ("Imposible cargar el mapa.")

run(host='localhost', port=8080)
