from web import cargarweb
import tasks
import DropboxUpload
from DropboxUpload import *
from bottle import *
from json import dumps

@get('/hashtag')
def operacion():
    return '''
        <form action = "/hashtag" method="post">
            Hashtag: <input name = "hashtag" type = "text" />
            Tiempo (en segundos): <input name = "tiempo" type = "text" />
            <input value = "enviar" type = "submit" />
        </form>
    '''

@post('/hashtag')
def do_operacion():
    hashtag = request.forms.get("hashtag")
    tiempo = request.forms.get("tiempo")
    result = tasks.hashtag.delay(hashtag, float(tiempo))
    holi = result.get()
    result2 = tasks.procesar.delay(hashtag)
    tuits = result2.get()

    if result2.successful():
        jsonLocalizacion = 'geo_data_'+hashtag[1:len(hashtag)]+'.json'
        MyDropbox().downloadLocation(jsonLocalizacion, '/subidas/'+jsonLocalizacion)
        return cargarweb(jsonLocalizacion)
    else:
        print ("<p>[*] La shet</p>")

run(host='localhost', port=8080)
