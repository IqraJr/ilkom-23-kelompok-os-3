# LANGKAH-LANGKAH MENJALANKAN DOCKER DAN MEMBUAT IMAGE DOCKER

1. **Buat Folder Docker**
   Buat folder bernama `docker` di direktori dengan terdapat file Docker di dalamnya serta file yang ingin dijalankan. Pada contoh ini, saya menggunakan file HTML sebagai contoh.

2. **Membuat Docker File**

   ```dockerfile
   FROM caddy:latest

   # Salin seluruh file index.html ke dalam folder caddy
   COPY ./index.html /usr/share/caddy/
   ```

   - `FROM`: Instruksi pertama untuk membuat Dockerfile yang mendefinisikan image dasar. Dengan `caddy:latest`, berarti kita menggunakan image resmi Caddy dengan tag `latest` untuk memastikan kita menggunakan versi terbarunya. Image ini sudah berisi web server Caddy.
   - `COPY`: Instruksi untuk menyalin file atau folder dari perangkat kita ke dalam image Docker.
     - `./index.html` adalah file sumber yang ada di direktori kita saat ini yang ingin disalin ke dalam container.
     - `/usr/share/caddy/` adalah folder tujuan di dalam container tempat file yang akan kita salin. Sama halnya dengan instruksi kedua jika ingin menyalin folder assets.

3. **Melakukan Perintah Membuat Image**

   Jalankan perintah berikut untuk membuat Docker image:

   ```bash
   docker build -t zacky .
   ```

   - Perintah ini membuat Docker image dengan nama `zacky`. Tanda `.` digunakan untuk memastikan perintah dijalankan di direktori yang berisi Dockerfile.

4. **Melakukan Perintah untuk Menjalankan Image**

   Jalankan perintah berikut untuk menjalankan Docker image:

   ```bash
   docker run -d -p 8080:80 zacky
   ```

   - Perintah ini menjalankan Docker image `zacky`.
   - `-d`: Menjalankan container di mode detached (latar belakang).
   - `-p 8080:80`: Memetakan port 8080 di host ke port 80 di dalam container.
     
5. **Melakukan Perintah untuk Menghentikan Container**

   Jalankan perintah berikut untuk menghentikan container yang sedang berjalan:

   ```bash
   docker stop <container_id>
   ```

   - Ganti `<container_id>` dengan ID atau nama container yang ingin dihentikan. Anda dapat melihat daftar container yang sedang berjalan dengan perintah:

     ```bash
     docker ps
## Dokumentasi

[Google Drive Link - Dokumentasi Docker](https://drive.google.com/file/d/1Xc1ueWsqXJI-GBc8SVtCTNrvJR5XUQ6V/view?usp=sharing)
