import socket

class Client:

    def __init__(self, client_socket=None):
        if client_socket is not None:
            self.client_socket = client_socket
        else:
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_name = "Client of Songling Zhou"

    def connect(self, server_address):
        self.client_socket.connect(server_address)
        client_num = int(input("Enter an integer: "))
        message = self.client_name  + "," + str(client_num)
        print("The message to be sent is: " + message)
        self.client_socket.sendall(message.encode())
        print("Message is sent successfully!")
        response = self.client_socket.recv(1024).decode()
        print(f"Server's message: {response}")
        try:
            data = response.split(",")
            server_name = data[0]
            server_num = int(data[1])
            print("Client's name: " + self.client_name + "\n" + "Server's name: " + server_name + "\n"
                    + "Client's number: " + str(client_num) + "\n" + "Server's number: " + str(server_num) + "\n" + "The sum is: " + str(client_num + server_num))
        except:
            print("Response has error\n")
        self.client_socket.close()
        
client = Client()
client.connect(('10.245.219.114', 8080))