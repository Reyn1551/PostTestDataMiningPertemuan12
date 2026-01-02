# Sistem Kasir Restoran Sushi (Post Test Pertemuan 12)

Repositori ini berisi implementasi sistem Point of Sales (POS) sederhana berbasis web untuk studi kasus restoran "Sushi Tei KW". Proyek ini dikembangkan sebagai pemenuhan tugas Post Test Praktikum, dengan fokus pada logika pemrosesan transaksi, manajemen state keranjang belanja di sisi klien, dan rendering template dinamis menggunakan Flask.

## Deskripsi Teknis

Aplikasi ini dibangun menggunakan arsitektur Monolithic sederhana dengan Python Flask sebagai backend. Tujuannya adalah mensimulasikan alur kerja kasir mulai dari pemilihan menu, kalkulasi subtotal, hingga pencetakan struk pembayaran.

### Fitur Utama
1.  **Dinamis Data Menu**: Menggunakan struktur data dictionary Python untuk menyimpan katalog produk, memungkinkan skalabilitas penambahan menu tanpa mengubah mark-up HTML.
2.  **Client-Side State Management**: Mengimplementasikan logika **Shopping Cart** menggunakan JavaScript untuk memanipulasi DOM dan menyimpan array pesanan sementara. Hal ini mencegah terjadinya *page reload* yang tidak perlu setiap kali pengguna menambah item.
3.  **Parsial Data Submission**: Mengirimkan data pesanan kompleks (nested objects) dari frontend ke backend melalui serialisasi JSON string.
4.  **Transaction Reporting**: Halaman hasil (`result.html`) yang merender rincian transaksi secara server-side untuk menjamin konsistensi data harga dan total akhir.

## Struktur Direktori

*   `app/views.py`: *Controller* utama yang menangani routing HTTP, logika bisnis, dan penyedia data menu.
*   `app/templates/`: *View layer* yang berisi file HTML dengan templating Jinja2.
    *   `utama.html`: Antarmuka pemilihan menu dan keranjang.
    *   `result.html`: Templat struk pembayaran.
*   `app/static/style.css`: *Style sheet* untuk kustomisasi antarmuka pengguna (UI) dengan pendekatan desain responsif (CSS Grid).
*   `run.py`: Entry point untuk menjalankan development server.

## Cara Menjalankan

Untuk menjalankan aplikasi ini di lingkungan lokal, pastikan Python 3 sudah terinstal, lalu ikuti langkah berikut:

1.  **Instalasi Dependensi**
    Aplikasi ini membutuhkan library `Flask`. Disarankan menggunakan Virtual Environment.
    ```bash
    pip install flask
    ```

2.  **Menjalankan Server**
    Ekesekusi file `run.py`:
    ```bash
    python run.py
    ```

3.  **Akses Aplikasi**
    Buka browser dan kunjungi `http://127.0.0.1:5000`.

---
*Pengembangan kode dilakukan dengan memperhatikan kaidah Clean Code (keterbacaan dan struktur modular) untuk memudahkan proses review dan pengembangan lebih lanjut.*
