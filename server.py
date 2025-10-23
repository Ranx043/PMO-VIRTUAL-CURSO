#!/usr/bin/env python3
"""
Servidor HTTP simple con soporte CORS para desarrollo local
"""
from http.server import HTTPServer, SimpleHTTPRequestHandler
import sys

class CORSRequestHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        # Agregar headers CORS
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()

    def log_message(self, format, *args):
        # Mejorar formato de logs
        sys.stderr.write("[%s] %s\n" % (self.log_date_time_string(), format % args))

def run(port=8000):
    server_address = ('', port)
    httpd = HTTPServer(server_address, CORSRequestHandler)
    print(f"[OK] Servidor iniciado en http://localhost:{port}")
    print(f"[INFO] Sirviendo archivos desde: {httpd.server_name}")
    print("[INFO] Con soporte CORS habilitado")
    print("\nPresiona Ctrl+C para detener el servidor\n")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n\n[INFO] Servidor detenido")
        sys.exit(0)

if __name__ == '__main__':
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
    run(port)
