Learnity: Tak Peduli Dimana, Ilmu Mengejarmu, Masa Depan Menunggumu.

---

## Panduan Menggunakan Fitur Chatbot Learnity

### Pengaturan Dasar di Sidebar

Di sisi kanan (sidebar), terdapat beberapa pilihan pengaturan untuk menyesuaikan pengalaman Anda:

* **Offline/Online AI**: Anda dapat mengatur apakah ingin menggunakan AI secara **offline** atau **online**. Ini memberikan fleksibilitas dalam penggunaan, terutama jika Anda tidak selalu terhubung ke internet.
* **Reset Memory**: Tombol ini berfungsi untuk **memulai percakapan baru** dengan AI Learnity. Semua riwayat chat sebelumnya akan dihapus dari memori untuk sesi baru.
* **Chat History**: Fitur ini memungkinkan Anda untuk **melihat riwayat percakapan** yang pernah Anda lakukan. Anda bisa memilih indeks riwayat mana yang ingin Anda lanjutkan.

---

### Konfigurasi Server

* **HTTP Server Settings**: Pengaturan ini sangat berguna jika Anda ingin menjadikan perangkat Anda sebagai server.
    * **Fungsi dan Tujuan**: Mengatur perangkat Anda agar perangkat lain dapat mengakses Learnity melalui jaringan yang sama.
    * **Keunggulan**: Meskipun Learnity tidak dapat berjalan secara langsung di perangkat seluler seperti Android, Anda bisa menjalankannya di laptop atau komputer. Lalu, dengan mengaktifkan fitur ini, Anda bisa mengakses Learnity dari ponsel Anda melalui tautan localhost yang sama, selama kedua perangkat terhubung ke jaringan yang sama (misalnya, Wi-Fi yang sama).

---

### Fitur Voice to Text

* **Fungsi**: Fitur ini memungkinkan Anda mengubah ucapan Anda menjadi teks.
* **Cara Menggunakan**: Cukup tekan tombol **konfigurasi 'Voice to Text'** di sidebar. Deskripsi lengkap mengenai cara penggunaannya sudah tersedia di tab yang sama.

Dengan panduan ini, Anda bisa menggunakan fitur Chatbot di Learnity dengan lebih mudah dan maksimal.

---

### Mengelola Absensi Dan Tugas Sekolah Secara Sederhana.

1.  **Buka Sidebar**: Sidebar dapat dibuka dengan mengklik tombol `>` di sudut kiri atas layar.
2.  **Konfigurasi Server Flask**: Di bagian "⚙️ **Flask Configuration**", Anda bisa menyesuaikan pengaturan server seperti **Host**, **Port**, dan **Max File Size**.
3.  **Mulai Server Flask**: Klik tombol **"🚀 Start Flask"**. Sebuah pesan sukses akan muncul, dan status server akan berubah menjadi `🟢 Running`.

---

### 🔐 Login

Setelah server Flask berjalan, Anda bisa masuk ke dalam sistem.

1.  **Isi Formulir Login**: Di bagian "🔐 **Login**" pada sidebar, masukkan **Username atau User ID** dan **Password** Anda.
    * **Contoh Akun Siswa**:
        * **Username**: `Sora`
        * **User ID**: `123456789`
        * **Password**: `123456`
    * **Contoh Akun Guru**:
        * **Username**: `Rika`
        * **User ID**: `987654321`
        * **Password**: `password`
2.  **Klik `Login`**: Setelah berhasil, dashboard akan muncul sesuai dengan peran pengguna (siswa atau guru).
3.  **Logout**: Jika Anda ingin keluar, klik tombol **"Logout"** di sidebar.

---

### 🧑‍🎓 Dashboard Siswa

Sebagai siswa, Anda akan memiliki dua tab utama:

#### 1. 📝 Tab "Absensi"

* **Absen Hari Ini**: Untuk mencatat kehadiran, klik tombol **"✅ Absen Sekarang"**. Anda hanya dapat absen satu kali sehari.
* **Riwayat Absensi**: Di sampingnya, Anda dapat melihat daftar riwayat absensi Anda.

#### 2. 📋 Tab "Tugas"

* **Daftar Tugas**: Semua tugas yang diberikan oleh guru akan ditampilkan di sini.
* **Mengumpulkan Tugas**:
    1.  Klik pada tugas untuk membukanya.
    2.  Isi kotak teks **"Jawaban Tugas:"**.
    3.  (Opsional) Unggah file dengan tombol **"Upload File"**.
    4.  Klik tombol **"Kumpulkan Tugas"** untuk mengirimkan jawaban Anda.
