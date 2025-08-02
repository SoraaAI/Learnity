import os
import threading
import webview
import time
import json
from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer

class Api:
    def __init__(self):
        self.script_dir = os.path.dirname(os.path.abspath(__file__))
        self.database_dir = os.path.join(self.script_dir, 'database')
        self.chat_history_path = os.path.join(self.database_dir, 'chat_history.json')
        os.makedirs(self.database_dir, exist_ok=True)
        if not os.path.exists(self.chat_history_path):
            with open(self.chat_history_path, 'w', encoding='utf-8') as f:
                json.dump([], f)
            print(f"Created new chat history file: {self.chat_history_path}")
    
    def read_chat_history(self):
        try:
            if os.path.exists(self.chat_history_path):
                with open(self.chat_history_path, 'r', encoding='utf-8') as f:
                    data = f.read().strip()
                    if data:
                        json.loads(data)
                        print(f"Chat history read from: {self.chat_history_path}")
                        return data
                    else:
                        return "[]"
            else:
                return "[]"
        except Exception as e:
            print(f"Error reading chat history: {e}")
            return "[]"
    
    def write_chat_history(self, data):
        try:
            parsed_data = json.loads(data)
            with open(self.chat_history_path, 'w', encoding='utf-8') as f:
                f.write(data)
            
            print(f"Chat history saved to: {self.chat_history_path}")
            print(f"Saved {len(parsed_data)} chat(s)")
            return {"success": True, "message": f"Chat history saved successfully ({len(parsed_data)} chats)"}
        except json.JSONDecodeError as e:
            error_msg = f"Invalid JSON data: {e}"
            print(f"Error saving chat history: {error_msg}")
            return {"success": False, "message": error_msg}
        except Exception as e:
            error_msg = str(e)
            print(f"Error saving chat history: {error_msg}")
            return {"success": False, "message": error_msg}
    
    def get_chat_stats(self):
        try:
            history_data = self.read_chat_history()
            chat_history = json.loads(history_data)
            
            stats = {
                "total_chats": len(chat_history),
                "online_chats": len([chat for chat in chat_history if chat.get('mode') == 'online']),
                "offline_chats": len([chat for chat in chat_history if chat.get('mode') == 'offline']),
                "file_path": self.chat_history_path,
                "file_exists": os.path.exists(self.chat_history_path)
            }
            
            if chat_history:
                timestamps = [chat.get('timestamp') for chat in chat_history if chat.get('timestamp')]
                if timestamps:
                    stats["oldest_chat"] = min(timestamps)
                    stats["newest_chat"] = max(timestamps)
            
            return {"success": True, "stats": stats}
        except Exception as e:
            return {"success": False, "message": str(e)}

def run_ollama_serve():
    print("Starting Ollama server with CORS enabled...")
    os.system('set OLLAMA_ORIGINS=* && ollama serve')

def run_http_server():
    project_root = os.path.dirname(os.path.abspath(__file__))
    os.chdir(project_root)
    print(f"Starting HTTP server from: {project_root}")
    handler = SimpleHTTPRequestHandler
    with TCPServer(('localhost', 8000), handler) as httpd:
        print("HTTP Server running on http://localhost:8000...")
        httpd.serve_forever()

def main():
    print("🚀 Starting Blue Ollama Chatbot...")
    print("📁 Project structure:")
    print("   final/")
    print("   ├── chatbot/ (HTML & Python script)")
    print("   └── database/ (JSON files)")
    
    api = Api()
    
    stats_result = api.get_chat_stats()
    if stats_result["success"]:
        stats = stats_result["stats"]
        print(f"\n📊 Chat History Stats:")
        print(f"   • Total chats: {stats['total_chats']}")
        print(f"   • Online chats: {stats['online_chats']}")
        print(f"   • Offline chats: {stats['offline_chats']}")
        print(f"   • File exists: {stats['file_exists']}")
        print(f"   • File path: {stats['file_path']}")
    
    print("\n🦙 Starting Ollama server...")
    ollama_thread = threading.Thread(target=run_ollama_serve, daemon=True)
    ollama_thread.start()
    
    print("🌐 Starting HTTP server...")
    http_server_thread = threading.Thread(target=run_http_server, daemon=True)
    http_server_thread.start()
    
    time.sleep(2)
    
    print("🖥️  Creating application window...")
    window = webview.create_window(
        "Blue Ollama Chatbot", 
        "http://localhost:8000/chatbot.html", 
        width=1200,
        height=720, 
        resizable=True, 
        js_api=api
    )
    
    print("✅ All systems ready! Opening chatbot...")
    print("\n💡 Usage Tips:")
    print("   • Toggle between Online (Gemini) and Offline (Ollama) modes")
    print("   • Click 'History' to view and load previous chats")
    print("   • Chat history is automatically saved to database/chat_history.json")
    print("   • Click 'New Chat' to start fresh conversations")
    
    webview.start()

if __name__ == "__main__":
    main()