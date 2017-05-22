import zmq

context = zmq.Context()

print("Conectando con el servidor..")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

hashtag = raw_input("Introduce el hashtag a buscar: ")
socket.send(hashtag)

message = socket.recv()

print(message)
