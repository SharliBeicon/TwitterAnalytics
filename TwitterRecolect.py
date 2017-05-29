import time
import tweepy
import json
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
def procesarTweets(archivo):
    f = open('descargas/' + archivo)
    geo_data = {
        "type": "FeatureCollection",
        "features": []
    }
    for line in f:
        try:
            localizacion = []
            tweet = json.loads(line) # load it as Python dict
            localizacion.append(tweet['place']['bounding_box']['coordinates'][0][0][0])
            localizacion.append(tweet['place']['bounding_box']['coordinates'][0][0][1])
            geo_json_feature = {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": localizacion
                },
                "properties": {
                    "text": tweet['text'],
                    "created_at": tweet['created_at']
                }
            }
            geo_data['features'].append(geo_json_feature)
        except:
            continue

    with open('geo_data.json', 'w') as fout:
        fout.write(json.dumps(geo_data, indent=4))
        f.close()
#Clase recolectora de datos de Twitter.
class MyListener(tweepy.StreamListener):
    def __init__(self, archivo, time_limit):
        self.start_time = time.time()
        self.limit = time_limit
        self.saveFile = open(archivo, 'a')
        super(MyListener, self).__init__()

    def on_data(self, data):
        if(time.time() - self.start_time) < self.limit:
            self.saveFile.write(data)
            self.saveFile.write('\n')
            return True
        else:
            self.saveFile.close()
            return False
