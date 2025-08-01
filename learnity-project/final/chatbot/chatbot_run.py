import os
import threading
import webview
import time
from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer

def run_ollama_serve():
    os.system('set OLLAMA_ORIGINS=* && ollama serve')

def run_http_server():
    project_root = os.path.dirname(os.path.abspath(__file__))
    os.chdir(project_root)
    handler = SimpleHTTPRequestHandler
    with TCPServer(('localhost', 8000), handler) as httpd:
        print("Serving on http://localhost:8000...")
        httpd.serve_forever()

ollama_thread = threading.Thread(target=run_ollama_serve)
ollama_thread.start()
http_server_thread = threading.Thread(target=run_http_server)
http_server_thread.start()

time.sleep(1)

window = webview.create_window("Blue Ollama Chatbot", "http://localhost:8000/chatbot_htm.html", width=1080, height=720, resizable=True)
webview.start()
ollama_thread.join()
http_server_thread.join()
