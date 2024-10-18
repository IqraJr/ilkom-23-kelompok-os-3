# Proses Daemon Menggunakan php

Daemon adalah program yang berjalan di latar belakang dan biasanya berjalan secara terus-menerus tanpa interaksi langsung dengan pengguna. Di PHP, Anda dapat membuat proses daemon untuk melakukan tugas berulang dengan cara menjalankan script secara terus menerus. Berikut ini adalah contoh dasar bagaimana membuat **proses daemon menggunakan PHP**.

## 1. Script PHP untuk Daemon

Berikut adalah contoh script daemon PHP sederhana yang berjalan di latar belakang dan mencatat waktu setiap 5 detik ke file log.

```php
<?php
// File: daemon.php

// Buat fungsi untuk menangani signal dari sistem
function signalHandler($signal) {
    switch($signal) {
        case SIGTERM:
            // Ketika proses dihentikan
            exit;
        case SIGHUP:
            // Ketika proses mendapat permintaan restart
            break;
    }
}

// Menangani signal
pcntl_signal(SIGTERM, "signalHandler");
pcntl_signal(SIGHUP, "signalHandler");

// Ubah proses menjadi daemon (fork)
$pid = pcntl_fork();
if ($pid == -1) {
    // Jika terjadi error saat fork
    die('Could not fork the process');
} elseif ($pid) {
    // Keluar dari proses induk
    exit;
} else {
    // Proses child, lanjutkan sebagai daemon
    // Pisahkan daemon dari terminal
    if (posix_setsid() == -1) {
        die('Could not detach from terminal');
    }

    // Loop daemon untuk melakukan tugas
    while (true) {
        // Tuliskan waktu ke log file
        file_put_contents('/path/to/your/logfile.log', date('Y-m-d H:i:s') . "
", FILE_APPEND);

        // Tunggu 5 detik sebelum mengulang
        sleep(5);

        // Tangani signal
        pcntl_signal_dispatch();
    }
}
?>
```

## Penjelasan Script:

1. **pcntl_fork()**: Memecah proses menjadi dua, induk dan anak. Proses induk segera keluar, sementara proses anak melanjutkan sebagai daemon.
2. **posix_setsid()**: Menjalankan proses anak sebagai "session leader" yang independen dari terminal.
3. **signalHandler()**: Mengelola signal dari sistem seperti SIGTERM (untuk menghentikan daemon dengan aman).
4. **sleep()**: Menghentikan eksekusi sementara (dalam contoh ini 5 detik), sebelum daemon mengulangi tugas.

## 2. Menjalankan Daemon

Jalankan script daemon dari command line:

```bash
php daemon.php
```

## 3. Menghentikan Daemon

Setelah daemon berjalan, Anda dapat menghentikannya dengan menemukan **PID** (Process ID) dari daemon dan mengirimkan sinyal `SIGTERM`. Misalnya:

```bash
ps aux | grep daemon.php
kill -SIGTERM <PID>
```

## Catatan Penting:

- Pastikan script daemon Anda tidak memakan banyak sumber daya dan mengelola pekerjaan dengan baik.
- Gunakan `sleep()` untuk menghindari penggunaan CPU yang berlebihan dalam loop tak terbatas.
- Daemon harus berjalan di latar belakang, pastikan Anda mencatat error atau aktivitas ke log file untuk memantau status daemon.

Dengan demikian, daemon PHP ini bisa berjalan di background untuk melakukan tugas otomatis seperti pencatatan, memeriksa status layanan, atau tugas berulang lainnya.
