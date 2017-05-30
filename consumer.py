from web import cargarweb
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
    return '''
	<!DOCTYPE html>
	<html lang="es">
	    <head>
	        <meta charset="utf-8" />
	        <title>Twitter Analylics</title>
	        <link rel="stylesheet" href="estilo.css" type="text/css"/>
	        <script>
				function enviar_formulario(){
   					document.form.submit()
				}
			</script>
	    </head>
	    <body>
	    <img id = "titulo" src="titulo.png"  style="position:relative; left: 23%; width: 50%; height: 50%;" >
		    <form name = "form" action = "/hashtag" method="post" style="position: absolute; left: 28%; top: 60%">
	            Hashtag: <input id = "hastag" name = "hashtag" type = "text" />
	            Tiempo (en segundos):   <input id = "tiempo" name = "tiempo" type = "text" />
	            <a class="myButton" href="javascript:enviar_formulario()" >E N V I A R</a>
        	</form>
	    </body>
	</html>
    '''

@get('/<filename>')
def stylesheets(filename):
    return static_file(filename, root='./')

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