* **Status Tugas**: Anda akan melihat status `✅ Sudah dikumpulkan` atau `⏳ Belum dikumpulkan` pada setiap tugas.

---

### 👩‍🏫 Dashboard Guru

Sebagai guru, Anda akan memiliki tiga tab utama untuk mengelola kelas Anda.

#### 1. 👥 Tab "Data Absensi"

* **Data Absensi Siswa**: Anda bisa melihat semua data absensi siswa.
* **Filter Tanggal**: Gunakan `Filter Tanggal` untuk melihat absensi pada tanggal tertentu.
* **Statistik Absensi**: Lihat ringkasan data absensi seperti total absensi, jumlah siswa aktif, dan absensi hari ini.

#### 2. 📝 Tab "Kelola Tugas"

* **Tambah Tugas Baru**:
    1.  Buka bagian **"➕ Tambah Tugas Baru"**.
    2.  Isi **Judul Tugas**, **Deskripsi**, dan **Deadline**.
    3.  Klik **"Tambah Tugas"** untuk membuat tugas baru.
* **Daftar Tugas**: Semua tugas yang telah Anda buat akan muncul di bagian ini. Anda bisa melihat deskripsi, deadline, dan jumlah siswa yang sudah mengumpulkan.

#### 3. 📊 Tab "Submission"

* **Submission Tugas**: Anda bisa melihat semua jawaban yang telah dikumpulkan siswa untuk setiap tugas.
* **Detail Submission**: Setiap submission akan menampilkan nama siswa, waktu pengumpulan, jawaban teks, dan nama file yang dilampirkan (jika ada).

---

### 🎭Beli Karakter

Aplikasi ini menggunakan sistem koin untuk membeli karakter baru. Setiap karakter memiliki harga yang berbeda. Karakter yang sudah dibeli dapat Anda gunakan sebagai karakter aktif.

#### 1. Masuk ke Aplikasi

Halaman utama aplikasi adalah halaman login. Untuk memulai, Anda harus masuk dengan salah satu akun yang ada di database.

* **Masukkan kredensial**: Gunakan `Username` atau `User ID` dan `Password` yang valid dari file `database/user_data.json`.
    * **Contoh Akun**: `Sora` dengan `password` `123456`.
* **Klik `Login`**: Setelah berhasil, Anda akan diarahkan ke halaman utama toko karakter.

#### 2. Menjelajahi Dashboard & Profil Pengguna

Di halaman utama, Anda akan melihat dua bagian utama: toko karakter dan profil pengguna.

* **Profil Pengguna (Sidebar)**: Di sisi kiri, Anda akan menemukan sidebar yang menampilkan informasi akun Anda.
    * **Username**: Nama pengguna Anda.
    * **User ID**: ID unik Anda.
    * **Role**: Peran Anda dalam sistem (siswa atau guru).
    * **Coins**: Jumlah koin yang Anda miliki saat ini.
    * **Current Character**: Karakter yang sedang Anda gunakan.
* **Toko Karakter**: Bagian utama di sisi kanan menampilkan semua karakter yang tersedia untuk dibeli.
    * Setiap karakter ditampilkan dengan nama, gambar (jika tersedia), dan harga dalam koin.
    * Anda dapat melihat karakter mana yang sudah Anda miliki atau sedang Anda gunakan.

#### 3. Membeli & Menggunakan Karakter

Anda dapat membeli karakter baru jika koin Anda mencukupi, atau mengganti karakter yang sedang Anda gunakan dengan yang sudah Anda miliki.

* **Membeli Karakter**:
    1.  Cari karakter yang Anda suka di toko.
    2.  Jika Anda memiliki cukup koin, tombol **`Buy [Nama Karakter]`** akan muncul.
    3.  Klik tombol tersebut untuk membeli karakter. Koin Anda akan berkurang dan karakter akan ditambahkan ke koleksi Anda.
* **Menggunakan Karakter**:
    1.  Jika Anda sudah memiliki karakter, tombol **`Use [Nama Karakter]`** akan muncul.
    2.  Klik tombol ini untuk menjadikan karakter tersebut sebagai karakter aktif Anda.
    3.  Setelah karakter berhasil diganti, status **`✅ Currently Using`** akan muncul di bawah gambar karakter tersebut.

---

### 📝 Catatan Penting

