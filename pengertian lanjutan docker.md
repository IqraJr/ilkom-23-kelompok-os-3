# Pengertian Docker

Docker merupakan platform yang memungkinkan pengembang untuk mengembangkan, mengirimkan, dan menjalankan aplikasi dalam kontainer. Kontainer adalah unit ringan dan portabel yang dapat menjalankan aplikasi dan semua dependensinya secara terisolasi dari lingkungan lainnya. Berikut beberapa pengertian lanjutan terkait Docker:

## 1. Kontainer
Sebuah unit standar yang mengemas kode aplikasi dan semua dependensinya, sehingga aplikasi dapat berjalan dengan konsisten di berbagai lingkungan.

## 2. Docker Image
Template yang digunakan untuk membuat kontainer. Image berisi semua file yang diperlukan untuk menjalankan aplikasi, termasuk kode sumber, pustaka, dan file konfigurasi.

## 3. Dockerfile
File teks yang berisi instruksi untuk membangun Docker image. Dalam Dockerfile, kita bisa menentukan langkah-langkah yang diperlukan untuk menginstal aplikasi dan dependensinya.

## 4. Docker Compose
Alat untuk mendefinisikan dan menjalankan aplikasi multi-kontainer. Dengan menggunakan file YAML, pengguna dapat mengatur berbagai kontainer yang saling terhubung dan mengelola siklus hidup mereka.

## 5. Docker Hub
Layanan penyimpanan cloud untuk Docker images. Pengembang dapat mengunggah, mengunduh, dan berbagi images di Docker Hub.

## 6. Orkestrasi
Proses manajemen dan pengaturan kontainer dalam skala besar. Alat seperti Kubernetes dan Docker Swarm digunakan untuk mengelola orkestrasi, memfasilitasi pengelolaan kontainer dalam kluster.

## 7. Virtualisasi vs. Kontainerisasi
Meskipun keduanya menawarkan isolasi, virtualisasi menjalankan sistem operasi tamu di atas hypervisor, sementara kontainer berjalan di atas kernel host dan lebih ringan, karena berbagi kernel yang sama.

## 8. Scalability
Kemampuan untuk dengan mudah menambah atau mengurangi jumlah kontainer yang berjalan berdasarkan kebutuhan beban kerja. Docker memudahkan proses ini dengan cepat.

Docker telah menjadi alat penting dalam pengembangan perangkat lunak modern, membantu tim untuk berkolaborasi lebih baik dan mempercepat proses pengembangan hingga produksi.
