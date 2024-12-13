# MENJALANKAN APLIKASI DENGAN DOCKER DI LINUX

# 1. Membuat Docker file
## Langkah 1: Membuat direktori proyek Docker
Buat folder proyek untuk menyimpan semua file yang diperlukan.
```bash
mkdir docker.project
cd docker.project
```

## Langkah 2: Membuat file aplikasi
Buat file Python bernama `main.py` dan isi dengan kode berikut:
```bash
nano main.py
```
### Isi file `main.py`:
```python
from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    html = """
    <html>
        <head>
            <style>
                body {
                    background-color: pink;
                    font-family: 'Arial', sans-serif;
                    text-align: center;
                    color: white;
                    margin-top: 20%;
                    font-size: 36px;
                }
            </style>
        </head>
        <body>
            <h1>Welcome Nuraisyah!</h1>
        </body>
    </html>
    """
    return render_template_string(html)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000)
```

## Langkah 3: Membuat daftar dependensi
Buat file `requirements.txt` untuk mencantumkan pustaka yang dibutuhkan.
```bash
echo flask > requirements.txt
```

## Langkah 4: Menulis Dockerfile
Buat file bernama `Dockerfile` yang mendefinisikan proses pembuatan image Docker.
```bash
nano Dockerfile
```
### Isi file `Dockerfile`:
```dockerfile
# Menggunakan Python versi slim sebagai image dasar
FROM python:3.10-slim

# Menetapkan direktori kerja
WORKDIR /usr/src/app

# Menyalin file dependensi ke container
COPY requirements.txt ./

# Menginstal pustaka Python
RUN pip install --no-cache-dir -r requirements.txt

# Menyalin semua file aplikasi ke container
COPY . .

# Menentukan port aplikasi Flask
EXPOSE 4000

# Perintah untuk menjalankan aplikasi
CMD ["python", "main.py"]
```

## Langkah 5: Menambahkan file .dockerignore
Tambahkan file `.dockerignore` untuk mengabaikan file yang tidak perlu dalam proses build.
```bash
echo "__pycache__/*.pyc*.pyo" > .dockerignore
```

## Langkah 6: Membuat Docker image
Gunakan perintah berikut untuk membangun image Docker.
```bash
docker build -t my-flask-app .
```

# 2. Menjalankan Container 
## Menjalankan container Docker
Jalankan container dengan mengaitkan port lokal ke port di container.
```bash
docker run -d -p 4000:4000 my-flask-app
```

## Memeriksa container yang aktif
Gunakan perintah berikut untuk melihat daftar container yang sedang berjalan:
```bash
docker ps
```
### Tampilan Cantainer Aktif
![image](https://github.com/user-attachments/assets/391a1786-6c92-4119-a17f-47bde25bb281)

## Mengakses aplikasi
Buka browser dan akses aplikasi Flask di:
```
http://localhost:4000
```
### Tampilan Browser
![Screenshot (188)](https://github.com/user-attachments/assets/796790dd-7c1e-44c7-8efc-04c9cefa0a1c)


# 3. Membatasi Penggunaan Memory dan CPU
Untuk membatasi penggunaan memori dan CPU, Anda dapat menggunakan opsi --memory saat menjalankan container.
```bash
docker run -d -p 4000:4000 --memory="215m" --cpus="0.5" my-flask-app
```
membatasi memori container menjadi 215MB dan menggunakan maksimal 0.5 CPU 
### Tampilan setelah dibatasi
![image](https://github.com/user-attachments/assets/3eeef629-49e7-4dc0-83b5-25a46878123d)


# 4. Bedah Container
Perintah untuk masuk ke dalam kontainer yang sedang di jalankan
```bash
docker exec -it agitated_greider /bin/bash
```
![image](https://github.com/user-attachments/assets/906467b4-24e4-4b48-b947-2424c96f3bf5)

