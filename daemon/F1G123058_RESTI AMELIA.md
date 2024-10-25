import threading
import time

def tugas_latar_belakang():
    while True:
        print("Daemon thread berjalan...")
        time.sleep(2)

# Membuat thread
daemon_thread = threading.Thread(target=tugas_latar_belakang)

# Menandai thread sebagai daemon
daemon_thread.daemon = True

# Memulai thread
daemon_thread.start()

# Program utama
print("Program utama berjalan...")
time.sleep(5)
print("Program utama selesai.")

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
git push origin main.

 
