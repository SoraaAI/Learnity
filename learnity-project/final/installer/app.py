import subprocess
import importlib
import sys
import os
import time
import webview

modules_to_check = [
    ("google-generativeai", "google.generativeai"),
    ("SpeechRecognition", "speech_recognition"),
    ("pyttsx3", "pyttsx3"),
    ("pyaudio", "pyaudio"),
    ("requests", "requests"),
    ("streamlit", "streamlit"),
    ("Pillow", "PIL"),
    ("pywebview", "webview"),
    ("opencv-python", "cv2"),
    ("mediapipe", "mediapipe"),
    ("pygetwindow", "pygetwindow"),
    ("pyautogui", "pyautogui")
]

def install_package(pkg_name):
    os.system(f"pip install {pkg_name}")

def try_import(pkg_name, module_name):
    try:
        importlib.import_module(module_name)
        return f"✅ {pkg_name} sudah terinstall."
    except ImportError:
        install_package(pkg_name)
        return f"❌ {pkg_name} seharusnya baru saja terinstall yaa, boleh tekan tombol Cek dan Install Dependensi sekali lagiy.."

class API:
    def check_dependicies(self):
        time.sleep(5.0)
        messages = []
        for pkg_name, module_name in modules_to_check:
            messages.append(try_import(pkg_name, module_name))
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
