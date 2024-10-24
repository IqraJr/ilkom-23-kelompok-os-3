# Proses Menjalankan Website Daftar Hadir dengan Daemon Process menggunakan Laragon

## 1. Pendahuluan
Pada tugas ini kita akan membuat sebuah **daemon process** yang berfungsi menangani tugas-tugas yang  akan berjalan di latar belakang, contohnya pemrosesan sebuah data otomatis tanpa interaksi langsung pengguna. Daemon process ini dapat membantu dalam pengelolahan antrian kehadiran, memprosesnya secara otomatis setiap beberapa detik. Pengembangan akan menggunakan **Laragon** sebagai server lokal, dan daemon akan diimplementasikan menggunakan **NSSM** agar dapat berjalan terus-menerus sebagai service di Windows.

## 2. Persiapan
Sebelum memulai daemon process, siapakan software yang diperlukan seperti:
- **Laragon** sebagai server lokal
- **NSSM** (Non-Sucking Service Manager) sebagai tool untuk menjalankan PHP sebagai service di Windows

### 2.1. Instalasi Laragon
1. pertama Unduh dan instal **Laragon** dari [laragon.org](https://laragon.org/download).
2. kemudian jalankan Laragon dan pastikan layanan Apache dan MySQL aktif.

### 2.2. Instalasi NSSM
1. Unduh **NSSM** dari situs resminya [nssm.cc](https://nssm.cc/download).
2. Ekstrak file ke direktori seperti `D:\nssm`.
3. Gunakan NSSM untuk menjalankan file PHP daemon sebagai service.


## 3. Struktur Proyek
buat folder dengan struktur folder proyek Anda sebagai berikut:
```
C:\laragon\www\tugas-daemon
├── daemon.php
├── index.php
├── visitors.txt
├── stats.json
└── daemon.log
```

## 4. Membuat Website
Saya menggambil contoh website dengan menggunakan php,  kasus yang saya ambil merupakan **Website Penghitung Jumlah Pengunjung (Visitor Notification System)**
Dalam file `index.php`, tuliskan isi program untuk sebagai tampilan dari website. Berikut adalah contoh kode:

```php
<?php
// index.php
class NotificationManager {
    private $visitorFile;
    private $logFile;

    public function __construct() {
        $this->visitorFile = __DIR__ . '/visitors.txt';
        $this->logFile = __DIR__ . '/daemon.log';

        // Buat file pengunjung jika belum ada
        if (!file_exists($this->visitorFile)) {
            file_put_contents($this->visitorFile, '0');
        }
    }

    public function incrementVisitor() {
        $count = (int)file_get_contents($this->visitorFile);
        $count++;
        file_put_contents($this->visitorFile, $count);
        return $count;
    }

    public function getLogs($lines = 10) {
        if (file_exists($this->logFile)) {
            $logs = file($this->logFile);
            return array_slice($logs, -$lines);
        }
        return [];
    }
}

// Inisialisasi manajer notifikasi
$manager = new NotificationManager();
$visitorCount = $manager->incrementVisitor();
?>

<!DOCTYPE html>
<html>
<head>
    <title>Visitor Notification System</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; background: #f5f5f5; }
        .container { max-width: 800px; margin: 0 auto; background: white; padding: 20px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
        .logs { background: #f8f8f8; padding: 15px; border-radius: 4px; margin-top: 20px; font-family: monospace; }
    </style>
</head>
<body>
    <div class="container">
        <h1>Visitor Notification System</h1>
        <p>Jumlah Pengunjung: <strong><?php echo $visitorCount; ?></strong></p>

        <div class="logs">
            <h2>System Logs</h2>
            <pre><?php
            foreach($manager->getLogs() as $log) {
                echo htmlspecialchars($log);
            }
            ?></pre>
        </div>
    </div>
</body>
</html>
```

## 5. Membuat Daemon Process
 file `daemon.php`, tuliskan logika untuk mengelola statistik pengunjung dan mencatat aktivitas. 

```php
<?php
class NotificationDaemon {
    private $logFile;
    private $isRunning;

    public function __construct() {
        $this->logFile = __DIR__ . '/daemon.log';
        $this->isRunning = true;
    }

    public function writeLog($message) {
        $timestamp = date('Y-m-d H:i:s');
        file_put_contents($this->logFile, "[$timestamp] $message\n", FILE_APPEND);
    }

    public function sendEmailNotification($visitorCount) {
        // Simulasi pengiriman email
        $to = 'user@example.com';
        $subject = 'New Visitor Alert';
        $message = "There is a new visitor! Total visitors: $visitorCount";
        // Uncomment the line below to send an actual email
        // mail($to, $subject, $message);
        $this->writeLog("Email sent to $to - Total visitors: $visitorCount");
    }

    public function start() {
        $this->writeLog("Notification daemon started");

        $lastCount = 0;

        while ($this->isRunning) {
            if (file_exists(__DIR__ . '/visitors.txt')) {
                $currentVisitors = (int)file_get_contents(__DIR__ . '/visitors.txt');
                
                // Kirim email jika ada pengunjung baru
                if ($currentVisitors > $lastCount) {
                    $this->sendEmailNotification($currentVisitors);
                    $lastCount = $currentVisitors;
                }
            }
            sleep(10); // Cek setiap 10 detik

            if (file_exists(__DIR__ . '/stop.flag')) {
                $this->isRunning = false;
                unlink(__DIR__ . '/stop.flag');
                $this->writeLog("Daemon stopped");
            }
        }
    }
}

// Jalankan daemon
$daemon = new NotificationDaemon();
$daemon->start();
?>

```

## 6. Menjalankan Daemon Process
1. Buka command line di Laragon dan Aktifkan largon.
2. Arahkan ke direktori proyek Anda:
   ```bash
   C:\laragon\www\tugas-daemon
   ```
3. Jalankan daemon process dengan perintah:
   ```bash
   php daemon.php
   ```
4. Pastikan daemon process berjalan di latar belakang dan memperbarui statistik secara otomatis.

## 7. Memantau Statistik dan Log
Data pengunjung dan statistik akan disimpan di `visitors.txt` dan `stats.json`, sedangkan log aktivitas daemon akan disimpan di `daemon.log`. Anda bisa membuka file ini untuk melihat pesan terkait aktivitas yang telah dilakukan oleh daemon process.

## 8. Bukti Screenshoot Program Berhasil Berjalan

## Tampilan Website
![Bukti Screenshoot ketika masih 13](https://drive.google.com/file/d/16eXLSbnKEdc7A8_D8WVMSUpXJv5SGjke/view?usp=drive_link)
## Tampilan Website Berhasil Menghitung Pengunjung
![Bukti Screenshootketika telah di tambah](https://drive.google.com/file/d/1tMV8lcRMG5MLxINXZimYkhrS6aQpeQIV/view?usp=drive_link)
## Daemon Process Berhasil Menampilkan Log Aktivitas
![Bukti Screenshoot](https://drive.google.com/file/d/1qSE2_93uhLNhC0JMCT2r88RKb87H3SEa/view?usp=drive_link)
