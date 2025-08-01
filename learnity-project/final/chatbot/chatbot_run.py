import os
import threading  # To run commands in parallel
import webview
from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer

def run_ollama_serve():
    """Run the Ollama server in the background."""
    os.system('set OLLAMA_ORIGINS=* && ollama serve')

def run_http_server():
    """Run a simple HTTP server to serve the HTML file."""
    project_root = os.path.dirname(os.path.abspath(__file__))  # Assuming script is in project root
    os.chdir(project_root)
    handler = SimpleHTTPRequestHandler
    with TCPServer(('localhost', 8000), handler) as httpd:
        print("Serving on http://localhost:8000...")
        httpd.serve_forever()

# Start the Ollama server in a separate thread
ollama_thread = threading.Thread(target=run_ollama_serve)
ollama_thread.start()

# Start the HTTP server in a separate thread to serve the HTML
http_server_thread = threading.Thread(target=run_http_server)
http_server_thread.start()

# Give the server a moment to start
import time
time.sleep(1)

# Create the Webview window that points to localhost
window = webview.create_window("Blue Ollama Chatbot", "http://localhost:8000/chatbot_htm.html", width=1080, height=720, resizable=True)

# Start the webview window
webview.start()

# Wait for the threads to finish
ollama_thread.join()
http_server_thread.join()
