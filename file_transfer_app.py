import http.server
import socketserver
import socket
import os

PORT = 8080
Handler = http.server.SimpleHTTPRequestHandler

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

ip = get_ip()
print(f"=== Minimal File Transfer App ===")
print(f"Sharing files from: {os.getcwd()}")
print(f"Access on other devices via: http://{ip}:{PORT}")
print("Press Ctrl+C to stop.")

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
