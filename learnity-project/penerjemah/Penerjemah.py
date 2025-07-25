import whisper
import threading
import keyboard
import os

stop_flag = False

def listen_for_enter():
    global stop_flag
    keyboard.wait("enter")
    stop_flag = True
    print("\n🔴 Proses dihentikan oleh pengguna.\n")

def transcribe_and_translate(file_path):
    print("🔄 Memuat model Whisper...")
    model = whisper.load_model("base")

    print("🎧 Mendeteksi bahasa dan mentranskrip...")
    result = model.transcribe(file_path, task="translate")

    print("\n🌍 Bahasa Terdeteksi:", result.get("language", "Tidak terdeteksi"))
    print("📝 Terjemahan ke Bahasa Indonesia:\n")
    print(result["text"])

def main():
    global stop_flag
    audio_path = input("Masukkan path ke file audio (.mp3/.wav): ").strip()
    if not os.path.exists(audio_path):
        print("❌ File tidak ditemukan.")
        return
    enter_thread = threading.Thread(target=listen_for_enter, daemon=True)
    enter_thread.start()
    transcribe_and_translate(audio_path)
    while not stop_flag:
        pass

if __name__ == "__main__":
    main()
