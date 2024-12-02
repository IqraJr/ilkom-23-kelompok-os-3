LANGKAH-LANGKAH MENJALANKAN DOCKER DI LINUX

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
# MENGISI FILE requirements.txt:
```bash
$ flask
```
# MEMBUAT Dockerfile:
```bash
$ touch Dockerfile
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

# AKSES APLIKASI DI BROWSER
http://localhost:5000

# MENAMPILKAN STATUS DOCKER TELAH BERJALAN:
![gambardocker] (https://github.com/delsskom/GAMBAR-STATUS-DOCKER/commit/f8018457df06e956d38915195a5f9af298ac1f31)

# MENAMPILKAN BUKTI DOCKER BERJALAN
![gambardocker] (https://github.com/delsskom/GAMBAR-STATUS-DOCKER/commit/c434196f1d509107a765fe7c4c01d3fa9eb4a1b6)

