from flask import Flask
from daemonize import Daemonize

app = Flask(__name__)

@app.route('/')
def home():
    return "Halo, ini adalah program web berbasis Python dengan daemon!"

def run():
    app.run(host='0.0.0.0', port=5000)

if __name__ == '__main__':
    daemon = Daemonize(app="flask_app", pid="/tmp/flask_app.pid", action=run)
    daemon.start()

# Proses Pembuatan Daemon dengan Python

## Langkah-langkah:
1. **Membuat Program Web**: Program web dibuat menggunakan *framework* Flask. Program ini menampilkan teks sederhana pada halaman web.
2. **Instalasi Modul `daemonize`**: Menggunakan pip untuk menginstal modul yang dibutuhkan:
   ```bash
   pip install python-daemon


### 4. Membuat dan Mengunggah File ke GitHub
Setelah membuat file `.md`, simpan dengan nama `F1G123010-riansyah.md` di folder `daemon/` pada repository GitHub kelompok Anda. 

Untuk mengunggahnya, lakukan langkah berikut:

```bash
git add daemon/F1G123010-riansyah.md
git commit -m "Menambahkan dokumentasi proses daemon"
git push origin main

 