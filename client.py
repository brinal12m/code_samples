import socket
import ssl

def https_client(host, port, certfile, cipher_suite):
    context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH, cafile=certfile)
    context.set_ciphers(cipher_suite)

    with socket.create_connection((host, port)) as sock:
        with context.wrap_socket(sock, server_hostname=host) as ssock:
            #ssock.sendall(b"GET / HTTP/1.1\r\nHost: " + host.encode() + b"\r\nConnection: close\r\n\r\n")
            ssock.sendall(b"GET /hello HTTP/1.1\r\nHost: " + host.encode() + b"\r\nConnection: close\r\n\r\n")
            response = ssock.recv(4096)
            print("Response from server:")
            print(response.decode())

if __name__ == "__main__":
    HOST = 'autoclient215.autobot.cvp'
    PORT = 12346
    # CERTFILE = 'certs/autoclient215.autobot.cvp.crt'  # Path to your server certificate  # Path to your server certificate
    CERTFILE = 'certs/rsa.crt.pem'  # Path to your server certificate  # Path to your server certificate
    
	# CIPHER_SUITE= 'ECDHE-ECDSA-AES256-SHA'
	
	
	# CIPHER_SUITE = 'AES256-SHA256'             # For server RSA cipher TLS_RSA_WITH_AES_256_CBC_SHA
    # CIPHER_SUITE= 'ECDHE-RSA-AES256-SHA'       # For server ECDHE Cipher - TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA
    # CIPHER_SUITE = 'AES256-SHA256'             # For server RSA ciher - RSA-AES256-SHA256
    
    
    CIPHER_SUITE = 'ECDHE-RSA-AES256-SHA'
	
	
    https_client(HOST, PORT, CERTFILE, CIPHER_SUITE)
