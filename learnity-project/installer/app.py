import webview
import subprocess
import importlib.util
import sys
import os

# Fungsi utilitas untuk install dependensi
def install_dependency(pkg_name, module_name=None):
    if module_name is None:
        module_name = pkg_name
    if importlib.util.find_spec(module_name) is None:
        subprocess.run([sys.executable, "-m", "pip", "install", pkg_name])
        return f"✅ {pkg_name} berhasil di-install."
    else:
        return f"✅ {pkg_name} sudah terinstall."

# API yang dipanggil dari frontend
class API:
    def check_dependicies(self):
        messages = []
        messages.append(install_dependency("google.generativeai"))
        messages.append(install_dependency("speech_recognition"))
        messages.append(install_dependency("speechrecognition"))
        messages.append(install_dependency("pyttsx3"))
        messages.append(install_dependency("pyaudio"))
        messages.append(install_dependency("requests"))
        messages.append(install_dependency("streamlit"))
        messages.append(install_dependency("Pillow", "PIL"))
        messages.append(install_dependency("PyWebview"))
        return messages

# Jalankan PyWebView
html_path = os.path.abspath("index.html")
api = API()
window = webview.create_window("Learnity Setup",
                               html_path,
                               width=1080,
                               height=720,
                               resizable=True,
                               js_api=api)
webview.start()
