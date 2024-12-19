# TUGAS BESAR DOCKER 
## 1. MEMBUAT IMAGES DAN CONTAINER PADA DOCKER  
### MEMBUAT FOLDER DOCKER DENGAN MENGGUNAKAN COMMAND WSL
```bash
$ mkdir docker3
```
### PINDAH KE FOLDER docker3
```bash
$ cd docker3
```
### MEMBUAT FILE DOCKERFILE
```bash
$ touch Dockerfile
```
### MELAKUKAN INPUT KEDALAM FILE DOCKERFILE
```bash
$ nano Dockerfile
```
### ISI PADA FILE Dockerfile
```bash
# Gunakan image PHP resmi
FROM php:8.1-apache

# Install dependencies (misalnya, jika menggunakan ekstensi tertentu)
RUN docker-php-ext-install mysqli pdo pdo_mysql

# Salin file PHP Anda ke dalam kontainer
COPY . /var/www/html/

# Expose port 80
EXPOSE 80
```
### MEMBUAT FILE index.php 
```bash
$ touch index.php
```
### MELAKUKAN INPUT PADA FILE index.php
```bash
$ nano index.php
```
### ISI PADA FILE index.php
```bash
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Anggota Kelompok 3</title>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap" rel="stylesheet">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css" rel="stylesheet">
    <style>
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        body {
            font-family: 'Poppins', sans-serif;
            background-color: #B0D4F1; /* Biru muda */
            color: #2C3E50; /* Biru gelap */
            margin: 0;
            padding: 0;
        }

        header {
            background-color: #003366; /* Biru tua */
            color: #B0D4F1; /* Warna teks */
            text-align: center;
            padding: 40px 20px;
            font-size: 2.2em;
            font-weight: bold; /* Menambah ketebalan teks */
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
            font-family: 'Poppins', sans-serif;
        }

        .container {
            display: flex;
            flex-wrap: wrap;
            justify-content: space-evenly;
            gap: 15px;
            padding: 20px;
            padding-bottom: 50px;
        }

        .member {
            background-color: #4A90E2; /* Biru */
            border-radius: 15px;
            padding: 20px;
            text-align: center;
            flex: 1 1 220px;
            max-width: 250px;
            min-height: 250px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }

        .member:hover {
            transform: translateY(-10px);
            box-shadow: 0 6px 20px rgba(0, 0, 0, 0.2);
        }

        .icon {
            font-size: 40px;
            color: #003366; /* Biru tua */
            margin-bottom: 15px;
        }

        .member h2 {
            color: #FFFFFF; /* Putih */
            font-size: 1.3em;
            margin-bottom: 10px;
            font-weight: 600;
        }

        .member p {
            font-size: 1em;
            color: #F0F8FF; /* Biru sangat terang */
            line-height: 1.3;
        }

        footer {
            background-color: #003366; /* Biru tua */
            color: white;
            text-align: center;
            padding: 10px;
            position: fixed;
            width: 100%;
            bottom: 0;
        }
    </style>
</head>
<body>

<header>
    Anggota Kelompok 3
</header>

<div class="container">
    <!-- Baris pertama: 3 anggota -->
    <div class="member">
        <div class="icon"><i class="fas fa-user-circle"></i></div>
        <h2>Iqra Fauzan Akbar</h2>
        <p>F1G123020</p>
    </div>
    <div class="member">
        <div class="icon"><i class="fas fa-user-circle"></i></div>
        <h2>Zacky Fiqran Kasmada</h2>
        <p>F1G123038</p>
    </div>
    <div class="member">
        <div class="icon"><i class="fas fa-user-circle"></i></div>
        <h2>Resti Amelia</h2>
        <p>F1G123058</p>
    </div>
</div>

<div class="container">
    <!-- Baris kedua: 3 anggota -->
    <div class="member">
        <div class="icon"><i class="fas fa-user-circle"></i></div>
        <h2>Siti Nuraisyah Sea</h2>
        <p>F1G123035</p>
    </div>
    <div class="member">
        <div class="icon"><i class="fas fa-user-circle"></i></div>
        <h2>Della Mustifar</h2>
        <p>F1G123043</p>
    </div>
    <div class="member">
        <div class="icon"><i class="fas fa-user-circle"></i></div>
        <h2>Zakiatul Balqis Mawaddah Azahra</h2>
        <p>F1G123056</p>
    </div>
</div>

<footer>
    <p>&copy; 2024 Kelompok 3</p>
</footer>

</body>
</html>

```

