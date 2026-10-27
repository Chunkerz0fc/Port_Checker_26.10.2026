import socket

target_ip = "127.0.0.1"
ports_to_be_scanned = [21, 80, 8080, 443]

print("Now scanning IP address: ", target_ip )

try:
    for port in ports_to_be_scanned:

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        s.settimeout(0.9)
        
        result = s.connect_ex((target_ip, port))
        
        if result == 0:
            print(f"Port {port}: OPEN")
        else:
           print(f"Port {port}: Closed")
            
        s.close()

except KeyboardInterrupt:
    print("\nExiting script.")