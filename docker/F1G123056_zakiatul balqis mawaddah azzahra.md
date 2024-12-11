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
http://localhost:8080

# MENAMPILKAN CARA RUNNING CONTAINER, STATUS DOCKER TELAH BERJALAN, DAN STOP CONTAINER:
![gambardocker] (https://drive.google.com/file/d/1vbabcrSyPvQW466Syh6eB7VMdATivKiA/view?usp=drive_link)

# MENAMPILKAN BUKTI DOCKER BERJALAN
![gambardocker] (https://drive.google.com/file/d/1S5MrX86l2euIf7Cs77enylsV2X1nWZSB/view?usp=drive_link)

# MENGHENTIKAN KONTAINER YANG BERJALAN
```bash
$ docker stop 6938e7e61034bd80069b71464194739e5300c22ba19af2576d923bedd5cb2aa5
```
