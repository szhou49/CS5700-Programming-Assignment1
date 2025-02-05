import socket
import threading
import random

def client_task(host, port):
    client_name = "Client of Songling Zhou"
    client_num = random.randint(1, 100)
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((host, port))
        message = f"{client_name},{client_num}"
        print(f"The message to be sent is: {message}")
        client.sendall(message.encode())
        print("Message is sent successfully!")
        response = client.recv(1024).decode()
        print(f"Server's message: {response}")
        try:
            data = response.split(",")
            server_name = data[0]
            server_num = int(data[1])
            print(f"Client's name: {client_name}\nServer's name: {server_name}\nClient's number: {client_num}\nServer's number: {server_num}\nThe sum is: {client_num + server_num}")
        except:
            print("Response has error\n")
        client.close()
    except Exception as e:
        print(e)

threads = []
NUM_CLIENTS = 5
for i in range(NUM_CLIENTS):
    thread = threading.Thread(target=client_task, args=('10.245.203.34', 8080))
    threads.append(thread)
    thread.start()
for thread in threads:
    thread.join()