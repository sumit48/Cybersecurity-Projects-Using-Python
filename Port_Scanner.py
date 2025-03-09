import socket


# Function to scan a range of ports on a target IP
def scan_ports(target_ip, start_port, end_port):
    print(f"Scanning ports on {target_ip} from {start_port} to {end_port}...")

    for port in range(start_port, end_port + 1):
        # Create a socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Set timeout for socket connection attempt (1 second)

        # Try to connect to the port
        result = sock.connect_ex((target_ip, port))

        if result == 0:
            print(f"Port {port} is open.")
        else:
            print(f"Port {port} is closed.")

        # Close the socket
        sock.close()


# Main function to input target IP and port range
if __name__ == "__main__":
    target_ip = input("Enter the target IP address: ")
    start_port = int(input("Enter the starting port number: "))
    end_port = int(input("Enter the ending port number: "))

    scan_ports(target_ip, start_port, end_port)
