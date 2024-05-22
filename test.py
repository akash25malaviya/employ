import socket

def check_grpc_port(host, port):
    try:
        # Create a socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Attempt to connect to the specified host and port
        s.connect((host, port))
        
        # If connection successful, the port is open
        print(f"Port {port} is open for gRPC communication.")
        
        # Close the socket connection
        s.close()
    except ConnectionRefusedError:
        # If connection is refused, the port is closed or unreachable
        print(f"Port {port} is closed or unreachable for gRPC communication.")

# Replace 'host' and 'port' with your gRPC server's host and port
check_grpc_port('localhost', 50051)  