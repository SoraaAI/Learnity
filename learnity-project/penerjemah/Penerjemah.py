import speech_recognition as sr
from googletrans import Translator
import pyttsx3

recognizer = sr.Recognizer()
translator = Translator()
engine = pyttsx3.init()

with sr.Microphone() as source:
    print("🎙️ Silakan bicara...")
    recognizer.adjust_for_ambient_noise(source)
    audio = recognizer.listen(source)

try:
    text = recognizer.recognize_google(audio, language='id-ID')
    print(f"Kamu bilang: {text}")
    translated = translator.translate(text, dest='en')
    print(f"Terjemahan: {translated.text}")
    engine.say(translated.text)
    engine.runAndWait()

except sr.UnknownValueError:
    print("Gagal mengenali suara.")
except sr.RequestError as e:
    print(f"Gagal request ke Google API: {e}")
