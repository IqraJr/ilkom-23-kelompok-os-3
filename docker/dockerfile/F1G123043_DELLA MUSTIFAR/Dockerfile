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
    
