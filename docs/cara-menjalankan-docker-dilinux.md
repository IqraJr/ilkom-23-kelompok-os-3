Berikut langkah-langkah untuk menjalankan Docker di Linux:

---

### 1. **Pastikan Docker Terinstal**
Jika Docker belum diinstal, ikuti langkah berikut untuk menginstalnya:

#### a. Update dan instal dependensi yang diperlukan
```bash
sudo apt update
sudo apt install apt-transport-https ca-certificates curl software-properties-common -y
```

#### b. Tambahkan GPG key dan repositori Docker
```bash
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

#### c. Install Docker Engine
```bash
sudo apt update
sudo apt install docker-ce docker-ce-cli containerd.io -y
```

#### d. Verifikasi Instalasi
Cek versi Docker untuk memastikan instalasi berhasil:
```bash
docker --version
```

---

### 2. **Mulai Docker Service**
Docker membutuhkan daemon untuk berjalan. Aktifkan layanan Docker dengan perintah berikut:

#### a. Mulai layanan Docker
```bash
sudo systemctl start docker
```

#### b. Aktifkan agar Docker berjalan otomatis saat booting
```bash
sudo systemctl enable docker
```

#### c. Verifikasi status Docker
```bash
sudo systemctl status docker
```
Jika berjalan dengan benar, Anda akan melihat status **active (running)**.

---

### 3. **Jalankan Docker Tanpa Sudo (Opsional)**
Secara default, Docker membutuhkan akses superuser. Untuk menjalankannya tanpa menggunakan `sudo`:

#### a. Tambahkan pengguna ke grup Docker
```bash
sudo usermod -aG docker $USER
```

#### b. Logout dan login kembali, atau jalankan:
```bash
newgrp docker
```

#### c. Uji dengan perintah tanpa `sudo`:
```bash
docker run hello-world
```

---

### 4. **Menjalankan Docker**
Sekarang Docker siap digunakan. Anda dapat menjalankan container dengan perintah berikut:

#### a. Menjalankan container uji
Jalankan container **Hello World** untuk memverifikasi instalasi:
```bash
docker run hello-world
```

#### b. Menjalankan aplikasi (contoh: Nginx)
```bash
docker run -d -p 8080:80 nginx
```
Akses aplikasi di browser dengan alamat `http://localhost:8080`.

---

### 5. **Perintah Dasar Docker**
- **Melihat container yang sedang berjalan**:
  ```bash
  docker ps
  ```
- **Melihat semua container (termasuk yang berhenti)**:
  ```bash
  docker ps -a
  ```
- **Menghentikan container**:
  ```bash
  docker stop [container_id]
  ```
- **Menghapus container**:
  ```bash
  docker rm [container_id]
  ```
- **Menghapus image**:
  ```bash
  docker rmi [image_id]
  ```

---

### 6. **Memulai Ulang Docker (Jika Dibutuhkan)**
Untuk memulai ulang layanan Docker:
```bash
sudo systemctl restart docker
```

Docker kini siap digunakan untuk membangun, mengelola, dan menjalankan container di Linux!