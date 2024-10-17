# CARA MENJALANKAN DAEMON PADA LARAVEL 11

## A. PENDAHULUAN

Daemon adalah proses yang berjalan di latar belakang tanpa interaksi langsung dengan pengguna. Fungsi utama daemon dalam sistem operasi adalah melakukan tugas-tugas otomatis atau layanan yang berkelanjutan. Biasanya daemon diaktifkan saat sistem booting dan terus berjalan tanpa perlu dimulai oleh pengguna.

## B. CARA PEMASANGAN
### 1. Carilah reporsitory github yang akan diclone 
``` 
git clone https://github.com/SirGhazian/website-donasi-laravel.git
```
### 2. Buatlah file dengan nama *laravel-daemon.sh*
Untuk membuat file *laravel-daemon.sh* masukan kode berikut pada kode editor anda
``` 
touch laravel-daemon.sh
```
### 3. Masukan kode berikut kedalam file *laravel-daemon.sh*
```
#!/bin/bash

case "$1" in
    start)
        # Mengecek apakah server sudah berjalan
        if [ -f laravel.pid ]; then
            echo "Server  sekarang sedang berjalan."
            exit 1
        fi

        # Jalankan server dan simpan PID ke file
        nohup php artisan serve > /dev/null 2>&1 &
        echo $! > laravel.pid
        echo "Server berjalan."
        ;;
    stop)
        # Mengecek apakah file PID ada
        if [ -f laravel.pid ]; then
            PID=$(cat laravel.pid)
            kill $PID
            rm laravel.pid
            echo "Server berhenti."
        else
            echo "Tidak ada server yang sedang berjalan."
        fi
        ;;
    *)
        echo "Usage: $0 {start|stop}"
        exit 1
        ;;
esac
```
### 4. Berikan perintah sebagai berikut untuk memberikan izin eksekusi
```
chmod +x laravel-daemon.sh
```
### 5. Cara menjalankan dan Memberhentikan server
#### a. Cara menjalankan server
```
./laravel-daemon.sh start
```
#### b. Cara memhentikan server
```
./laravel-daemon.sh stop
```
### 6. Cara mengakses
Masukan URL berikut ke dalam browser anda
```
http://localhost:8000/
```
## C.SCREENSHOT
![Screenshot 2024-10-18 002510](https://github.com/user-attachments/assets/23d03423-a7b1-4039-82c7-b45be503de74)
![image](https://github.com/user-attachments/assets/1a29d828-8bb5-44dd-b74d-bc4c0355d4f0)

## KESIMPULAN 
Bahwa daemon akan tetap berjalan di latar belakang hingga dihentikan secara manual.Sedangkan Artisan serve akan mati saat terminal ditutup.Dengan demikian  artisan serve lebih cocok untuk lingkungan pengembangan sementara daemon sangat ideal untuk lingkungan produksi yang membutuhkan proses otomatis yang stabil dan berkelanjutan.









