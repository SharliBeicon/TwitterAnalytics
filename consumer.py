import tasks
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
        return '''
            <html>
            <head>
              <link rel="stylesheet" href="http://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.3/leaflet.css" />
              <script src="http://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.3/leaflet.js"></script>
              <script src="http://code.jquery.com/jquery-2.1.0.min.js"></script>
              <!-- this goes in the <head> -->
              <style>
              #map {
                height: 600px;
              }
              </style>
            </head>
            <body>
              <!-- this goes in the <body> -->
              <div id="map"></div>
              <script>
                // Load the tile images from OpenStreetMap
              var mytiles = L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
                  attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
              });
              // Initialise an empty map
              var map = L.map('map');
              // Read the GeoJSON data with jQuery, and create a circleMarker element for each tweet
              // Each tweet will be represented by a nice red dot
              $.getJSON("geo_data.json", function(data) {
                  var myStyle = {
                      radius: 2,
                      fillColor: "red",
                      color: "red",
                      weight: 1,
                      opacity: 1,
                      fillOpacity: 1
                  };

                  var geojson = L.geoJson(data, {
                      pointToLayer: function (feature, latlng) {
                          return L.circleMarker(latlng, myStyle);
                      }
                  });
                  geojson.addTo(map)
              });
              // Add the tiles to the map, and initialise the view in the middle of Europe
              map.addLayer(mytiles).setView([50.5, 5.0], 5);
              </script>
            </body>
            </html>
        '''
    else:
        print ("<p>[*] La shet</p>")

run(host='localhost', port=8080)
