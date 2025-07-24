import streamlit as st
import speech_recognition as sr
import tempfile
import os

st.title("🎙️ Speech to Text App")
st.markdown("Upload file audio kamu (.wav) dan aku akan transkrip otomatis pakai Google Speech Recognition API (Bahasa Indonesia).")

# Upload file audio
uploaded_file = st.file_uploader("Upload audio file dibawah satu menit (.wav)", type=["wav"])

if uploaded_file is not None:
    # Simpan file ke temporary location
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp_file:
        tmp_file.write(uploaded_file.read())
        tmp_path = tmp_file.name

    # Mulai proses speech recognition
    r = sr.Recognizer()
    with sr.AudioFile(tmp_path) as source:
        audio_data = r.record(source)

    with st.spinner("Sedang mentranskrip..."):
        try:
            # Transkrip pakai Google Speech Recognition
            hasil = r.recognize_google(audio_data, language="id-ID")
            st.success("Transkripsi selesai!")
            st.text_area("📝 Hasil Transkripsi", value=hasil, height=200)
        except sr.UnknownValueError:
            st.error("Google Speech Recognition tidak dapat memahami audio.")
        except sr.RequestError as e:
            st.error(f"Terjadi error saat meminta ke Google API: {e}")

    # Hapus file temp
    os.remove(tmp_path)
