# Apa itu Daemon?

Daemon adalah program komputer yang berjalan di latar belakang, biasanya tanpa interaksi langsung dengan pengguna. Daemon sering digunakan untuk menangani tugas-tugas tertentu, seperti pengelolaan jaringan, penjadwalan tugas, atau mengawasi proses lain. Dalam sistem operasi Unix dan Linux, daemon biasanya memiliki nama yang diawali dengan huruf "d" (misalnya, `httpd` untuk server web). Daemon dapat dimulai secara otomatis saat sistem booting atau dijalankan atas permintaan.

## Ciri-ciri Daemon

1. **Berjalan di Latar Belakang**  
   Daemon tidak menampilkan antarmuka langsung kepada pengguna dan beroperasi di latar belakang.

2. **Memulai Otomatis**  
   Banyak daemon diatur untuk memulai secara otomatis saat sistem boot, sehingga tidak memerlukan interaksi manual untuk memulainya.

3. **Tidak Bergantung pada Terminal**  
   Setelah dijalankan, daemon tidak terikat pada terminal atau sesi pengguna. Ia terus berjalan meskipun terminal yang digunakan untuk menjalankannya ditutup.

4. **Berjalan Lama**  
   Daemon dirancang untuk berjalan dalam waktu yang lama, idealnya sepanjang waktu sistem berjalan, dan hanya dihentikan jika sistem dimatikan atau dengan perintah tertentu.

## Contoh Daemon

- `httpd`: Daemon untuk web server Apache.
- `sshd`: Daemon untuk server SSH yang memungkinkan akses jarak jauh ke sistem.
- `cron`: Daemon yang menjalankan tugas terjadwal di sistem Linux dan Unix.
