# LANGKAH-LANGKAH PEMBUATAN DAEMON PROCESS

Daemon adalah sebuah proses yang berjalan di latar belakang pada sistem operasi, biasanya tanpa interaksi langsung dengan pengguna. Daemon sering digunakan untuk menjalankan layanan atau tugas yang berkelanjutan seperti server web, pengelolaan log, atau layanan jaringan.

Berikut tahapannya :

## Buat file.service
Buat File .service: Buat file service kosong di direktori /etc/systemd/system/ dengan nama della.service:

```bash
$ sudo touch /etc/systemd/system/della.service
```

touch fungsinya untuk membuat file.service
git 
## Edit File .service
Setelah membuat file, buka file tersebut menggunakan editor teks seperti nano atau vim untuk menambahkan konfigurasi service.

```bash
$ sudo nano /etc/systemd/system/della.service
```
nano fungsinya untuk membuka file.service

## Penulisan script konfigurasi .service

```bash
[Unit]
Description=della daemon

[Service]
User=della
Restart=always
WorkingDirectory=/home/della/venv/tugas
Environment="PYTHONPATH=/home/della/venv/tugas/1lib/python3.12/site-packages"
ExecStart=/home/della/venv/tugas/bin/uvicorn main:app --reload --port 7888

[Install]
WantedBy=multi-user.target
```
## Penjelasan dari setiap bagian

[Unit]

Description: Menyediakan deskripsi singkat tentang unit. Dalam hal ini, ini adalah daemon untuk pengguna "della daemon".

[Service]

User: Menentukan pengguna di mana layanan service akan dijalankan. yaitu "della" ada di sistem.

Restart: Menentukan kebijakan restart. always berarti layanan akan selalu dimulai kembali jika mati.

WorkingDirectory: Menentukan direktori kerja untuk service, yaitu /home/della/venv/tugas

Environment: Menentukan variabel lingkungan. Dalam hal ini, PYTHONPATH diatur untuk memastikan bahwa direktori yang berisi paket Python diambil dengan benar yakni 1lib/python3.12/site-packages

ExecStart: Menentukan perintah untuk menjalankan layanan. Ini menjalankan uvicorn dengan aplikasi yang ditentukan (main:app), dengan opsi untuk memuat ulang secara otomatis dan mendengarkan pada port 7888.

[Install]

WantedBy: Menentukan target di mana unit ini diaktifkan. multi-user,target biasanya digunakan untuk layanan yang berjalan di latar belakang.

## Menjalankan perintah daemon
```bash
$ sudo systemctl daemon-reload
$ sudo systemctl enable della.service
$ sudo systemctl start della.service
$ sudo systemctl status della.service
```
## Bukti Daemon berjalan 


berikut bukti menjalankan daemon process

![gambardaemon](https://github.com/delsskom/bukti-daemon-berjalan/blob/main/bukti%20sc%20menjalankan%20daemon.jpg?raw=true)

bukti website hello word

![gambardaemon](https://github.com/delsskom/bukti-daemon-berjalan/blob/main/Screenshot%202024-10-31%20140020.png?raw=true)

menambahkan gambar pada daemon process

## Menghentikan layanan operasi della.service
```bash
$ sudo systemctl stop della.service
```

fungsinya agar daemon yang berjalan di belakang layar dapat terhenti dengan tujuan menjaga memori agar tidak berkurang