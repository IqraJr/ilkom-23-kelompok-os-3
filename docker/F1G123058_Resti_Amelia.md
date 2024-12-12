LANGKAH-LANGKAH MENJALANKAN DOCKER DI LINUX

# BUAT FOLDER DOCKER:
```bash
$ mkdir os
```
# BERPINDAH KE FOLDER:
```bash
$ cd os
```
# BUAT DOCKERFILE
```bash
$ touch Dockerfile
```
# MENGEDIT ISI DOCKERFILe
```bash
$ nano Dockerfile
```
# ISI DOCKERFILE
```bash
# Menggunakan image Nginx resmi dari Docker Hub
FROM nginx:latest

# Menyalin file HTML ke dalam direktori default Nginx
COPY ./html /usr/share/nginx/html/

# Mengekspos port 80 agar bisa diakses dari luar
EXPOSE 80
```
# BUAT FOLDER TEMPAT HTML
```bash
$ mkdir html
```
# BUAT FILE INDEX DI DALAM FOLDER HTML:
```bash
$ touch html/index.html
```
# MENGEDIT ISI FILE INDEX YANG ADA DI DIDALAM FOLDER HTML:
```bash
$ nano html/index.html
```

# ISI FILE index.html:
```bash
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Selamat Datang di Nginx</title>
</head>
<body>
    <h1>Hello, Docker dan Nginx!</h1>
    <p>Ini adalah halaman HTML sederhana yang dilayani oleh Nginx di dalam Docker container.</p>
</body>
</html>
```

#  BANGUN Docker Image:
```bash
$ docker build -t os-app .
```

# MENJALANKAN KONTAINER:
```bash
$ docker run -d -p 8080:80 os-app
```

# AKSES APLIKASI DI BROWSER
http://localhost:8080/

# MENAMPILKAN CARA RUNNING CONTAINER, STATUS DOCKER TELAH BERJALAN, DAN STOP CONTAINER:
Link gambar : (https://drive.google.com/file/d/1LuSi1LucrpF54qQHF0GKCrSepz9L0O_e/view?usp=drivesdk)


# MENAMPILKAN BUKTI DOCKER BERJALAN
![gambardocker](https://drive.google.com/uc?id=1Ji52vq7cXG__TpfjK7lNqFb2TXhp5hwj)


# MENGHENTIKAN KONTAINER YANG BERJALAN
```bash
$ docker stop 6938e7e61034bd80069b71464194739e5300c22ba19af2576d923bedd5cb2aa5
```
# MELAKUKAN PEMBATASAN MEMORI
```bash
$ docker run -d -p 8080:80--memory=500m os-app
```
# BUKTI STATUS PEMBATASAN MEMORI
Link gambar : (https://drive.google.com/file/d/1LQrsDZ_gxE1_caRxhnYlh-Hqj9o4qhrh/view?usp=drivesdk)
# MELAKUKAN FASE BEDAH CONTAINER
## 1. Command ps aux
Menampilkan semua proses yang sedang berjalan di dalam container. Ini berguna untuk menganalisis aplikasi atau proses yang sedang dijalankan dalam container.
```bash
$ docker exec -it <container_id> ps aux
```
### Bukti Percobaan ps aux
Link gambar : (https://drive.google.com/file/d/1LpFOpT-zx-YFsgPlr7lMR8g1R9hlHgkQ/view?usp=drivesdk)

## 2. Command history
Command ini memberikan informasi rinci tentang container, termasuk konfigurasi jaringan, mounts, environment variables, dan lainnya.
```bash
$ docker history <image_id>
```
## Bukti percobaan history
Link gambar : (https://drive.google.com/file/d/1Lq2e4zrcYOW7wuR4NQqOms_hpgu3gQmG/view?usp=drivesdk)

## 3.Command masuk ke container
Untuk masuk dan melakukan modifikasi file didalam container
```bash
$ docker exec -it <container_id> /bin/bash
```
## Bukti percobaan masuk ke container
Link gambar : (https://drive.google.com/file/d/1LtJI2NTKAFTmNeuxImYGchg9___xm_qp/view?usp=drivesdk)
