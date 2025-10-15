# client.py
import socket

def start_client():
    try:
        # Create a TCP/IP socket
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Server details to connect to
        host = '127.0.0.1'
        port = 5000

        # Connect to the server
        client_socket.connect((host, port))
        print("Connected to server.")

        # Send message to the server
        message = "Hello from client!"
        client_socket.send(message.encode())

        # Receive response from server
        response = client_socket.recv(1024).decode()
        print(f"Server replied: {response}")

        # Close connection
        client_socket.close()
        print("Connection closed.")

    except socket.error as e:
        print(f"Socket error: {e}")
    except Exception as e:
        print(f"General error: {e}")

if __name__ == "__main__":
    start_client()
    