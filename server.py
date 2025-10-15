# server.py
import socket

def start_server():
    try:
        # Create a TCP/IP socket
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Bind the socket to an IP address and port
        host = '127.0.0.1'  # Localhost
        port = 4000
        server_socket.bind((host, port))

        # Listen for incoming connections
        server_socket.listen(1)
        print(f"Server listening on {host}:{port}")

        # Accept a connection from a client
        conn, addr = server_socket.accept()
        print(f"Connected by {addr}")

        # Receive data from client
        data = conn.recv(1024).decode()
        print(f"Client says: {data}")

        # Send a response
        conn.send("Hello from server!".encode())

        # Close the connection
        conn.close()
        print("Connection closed.")

    except socket.error as e:
        print(f"Socket error: {e}")
    except Exception as e:
        print(f"General error: {e}")

if __name__ == "__main__":
    start_server()
