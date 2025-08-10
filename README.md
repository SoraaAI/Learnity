# Learnity: Tak Peduli Dimana, Ilmu Mengejarmu, Masa Depan Menunggumu

---

## 📖 Panduan Penggunaan Aplikasi Learnity

Panduan ini membantu Anda memahami fitur-fitur yang tersedia pada aplikasi **Learnity**, mulai dari pengaturan dasar, pengelolaan data, hingga penggunaan fitur canggih seperti AI, voice-to-text, dan penerjemah audio.

---

## ⚙️ Pengaturan Dasar di Sidebar (Fitur Chatbot)

**Fungsi:** Sidebar adalah panel pengaturan utama untuk mengelola interaksi chatbot Learnity. Semua pengaturan ini memengaruhi cara chatbot bekerja dan berinteraksi dengan pengguna.

* **Offline/Online AI** — Pilih penggunaan AI **offline** (tanpa internet, via Ollama) atau **online** (via Gemini). Mode offline cocok untuk menjaga privasi dan menghemat koneksi internet, sementara mode online memungkinkan akses ke kemampuan AI yang lebih luas.
* **Reset Memory** — Menghapus riwayat percakapan agar AI memulai dari awal, berguna jika topik pembicaraan sudah berubah atau ingin menghilangkan konteks lama.
* **Chat History** — Menampilkan daftar riwayat percakapan yang pernah dilakukan dan memuat ulang percakapan tersebut untuk dilanjutkan.

---

## 🌐 Konfigurasi Server

**Fungsi:** Mengubah perangkat Anda menjadi server agar Learnity dapat diakses oleh perangkat lain melalui jaringan lokal.

### HTTP Server Settings

* **Fungsi** — Memungkinkan Anda membuka Learnity di perangkat lain (misalnya ponsel) menggunakan browser.
* **Keunggulan** — Ideal jika perangkat utama adalah laptop/PC, tetapi ingin mengakses aplikasi dari ponsel di jaringan Wi-Fi yang sama.
* **Penggunaan** — Aktifkan fitur server, tentukan **host** dan **port**, lalu gunakan alamat tersebut pada perangkat lain.

---

## 🎙️ Voice to Text

**Fungsi:** Mengubah suara menjadi teks sehingga Anda dapat berinteraksi dengan AI atau membuat catatan hanya dengan berbicara.

* **Penggunaan** — Aktifkan mode voice-to-text di sidebar, izinkan akses mikrofon, lalu mulai berbicara. Teks akan muncul secara otomatis.
* **Manfaat** — Mempercepat input tanpa mengetik, berguna saat tangan sedang sibuk atau ingin menghemat waktu.

---

## 📅 Absensi & 📚 Tugas Sekolah

### 🔓 Login

* **Fungsi** — Mengamankan akses dan mempersonalisasi fitur sesuai peran (siswa/guru).
* **Contoh Akun Siswa** — Username: `Sora`, ID: `123456789`, Password: `123456`
* **Contoh Akun Guru** — Username: `Rika`, ID: `987654321`, Password: `password`

### 🧑‍🎓 Dashboard Siswa

1. **Absensi** — Mencatat kehadiran harian dengan sekali klik.
2. **Tugas** — Melihat daftar tugas, mengumpulkan jawaban, dan mengecek status pengumpulan.

### 👩‍🏫 Dashboard Guru

1. **Data Absensi** — Memantau kehadiran siswa, memfilter tanggal, dan melihat statistik.
2. **Kelola Tugas** — Membuat, mengedit, dan menghapus tugas.
3. **Submission** — Meninjau jawaban siswa dalam bentuk teks atau file.

---

## 🛒 Beli Karakter

**Fungsi:** Memberi motivasi belajar dengan sistem hadiah berupa karakter yang dapat dibeli menggunakan koin.

1. **Masuk** — Gunakan akun yang terdaftar.
2. **Profil Pengguna** — Menampilkan informasi akun dan koin.
3. **Membeli Karakter** — Menggunakan koin untuk membeli karakter baru.
4. **Menggunakan Karakter** — Mengatur karakter aktif sesuai preferensi.

> **Catatan:** Gambar karakter harus tersedia di folder `image/char` agar dapat ditampilkan.

---

## 📸 Analisis Foto

**Fungsi:** Menggunakan AI Gemini untuk memahami isi gambar.

1. **Unggah Gambar** — Format JPG/JPEG/PNG.
2. **Berikan Prompt** — Ajukan pertanyaan atau instruksi untuk gambar tersebut.
3. **Analisis** — AI akan memberikan deskripsi atau jawaban berdasarkan isi gambar.

---

## 🗺️ Planning Quest

**Fungsi:** Membantu perencanaan aktivitas dengan sistem gamifikasi.

* **📋 My Plans** — Mengelola daftar rencana dan menandai quest yang selesai untuk mendapatkan koin.
* **🤖 AI Assistant** — Memberi saran atau membantu membuat rencana melalui AI.
* **➕ Create Plan** — Membuat rencana baru dengan detail seperti judul, deskripsi, prioritas, dan deadline.

**Reward Koin:**

* Prioritas rendah — 🪙 +2 koin
* Prioritas sedang — 🪙 +5 koin
* Prioritas tinggi — 🪙 +8 koin

---

## 🌍 Penerjemah Audio

**Fungsi:** Mengubah ucapan dalam audio menjadi teks, menerjemahkannya, dan menghasilkan kembali dalam bentuk audio.

1. **Pilih Bahasa** — Atur bahasa sumber dan target.
2. **Unggah/Rekam Audio** — Format `.wav` direkomendasikan.
3. **Konversi ke Teks** — AI mengenali ucapan menjadi teks.
4. **Terjemahkan** — Edit teks jika perlu, lalu terjemahkan.
5. **Buat Audio Terjemahan** — Mendengarkan hasil terjemahan dalam bentuk audio.

---

## ✋ Upload File: Manual & Gesture Tracking

### Mode Gestur

* **Fungsi** — Mengunggah/unduh file dengan gerakan tangan melalui webcam.
* **Kontrol** — 1 jari untuk unggah, 3 jari untuk unduh.

### Mode Manual

* Unggah file menggunakan tombol **Upload**.
* Unduh file dengan tombol **Download Files**.

### Server Opsional

* **Fungsi** — Menjalankan server HTTP untuk mengelola file melalui browser di jaringan lokal.

---

Panduan ini mencakup seluruh fitur Learnity beserta penjelasannya, sehingga Anda dapat memanfaatkannya secara maksimal untuk mendukung pembelajaran interaktif.
