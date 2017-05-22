#-*- coding: utf-8 -*-
import time
import zmq
import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener

consumer_key = 'kRNH81VeTyDeCHo6v5x2EWbzm'
consumer_secret = 'EHp5PUIqC6CXXEoofez5CDaNIIsBCrcISYCd7Sk4VDwunahUQ4'
access_token = '243348295-R1plXZdp6n1PjqnZYhFinhwVHmj76zJqSuqVS7IT'
access_secret = '4UEkdO0i984kFn2n7bgnsNuPybJeFB0fctqqf7mzv5PeE'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

class MyListener(StreamListener):
    def on_data(self, data):
        try:
            with open('python.json', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True

    def on_error(self, status):
        print(status)
        return True

while True:
    message = socket.recv()
    time.sleep(1)

    socket.send(b"[*]Información recolectandose correctamente")

    twitter_stream = Stream(auth, MyListener())
    twitter_stream.filter(track = [message])