* **Gambar Karakter**: Gambar karakter diambil dari folder `image/char`. Pastikan file gambar seperti `ISFJ_char.png` dan lainnya tersedia di folder tersebut untuk ditampilkan. Jika tidak, akan muncul placeholder.
* **Data Pengguna**: Semua data, termasuk koin dan karakter yang dimiliki, disimpan dalam file `database/user_data.json`. Perubahan apa pun yang Anda buat dalam aplikasi akan memperbarui file ini secara langsung.
* **Logout**: Untuk keluar dari akun Anda, cukup klik tombol **`Logout`** di sidebar.

-----

### 📸 Analisis Foto

1.  **Unggah Gambar**:

      * Klik tombol **"Pilih sebuah gambar..."**.
      * Pilih file gambar dari komputer Anda dengan format **JPG**, **JPEG**, atau **PNG**.
      * Gambar yang Anda unggah akan langsung ditampilkan di bawah tombol.

2.  **Berikan Prompt**:

      * Di kotak teks **"Berikan prompt atau pertanyaan Anda tentang gambar ini:"**, tuliskan pertanyaan atau perintah yang Anda inginkan.
      * **Contoh prompt**:
          * "Jelaskan apa yang terjadi dalam gambar ini."
          * "Apa saja objek yang terlihat di foto ini?"
          * "Apakah gambar ini menunjukkan pemandangan siang atau malam?"
          * "Berikan deskripsi kreatif untuk gambar ini."

-----

#### 3\. Menganalisis Gambar

1.  **Klik Tombol**: Klik tombol **"Analisis Gambar"** untuk mengirimkan gambar dan prompt Anda ke model Gemini.
2.  **Proses Analisis**: Aplikasi akan menampilkan status **"Sedang menganalisis gambar dengan Gemini..."** saat menunggu respons.
3.  **Lihat Hasil**: Setelah proses selesai, hasilnya akan ditampilkan di bagian **"Hasil Analisis Gemini"**. Anda akan melihat teks yang berisi jawaban atau deskripsi dari AI Gemini berdasarkan prompt yang Anda berikan.

---

### 🚀 Planning Quest

#### 1. Dashboard Utama
* **`📋 My Plans`**: Di sini Anda bisa melihat, mengedit, dan menghapus semua rencana quest yang telah Anda buat. Anda juga dapat menandai item quest sebagai selesai untuk mendapatkan koin.
* **`🤖 AI Assistant`**: Tab ini adalah antarmuka untuk berinteraksi dengan asisten AI.
* **`➕ Create Plan`**: Gunakan tab ini untuk membuat rencana quest baru dengan detail yang spesifik.

#### 2. Mengelola Rencana Quest
Di tab **`📋 My Plans`**, Anda dapat melihat daftar rencana yang sudah dibuat.
* **Lihat Detail**: Setiap rencana dapat diperluas untuk melihat deskripsi, tanggal dibuat, tenggat waktu, dan item-item quest di dalamnya.
* **Selesaikan Quest**: Untuk setiap item quest, ada tombol **`Complete`**. Setelah Anda menyelesaikannya, klik tombol ini untuk menandainya sebagai selesai dan secara otomatis mendapatkan **koin** sebagai hadiah.
    * **Prioritas Rendah**: 🪙 +2 koin
    * **Prioritas Sedang**: 🪙 +5 koin
    * **Prioritas Tinggi**: 🪙 +8 koin
* **Hapus Rencana**: Jika Anda ingin menghapus seluruh rencana, gunakan tombol **`🗑️ Delete Plan`**.

#### 3. Berinteraksi dengan AI Assistant
Di tab **`🤖 AI Assistant`**, Anda dapat mengobrol dengan asisten AI.

* **Pilih Mode AI**: Di sidebar, Anda dapat memilih antara dua mode:
    * **Offline**: Menggunakan model AI lokal (Ollama) yang berjalan di komputer Anda. Ini tidak memerlukan koneksi internet, tetapi Anda harus sudah menginstal dan menjalankan Ollama.
    * **Online**: Menggunakan model AI Gemini dari Google. Ini memerlukan koneksi internet dan kunci API Gemini yang valid.
* **Mulai Obrolan**: Tuliskan pertanyaan atau prompt Anda di kotak chat dan tekan Enter. Asisten AI akan merespons pertanyaan Anda.

#### 4. Membuat Rencana Quest Baru
Di tab **`➕ Create Plan`**, Anda bisa membuat rencana baru dari awal.

