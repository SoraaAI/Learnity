import subprocess
import importlib.util
import sys
import os
import importlib
import time

try:
    import webview
except ImportError:
    os.system("pip install pywebview")

def install_dependency(pkg_name, module_name=None):
    if module_name is None:
        module_name = pkg_name
    if importlib.util.find_spec(module_name) is not None:
        return f"✅ {pkg_name} sudah terinstall."
    else:
        os.system(f"pip install {module_name}")
        return f"❌ {pkg_name} belum terinstall, menginstall.."

class API:
    def check_dependicies(self):
        time.sleep(5.0)
        messages = []
        messages.append(install_dependency("google-generativeai", "google.generativeai"))
        messages.append(install_dependency("SpeechRecognition", "speech_recognition"))
        messages.append(install_dependency("pyttsx3"))
        messages.append(install_dependency("pyaudio"))
        messages.append(install_dependency("requests"))
        messages.append(install_dependency("streamlit"))
        messages.append(install_dependency("Pillow", "PIL"))
        messages.append(install_dependency("pywebview", "webview"))
        messages.append(install_dependency("cv2"))
        messages.append(install_dependency("mediapipe"))
        messages.append(install_dependency("pygetwindow"))
        messages.append(install_dependency("pyautogui"))
        return messages

html_path = 'index.html'
api = API()
window = webview.create_window("Learnity Setup",
                               html_path,
                               width=1080,
                               height=720,
                               resizable=True,
                               js_api=api)
webview.start()
