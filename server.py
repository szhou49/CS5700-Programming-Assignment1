import socket
import threading

class Server:

    def __init__(self, server_socket=None):
        if server_socket is not None:
            self.server_socket = server_socket
        else:
            self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_name = "Server of Songling Zhou"
        self.server_num = 14
        self.flag = True

    def handleClient(self, client_socket, client_address):
        print(f"Connection established with {client_address}\n")
        try:
            while self.flag:
                data = client_socket.recv(1024).decode()
                if not data:
                    break
                arr = data.split(",")
                client_name = arr[0]
                client_num = int(arr[1])
                if (client_num >= 1 and client_num <= 100):
                    print(f"Client's name: {client_name}\nServer's name: {self.server_name}\nClient's number: {client_num}\nServer's number: {self.server_num}\nThe sum is: {client_num + self.server_num}\n")
                    response = f"{self.server_name},{self.server_num}"
                    client_socket.sendall(response.encode())
                else:
                    response = "Number is out of range. Server is close"
                    client_socket.sendall(response.encode())
                    self.flag = False
                    break
        except Exception as e:
            print(f"Error with {client_address}: {e}")
        finally:
            client_socket.close()
            print(f"Close connection from {client_address}")

    def run(self, server_address):
        self.server_socket.bind(server_address)
        self.server_socket.listen(5)
        print("Server is listening on port 8080...\n")
        while self.flag:
            try:
                self.server_socket.settimeout(1) 
                client_socket, client_address = self.server_socket.accept()
                thread = threading.Thread(target=self.handleClient, args=(client_socket, client_address))
                thread.start()
            except socket.timeout:
                continue
        self.server_socket.close()
        print("Server is closed")

server = Server()
server.run(("0.0.0.0", 8080))
