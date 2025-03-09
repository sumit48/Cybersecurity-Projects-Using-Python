import ipaddress
import platform

def validate_ip(ip):
    """ Validate single IP address (not CIDR) """
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False

def validate_port(port):
    """ Validate if the port is within the valid range """
    return port.isdigit() and 1 <= int(port) <= 65535

def generate_firewall_rule(source_ip, destination_ip, port, action):
    # Validate IPs
    if not validate_ip(source_ip) or not validate_ip(destination_ip):
        return "Invalid IP Address"

    # Validate Port
    if not validate_port(port):
        return "Invalid Port Number (should be between 1 and 65535)"

    port = int(port)  # Convert to integer
    action = action.upper()  # Ensure uppercase (ACCEPT, DROP)

    # Generate firewall rule based on OS
    if platform.system() == "Windows":
        rule = (f'netsh advfirewall firewall add rule name="Custom Rule" '
                f'dir=in action={action} protocol=TCP remoteip={source_ip} remoteport={port}')
    else:
        rule = f"iptables -A INPUT -s {source_ip} -p tcp --dport {port} -j {action}"

    return rule

# Example usage
source_ip = input("Enter the source IP: ").strip()
destination_ip = input("Enter the destination IP: ").strip()
port = input("Enter the port (1-65535): ").strip()
action = input("Enter the action (ACCEPT or DROP): ").strip()

firewall_rule = generate_firewall_rule(source_ip, destination_ip, port, action)
print(f"Generated Firewall Rule: {firewall_rule}")