### MEMBUAT FILE docker-compose.yml
```bash
$ touch docker-compose.yml
```
### MELAKUKAN INPUT PADA FILE docker-compose.yml
```bash
$ $ nano docker-compose.yml
```
### ISI FILE docker-compose.yml
```bash
version: '3'
services:
  php:
    build: .
    ports:
      - "8080:80"
    volumes:
      - .:/var/www/html

```
### MELAKUKAN BUILD IMAGE
```bash
$ docker build -t latihandoker .
```

### MENAMPILKAN IMAGE YANG TERSEDIA
```bash
$ docker images
```

### MEMBUAT CONTAINER DENGAN MENGGUNAKAN IMAGES YANG SUDAH KITA BUAT
```bash
$ docker run -d -p 8081:80 dockerkel4
```

### MENGAKSES LOCAL HOST
```bash
http://localhost:8081/
```
![gambar](https://drive.google.com/uc?id=1gn3LnyMsoSGSI_KUx10XlrepYgtD15Am)

### MENGHENTIKAN PROSES DOCKER
```bash
$ docker stop dockerkel4
```

## 2.MELAKUKAN PEMBATASAN MEMORY DAN CPU DALAM CONTAINER 
### PEMBATASAN MEMORY
```bash
$ docker update --memory 500m --memory-swap 600m dockerkel4        
```
#### SEBELUM PEMBATASAN MEMORY
![gambar](https://drive.google.com/uc?id=1A03papVf9t2w2UYU9dLxW33IBxl6PAW-)

#### SESUDAH PEMBATASAN MEMORY
![gambar](https://drive.google.com/uc?id=1L-PKcy_8KmREOk07dybpe4ynPJX3Vad3)

### PEMBATASAN CPU
```bash
$ docker update --cpus=2 dockerkel4
```
#### SEBELUM PEMBATASAN CPU
![gambar](https://drive.google.com/uc?id=1gd42bpttiiy3pdv2UYdSi0GE15G5fKBp)

#### SESUDAH PEMBATASAN CPU
![gambar](https://drive.google.com/uc?id=1y6B9xzKfl1rvAyxy8eXpF-rSimVntwA5)

## 3. MELAKUKAN FASE BEDAH CONTAINER
### masuk ke dalam container 
Sebelum kita melakukan bedah container terlebih dahulu kita akan masuk ke dalam containernya terlebih dahulu dengan command.
```bash
$ docker exec -it dockerkel4 /bin/bash
```
![gambar](https://drive.google.com/uc?id=1M1g0IqKhDg904DFyOwF6JsF3C-oV5Zzw)

Setelah masuk ke dalam container kita akan mencoaba beberapa command dibawah ini
### 1. Command ls -la /
Menampilkan semua file dan folder di root direktori dengan detail.

![gambar](https://drive.google.com/uc?id=1oHQoQ_KUzx2B46dNDMcoP6ckMnBbvewC)

### 2. Command cat /etc/os-release
Menampilkan Informasi OS (contoh: Ubuntu, Debian, dll.)..

![gambar](https://drive.google.com/uc?id=1zEMefVZICUHOjqaq2xBYLqRzNOIaIcrG)

### 3. Command df -h
Menampilkan penggunaan disk dalam format yang mudah dibaca.

![gambar](https://drive.google.com/uc?id=1qM46gXH0Y42u_QL4xmdDkNUxpFkjpjbu)

### 4. Command ps aux
Menampilkan daftar proses yang berjalan di container.

![gambar](https://drive.google.com/uc?id=1POp2lU2nLdEYu18qMjLauXTddLeCea--)

### 5. Command top
Menampilkan tampilan real-time proses aktif.

![gambar](https://drive.google.com/uc?id=1SPEtu5bUEpULJPNNf9I_EQjw7UOe6lJp)

### 6. Command lscpu
Menampilkan detail arsitektur pada cpu.

![gambar](https://drive.google.com/uc?id=1U90V3liMp8mpuMcweFePSA-CEV1z-KgP)

## KELUAR DARI CONTAINER 
```bash
# exit
```
