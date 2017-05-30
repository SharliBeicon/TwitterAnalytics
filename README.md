# Twitter Maps
**Twitter™ Maps** es una aplicación cliente/servidor implementada en Python en la que un cliente introduce un hashtag y un tiempo de análisis, y el servidor le devuelve un mapa con los lugares concretos donde se ha utilizado dicho hashtag.

Creado por: "The Jarons Team"
* Iván Magariño Aguilar
* Eduardo Mesa Orcero
* Vicente Sánchez Dorado
* Carlos Tocino Cubelo

## Uso de la aplicación

1. Tener activo un proceso servidor de **rabbitmq-server**
2. ```celery -A tasks worker -l=info``` Para iniciar el worker que realiza los procesos de escucha de tweets, subida a dropbox, descargas y procesamiento.
3. ```sudo python consumer.py``` Para iniciar el servicio web.
4. Acceder al servicio web mediante http://localhost:8080/hashtag
5. Poner el hashtag, el tiempo y a esperar.
