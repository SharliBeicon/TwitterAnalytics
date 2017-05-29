import dropbox
import tempfile

token = "m_VO84q7mPgAAAAAAAAITTsQfJiC7sFhgFrrVqp1y6a6xoyfO-NGrypTEJ_FxGAg"
dbx = dropbox.Dropbox(token)

class MyDropbox():
    def upload(self, archivo):
        with open (archivo, 'rb') as f:
            data = f.read()
        ruta = '/' + archivo
        return dbx.files_upload(data, ruta, mute = True)

    def download(self, archivo, ruta):
        dbx.files_download_to_file('descargas/'+archivo, ruta)

    def downloadLocation(self, archivo, ruta):
        dbx.files_download_to_file(archivo, ruta)
