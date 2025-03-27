import socket
import time

# TCP Server
def tcp_server(host='127.0.0.1', port=12345):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"TCP Server listening on {host}:{port}")
    
    conn, addr = server_socket.accept()
    print(f"Connected by {addr}")
    
    while True:
        data = conn.recv(1024)
        if not data:
            break
        conn.sendall(data)
    
    conn.close()
    server_socket.close()

# TCP Client
def tcp_client(host='127.0.0.1', port=12345, ping_count=5):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    
    for i in range(ping_count):
        message = f"Ping {i}"
        start_time = time.time()
        client_socket.sendall(message.encode())
        data = client_socket.recv(1024)
        end_time = time.time()
        print(f"Received: {data.decode()} - RTT: {end_time - start_time:.6f} seconds")
    
    client_socket.close()

# UDP Server
def udp_server(host='127.0.0.1', port=12346):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host, port))
    print(f"UDP Server listening on {host}:{port}")
    
    while True:
        data, addr = server_socket.recvfrom(1024)
        print(f"Received from {addr}: {data.decode()}")
        server_socket.sendto(data, addr)

# UDP Client
def udp_client(host='127.0.0.1', port=12346, ping_count=5):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.settimeout(1)
    
    for i in range(ping_count):
        message = f"Ping {i}"
        start_time = time.time()
        client_socket.sendto(message.encode(), (host, port))
        try:
            data, _ = client_socket.recvfrom(1024)
            end_time = time.time()
            print(f"Received: {data.decode()} - RTT: {end_time - start_time:.6f} seconds")
        except socket.timeout:
            print("Request timed out")
    
    client_socket.close()

if __name__ == "__main__":
    choice = input("Run server or client? (tcp_server/tcp_client/udp_server/udp_client): ")
    if choice == "tcp_server":
        tcp_server()
    elif choice == "tcp_client":
        tcp_client()
    elif choice == "udp_server":
        udp_server()
    elif choice == "udp_client":
        udp_client()
    else:
        print("Invalid choice.")
