import socket

class Server:

    def __init__(self, server_socket=None):
        if server_socket is not None:
            self.server_socket = server_socket
        else:
            self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_name = "Server of Songling Zhou"
        self.server_num = 14

    def run(self, server_address):
        self.server_socket.bind(server_address)
        self.server_socket.listen(5)
        print("Server is listening on port 8080...\n")

        while True:
            # Accept an incoming client connection
            client_socket, client_address = self.server_socket.accept()
            print(f"Connection established with {client_address}\n")

            # Receive data from the client
            data = client_socket.recv(1024).decode().split(",")
            client_name = data[0]
            client_num = int(data[1])
            if (client_num >= 1 and client_num <= 100):
                print("Client's name: " + client_name + "\n" + "Server's name: " + self.server_name + "\n"
                        + "Client's number: " + str(client_num) + "\n" + "Server's number: " + str(self.server_num) + "\n" + "The sum is: " + str(client_num + self.server_num) + "\n")
                # Send a response back to the client
                response = self.server_name + "," + str(self.server_num)
                client_socket.sendall(response.encode())
                client_socket.close()
            else:
                response = "Number is out of range. Server is close"
                client_socket.sendall(response.encode())
                client_socket.close()
                break

server = Server()
server.run(("0.0.0.0", 8080))
