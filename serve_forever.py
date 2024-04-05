import http.server
import ssl
import socket

class SimpleHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/hello':
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Hello World!")
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Not Found")

def serve_forever_ssl(server):
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    except ssl.SSLError as e:
        print("SSL Error:", e)
        serve_forever_ssl(server)  # Restart the server on SSL error

def start_server(host, port, rsa_certfile, rsa_keyfile, cipher_suite):
    # Create HTTP server
    httpd = http.server.HTTPServer((host, port), SimpleHTTPRequestHandler)
	
    # Create SSL context
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain(certfile=rsa_certfile, keyfile=rsa_keyfile)
    context.set_ciphers(cipher_suite)
	
	# Wrap socket with SSL context
    httpd.socket = context.wrap_socket(httpd.socket, server_side=True)

    # Start serving
    serve_forever_ssl(httpd)

def main():
    # Create HTTP server
    httpd = http.server.HTTPServer(('localhost', 443), SimpleHTTPRequestHandler)
    
    # Create SSL context
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain(certfile='server.crt', keyfile='server.key')
    context.set_ciphers('ECDHE:!aNULL:!eNULL')

    # Wrap socket with SSL context
    httpd.socket = context.wrap_socket(httpd.socket, server_side=True)

    # Start serving
    serve_forever_ssl(httpd)

	
if __name__ == "__main__":
    # HOST = 'autoclient215.autobot.cvp'
    HOST = 'autoclient215'
    PORT = 12345
    RSA_CERTFILE = 'certs/rsa.crt.pem'  # Path to RSA certificate
    RSA_KEYFILE = 'certs/rsa.key.pem'   # Path to RSA private key

    # CIPHER_SUITE = 'AES256-SHA256'  # Example cipher suite, replace with your preferred one
    # CIPHER_SUITE = 'AES256-CBC-SHA'   #'AES256-SHA'
    
    # CIPHER_SUITE = 'RSA-AES256-SHA256'
    # CIPHER_SUITE = 'TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA'  # ECDHE Cipher
    # CIPHER_SUITE = 'TLS_RSA_WITH_AES_256_CBC_SHA'   #RSA Cipher
	
    # CIPHER_SUITE = 'ECDHE:!aNULL:!eNULL'
    CIPHER_SUITE = 'ALL:!ECDHE'

    start_server(HOST, PORT, RSA_CERTFILE, RSA_KEYFILE, CIPHER_SUITE)
