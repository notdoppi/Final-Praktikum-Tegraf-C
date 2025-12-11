# Final-Praktikum-Tegraf-C

| Name           | NRP        | Kelas     |
| ---            | ---        | ----------|
| Dwinanda Rakhish Baley | 5025241198 | C |
| Mirza Rifai Dhiaurrahman | 5025241205 | C |

## Knight’s Tour Solver (Warnsdorff + Backtracking)
Program ini mencari jalur Kuda pada papan catur 8×8, baik open tour maupun closed tour. Program menggunakan gabungan heuristik Warnsdorff dan backtracking untuk mencari rute yang mengunjungi seluruh kotak pada papan. Pengguna dapat memilih titik awal (x, y) dan memilih jenis tour yang ingin dicari.

### Cara Menggunakan Program
1. Jalankan file Python:
```python
python knightTour.py
```
2. Program akan meminta tiga input:  
- Start X
  - Koordinat X (0–7), dihitung dari kiri ke kanan.
- Start Y  
  - Koordinat Y (0–7), dihitung dari atas ke bawah.
- Jenis tour
  - Ketik c untuk closed tour
  - Ketik o untuk open tour

### Alur Kerja Program
1. Inisialisasi papan
   - Papan berukuran 8×8 diisi dengan nilai -1 (belum dikunjungi).
   - Titik awal diisi 0 (posisi pertama).
2. Pemilihan langkah menggunakan Warnsdorff
   - Untuk posisi saat ini, program menghitung semua langkah valid yang dimiliki kuda.
   - Setiap kandidat langkah diberi nilai degree (jumlah langkah lanjutan yang tersedia).
   - Daftar langkah diurutkan dari degree paling kecil ke paling besar.
   - Cara ini memperkecil kemungkinan macet di akhir.
3. Backtracking
   - Program bergerak mengikuti langkah terbaik.
   - Jika buntu, program mundur ke langkah sebelumnya dan mencoba jalur lain.
4. Pemeriksaan jenis tour
   - Jika open, jalur selesai saat semua 64 petak terkunjungi.
   - Jika closed, langkah terakhir harus bisa kembali ke posisi awal dengan gerakan kuda.
5. Output
   - Jika tour ditemukan, program mencetak papan 8×8 berisi urutan langkah (0–63).
   - Jika tidak ditemukan, program menampilkan pesan bahwa tour tidak tersedia dari posisi tersebut.
     
Contoh Output
```
39 18  1 20 41 36  3  6
 0 21 40 37  2  5 44 35
17 38 19 50 45 42  7  4
22 63 56 47 30 49 34 43
57 16 23 62 51 46 29  8
24 13 60 55 48 31 52 33
15 58 11 26 61 54  9 28
12 25 14 59 10 27 32 53
```
