Proses Menjalankan Website TIKET KAPAL dengan Daemon Process menggunakan Laragon MENGGUNAKAN BAHASA PYTHON

```markdown
# Proses Menjalankan Website Tiket Kapal dengan Daemon Process menggunakan Laragon Menggunakan Bahasa Python

Berikut adalah langkah-langkah untuk membuat dan menjalankan website Tiket Kapal menggunakan Python dengan Flask, dan menjalankannya sebagai daemon process di Laragon.

## 1. Persiapan Lingkungan

### 1.1 Instalasi Laragon

1. **Download Laragon**: Kunjungi [laragon.org](https://laragon.org) dan unduh Laragon.
2. **Instal Laragon**: Ikuti instruksi instalasi.

## 2. Membuat Aplikasi Flask

### 2.1 Instalasi Flask

Jika belum memiliki Python, silakan instal terlebih dahulu. Kemudian, instal Flask melalui terminal:

```bash
pip install Flask
```

### 2.2 Struktur Proyek

Buat struktur proyek sebagai berikut:

```
tiket_kapal/
│
├── app.py
├── daemon_app.py
└── templates/
    └── index.html
```

## 3. Kode Aplikasi Flask

### 3.1 `app.py`

Buat file `app.py` dan masukkan kode berikut:

```python
from flask import Flask, render_template

app = Flask(__name__)

# Dummy data untuk tiket kapal
tickets = [
    {"id": 1, "destination": "Bali", "price": 500000},
    {"id": 2, "destination": "Gili Trawangan", "price": 400000},
    {"id": 3, "destination": "Labuan Bajo", "price": 750000},
]

@app.route('/')
def index():
    return render_template('index.html', tickets=tickets)

if __name__ == '__main__':
    app.run(debug=True)
```

### 3.2 `templates/index.html`

Buat file `index.html` di dalam folder `templates`:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Daftar Tiket Kapal</title>
</head>
<body>
    <h1>Daftar Tiket Kapal</h1>
    <ul>
        {% for ticket in tickets %}
        <li>
            Tiket ke {{ ticket.destination }} - Rp {{ ticket.price }}
        </li>
        {% endfor %}
    </ul>
</body>
</html>
```

## 4. Menjalankan Aplikasi sebagai Daemon

Untuk menjalankan aplikasi Flask sebagai daemon, kita dapat menggunakan library `python-daemon`.

### 4.1 Instalasi python-daemon

Jika belum menginstal `python-daemon`, lakukan dengan perintah:

```bash
pip install python-daemon
```

### 4.2 `daemon_app.py`

Buat file `daemon_app.py` dan masukkan kode berikut:

```python
import daemon
from app import app

def run_app():
    app.run(host='0.0.0.0', port=5000)

if __name__ == '__main__':
    with daemon.DaemonContext():
        run_app()
```

## 5. Menjalankan Daemon

Buka terminal, arahkan ke direktori `tiket_kapal`, dan jalankan aplikasi dengan perintah:

```bash
python daemon_app.py
```

## 6. Verifikasi

1. **Akses Aplikasi**:
   - Buka browser dan akses `http://127.0.0.1:5000` untuk melihat daftar tiket kapal.

2. **Cek Proses Daemon**:
   - Di terminal, Anda dapat menggunakan perintah berikut untuk memastikan aplikasi berjalan:
     ```bash
     ps aux | grep python
     ```

## 7. Catatan

- **Menjaga Proses**: Daemon akan berjalan di latar belakang. Jika Anda ingin menghentikannya, Anda harus menemukan dan membunuh proses tersebut secara manual, atau Anda bisa menambahkan fitur untuk menghentikannya di kode.
- **Error Handling**: Pastikan untuk menangani error yang mungkin terjadi saat menjalankan aplikasi.
```

