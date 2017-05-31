import dropbox
import tempfile

token = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
dbx = dropbox.Dropbox(token)

class MyDropbox():
    def upload(self, archivo):
        with open (archivo, 'rb') as f:
            data = f.read()
        ruta = '/' + archivo
        try:
            dbx.files_upload(data, ruta, mute = True)
        except:
            print ('Error en la subida.')

    def download(self, archivo, ruta):
        try:
            dbx.files_download_to_file('descargas/'+archivo, ruta)
        except:
            print ('Error en la descarga.')

    def downloadLocation(self, archivo, ruta):
        try:
            dbx.files_download_to_file(archivo, ruta)
        except:
            print('Error en la descarga.')
