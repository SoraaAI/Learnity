import speech_recognition as sr
from googletrans import Translator
import pyttsx3
import threading

recognizer = sr.Recognizer()
translator = Translator()
engine = pyttsx3.init()
stop_flag = False

AUDIO_FILE = "temp.wav"

def record_audio():
    global stop_flag
    with sr.Microphone() as source:
        print("🎙️ Mulai merekam... (Tekan Enter untuk selesai dan mulai menerjemahkan)")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source, phrase_time_limit=None)
        with open(AUDIO_FILE, "wb") as f:
            f.write(audio.get_wav_data())
        print("📁 Audio disimpan. Tunggu enter untuk lanjut.")
        stop_flag = True

def wait_for_enter():
    global stop_flag
    input()
    stop_flag = True

print("🟢 Tekan Enter saat kamu selesai bicara.")
t1 = threading.Thread(target=record_audio)
t2 = threading.Thread(target=wait_for_enter)
t1.start()
t2.start()
t1.join()
t2.join()

try:
    with sr.AudioFile(AUDIO_FILE) as source:
        audio = recognizer.record(source)
        print("🧠 Mendeteksi suara...")
        text = recognizer.recognize_google(audio)
        print(f"🗣️ Teks: {text}")
        translated = translator.translate(text, dest='id')
        print(f"📘 Terjemahan: {translated.text}")
        engine.say(translated.text)
        engine.runAndWait()
except sr.UnknownValueError:
    print("🤔 Tidak bisa mengenali suara.")
except sr.RequestError as e:
    print(f"⚠️ Error API: {e}")
except Exception as e:
    print(f"🚨 Error lain: {e}")