* **Tambahkan Item Quest**: Anda dapat menambahkan beberapa item quest ke dalam satu rencana. Setiap item quest memiliki judul dan tenggat waktunya sendiri.
* **Isi Detail Rencana**:
    * **Plan Title**: Beri nama rencana Anda (contoh: "Belajar Bahasa Inggris").
    * **Plan Description**: Deskripsikan tujuan besar dari rencana Anda.
    * **Priority Level**: Tetapkan prioritas (**low**, **medium**, atau **high**).
    * **Plan Deadline**: Tentukan tanggal batas waktu untuk keseluruhan rencana.
* **Simpan Rencana**: Klik tombol **`🎯 Create Plan`** untuk menyimpan rencana baru Anda.

---

### 🎙️ Penerjemah Audio

Learnity memproses file audio Anda melalui tiga langkah utama: pengenalan ucapan, terjemahan, dan sintesis ucapan.

#### 1. Pengaturan Awal (Sidebar)
Sebelum memulai, gunakan sidebar di sisi kiri untuk mengatur preferensi Anda:
1.  **Pilih Bahasa Sumber**: Di bagian "**Dari Bahasa:**", pilih bahasa yang diucapkan dalam file audio yang akan Anda unggah.
2.  **Pilih Bahasa Target**: Di bagian "**Ke Bahasa:**", pilih bahasa yang Anda inginkan untuk terjemahan.
3.  **Pengaturan Audio (Opsional)**: Anda dapat mencentang kotak **"Putar TTS dengan Lambat"** jika Anda ingin audio terjemahan dimainkan dengan tempo yang lebih lambat.

---

#### 2. Unggah dan Konversi Audio
Di bagian utama aplikasi, Anda memiliki dua opsi untuk menginput audio.
1.  **Opsi 1: Rekam Audio**
    * Aplikasi ini memberikan instruksi untuk merekam audio menggunakan fitur bawaan browser atau perangkat Anda.
    * Setelah merekam, simpan file audio tersebut ke komputer Anda.
    * Lanjutkan ke **Opsi 2** untuk mengunggah file yang telah Anda rekam.
2.  **Opsi 2: Unggah File Audio**
    * Klik tombol "**📁 Unggah file audio**" untuk memilih file audio (format **.wav** direkomendasikan) dari komputer Anda.
    * Setelah mengunggah, Anda akan melihat pemutar audio.
    * Klik tombol **"🔄 Konversi Ucapan ke Teks"**. Aplikasi akan memproses audio Anda dan mengekstrak teks.
    * Tunggu hingga pesan **"✅ Teks berhasil diekstrak!"** muncul. Jika ada masalah, Anda akan melihat pesan kesalahan yang menunjukkan penyebabnya.

---

#### 3. Terjemahkan Teks
Setelah audio berhasil dikonversi menjadi teks, Anda akan pindah ke langkah berikutnya.
1.  **Tinjau dan Edit Teks Asli**: Di bagian **"Teks yang Diekstrak"**, Anda dapat melihat teks yang dihasilkan. Jika ada kesalahan, Anda bisa mengeditnya langsung di kotak teks yang tersedia.
2.  **Terjemahkan**: Setelah teks asli sesuai, klik tombol **"🔄 Terjemahkan Teks"**. Aplikasi akan menggunakan Google Translate untuk menerjemahkan teks tersebut ke bahasa target yang Anda pilih.
3.  **Lihat Hasil Terjemahan**: Teks terjemahan akan muncul di bagian **"Terjemahan"**.

---

#### 4. Buat dan Unduh Audio Terjemahan (Opsional)
Jika Anda ingin mendengarkan terjemahan dalam bentuk audio:
1.  **Buat Ucapan**: Klik tombol **"🗣️ Buat Ucapan"**. Aplikasi akan mensintesis ucapan dari teks terjemahan.
2.  **Dengarkan dan Unduh**: Sebuah pemutar audio akan muncul, memungkinkan Anda untuk mendengarkan hasil terjemahan. Anda juga dapat menggunakan tombol **"📥 Unduh Audio Terjemahan"** untuk menyimpan file MP3 tersebut ke komputer Anda.

---

#### 5. Ringkasan dan Reset
Di bagian bawah aplikasi, ada bagian "**Ringkasan Hasil**" yang menampilkan teks asli dan terjemahan secara berdampingan. Jika Anda ingin memulai dari awal, klik tombol **"🗑️ Hapus Semua Hasil"** untuk mereset seluruh aplikasi.
