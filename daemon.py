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
