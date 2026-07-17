"""Starting point for lichess-bot."""
from lib.lichess_bot import start_program

if __name__ == "__main__":
    start_program()
import http.server
import socketserver
import threading

def run_dummy_server():
    PORT = 10000
    Handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        httpd.serve_forever()

# Pornește serverul web pe un fir de execuție secundar
threading.Thread(target=run_dummy_server, daemon=True).start()
