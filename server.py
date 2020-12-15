import socket
import threading

HEADER = 64
PORT = 8760
SERVER = '192.168.208.9'

print(SERVER)

ADDR = (SERVER, PORT) 
FORMAT = 'utf-8'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def incoming_clients(conn, addr):
	print(f"New connection established for {addr}")
	connected = True
	while connected:
		msg_length = conn.recv(HEADER).decode(FORMAT)
		if msg_length:
			msg_length = int(msg_length)
			msg = conn.recv(msg_length).decode(FORMAT)
			print(f"{addr} sent: {msg}")		
			conn.send("MSG RECEIVED".encode(FORMAT))
			if msg == "DISCONNECT":
				connected = False
	conn.close()
		
def main():
	server.listen()
	print(f'Server has started listening for clients on {SERVER}...')
	while True:
		conn, addr = server.accept()
		thread = threading.Thread(target=incoming_clients,args=(conn, addr))
		thread.start()
		print(f'NO of Clients that are connected: {threading.activeCount() -1}')
	server.close()

print("Server Program has started...")
main()
