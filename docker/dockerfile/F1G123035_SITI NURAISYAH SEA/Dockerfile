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
