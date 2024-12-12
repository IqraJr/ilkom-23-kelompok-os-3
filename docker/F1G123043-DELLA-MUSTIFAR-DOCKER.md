# LANGKAH-LANGKAH MENJALANKAN DOCKER DI LINUX

# BUAT FOLDER DOCKER:
```bash
$ mkdir docker-project
```

# BERPINDAH KE FOLDER:
```bash
$ cd docker-project
```

# MENGEDIT ISI FILE:
```bash
$ nano app.py
```

# ISI FILE app.py:
```bash
$ from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Docker!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

```

# MEMBUAT FILE requirements.txt:
```bash
$ touch requirements.txt
```
# MENGEDIT FILE  requirements.txt:
```bash
$ nano requirements.txt
```
# MENGISI FILE requirements.txt:
```bash
$ flask
```
# MEMBUAT Dockerfile:
```bash
$ touch Dockerfile
```
# MENGEDIT FILE Dockerfile
```bash
$ nano Dockerfile
```

# MENGISI FILE Dockerfile:
```bash
$ # Menggunakan image Python resmi
FROM python:3.9-slim

# Menetapkan direktori kerja di container
WORKDIR /app

# Menyalin file dependensi ke dalam container
COPY requirements.txt requirements.txt

# Menginstal dependensi Python
RUN pip install -r requirements.txt

# Menyalin semua file proyek ke dalam container
COPY . .

# Menentukan port untuk aplikasi Flask
EXPOSE 5000

# Menjalankan aplikasi
CMD ["python", "app.py"]
```

# MEMBUAT FILE .dockerignore:
```bash
$ touch .dockerignore
```
# MENGEDIT FILE .dockerignore
```bash
$ nano .dockerignore
```
# ISI FILE .dockerignore:
```bash
$ __pycache__/
*.pyc
*.pyo
```

#  BANGUN Docker Image:
```bash
$ docker build -t flask-app .
```

# MENJALANKAN KONTAINER:
```bash
$ docker run -d -p 5000:5000 b3ba74c3787d
```
# MENAMPILKAN KONTAINER YANG AKTIF
```bash
$ docker ps
```
![gambardocker](https://drive.google.com/uc?id=1I4FtFMzlInXRoQYQTp9p49guL_T7n59o)

# AKSES APLIKASI DI BROWSER
```bash
$ http://localhost:5000
```

# MENAMPILKAN STATUS DOCKER TELAH BERJALAN:
![gambardocker](https://drive.google.com/uc?id=1p9ggqytBCGcX40GsG9MZqMmgFhL-VMbI)

# MENAMPILKAN BUKTI DOCKER BERJALAN
![gambardocker](https://drive.google.com/uc?id=1H5cmME0g7XrqJXG06LIa1KE25jv2Um-I)

# MELAKUKAN PEMBATASAN MEMORI DAN CPU
```bash
$ docker update --memory="256m" --memory-swap="512m" --cpus="0.5" vibrant_elbakyan
```
```bash
$ docker inspect vibrant_elbakyan
```
```bash
$ docker stats --no-stream --format "table {{.Name}}\t{{.ID}}\t{{.CPUPerc}}\t{{.MemPerc}}\t{{.MemUsage}}"
```
![gambardocker](https://drive.google.com/uc?id=1Hp-tMjlgoR3Xo8TJNSxthuBVYo8dzqTk)

# MENGHENTIKAN KONTAINER YANG BERJALAN
```bash
$ docker stop 6938e7e61034bd80069b71464194739e5300c22ba19af2576d923bedd5cb2aa5
```
# MENGHENTIKAN DOCKER DI LINUX 
```bash
$ sudo systemctl stop docker
```
# PERINTAH UNTUK MENCEGAH DOCKER AGAR TIDAK OTOMATIS DI MULAI
```bash
$ sudo systemctl disable docker.service
sudo systemctl disable docker.socket
```