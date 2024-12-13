# Daemon: Program yang Berjalan di Latar Belakang

**Daemon** adalah program komputer yang berjalan di latar belakang (background) dan tidak terikat dengan antarmuka pengguna (user interface). Daemon biasanya digunakan untuk menangani tugas-tugas yang berjalan secara otomatis atau untuk menyediakan layanan tertentu dalam sistem operasi.

## Ciri-ciri Daemon

### 1. Menjalankan di Background
Daemon tidak memerlukan interaksi langsung dari pengguna dan biasanya dimulai saat sistem booting.

### 2. Layanan Jaringan
Banyak daemon berfungsi sebagai server untuk memberikan layanan jaringan, seperti HTTP server (misalnya Apache), database server, dan lain-lain.

### 3. Manajemen Proses
Daemon dapat mengelola proses lain, seperti monitor sistem, penjadwalan tugas, atau menangani antrian pekerjaan.

### 4. Dinamika
Daemon dapat diaktifkan atau dinonaktifkan sesuai kebutuhan, dan dapat dijadwalkan untuk berjalan pada waktu tertentu.

## Fungsi Utama Daemon

### 1. Menangani Permintaan Jaringan
Banyak daemon bertugas untuk mendengarkan permintaan di jaringan, seperti server web (HTTP daemon) atau server email (SMTP daemon).

### 2. Pekerjaan Berkala
Beberapa daemon menjalankan tugas berkala, seperti cron daemon yang mengatur penjadwalan tugas otomatis pada waktu tertentu.

### 3. Pengelolaan Sumber Daya
Daemon dapat mengelola dan memonitor sumber daya sistem, seperti daemon untuk manajemen sistem file atau pengawasan kinerja.

### 4. Layanan Sistem**
Beberapa daemon memberikan layanan untuk pengguna dan aplikasi lain, seperti database daemon yang mengelola koneksi dan query ke database.

## Contoh Daemon
Beberapa contoh daemon yang umum digunakan di sistem adalah:
- `cron` (untuk menjadwalkan tugas otomatis)
- `sshd` (untuk mengelola koneksi SSH)
- `httpd` (untuk melayani permintaan HTTP)
