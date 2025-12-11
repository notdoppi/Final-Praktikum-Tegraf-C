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

## Largest Monotonically Increasing Subsequence
Pada program ini, kita diminta untuk mencari subsequence paling panjang dari suatu deretan angka dimana nilainya selalu naik secara monoton dan posisi elemen harus sesuai urutan aslinya

### Alur pemrograman

1. Membuat Node Tree
   Program memakai class `Node` untuk membuat pohon. Setiap node mempunyai:
   - `value` = isi angkanya
   - `children` = daftar node yang nilainya lebih besar dan berada di sebelah kanan pada array

2. Membuat Tree
   Fungsi `build_tree(arr, index)`:
   - mengambil elemen arr[index] menjadi root
   - mencari semua elemen di kanan (`index+1` sampai akhir) yang lebih besar
   - Untuk setiap elemen yang lebih besar, buat node child lewat rekursi
   - Hasilnya, pohon yang memperlihatkan semua pilihan angka berikutnya yang valid untuk subsequence naik

3. Mencari semua LIS dari 1 node
   Fungsi  `find_all_LIS_from_node(node, current_seq)`:
   - Tambahkan nilai node ke subsequence saat ini
   - Kalau node ga punya child → ini subsequence lengkap, kembalikan
   - Kalau punya anak:
       - Rekursif ke setiap anak
       - Simpan semua subsequence dengan panjang maksimal
4. Menjalankan dari setiap elemen array
   Fungsi `find_all_LIS(arr)`:
   - Setiap elemen dijadikan root awal
   - membangun pohon dari indeks itu
   - Cari semua LIS dari pohon tersebut
   - Simpan hanya subsequence terpanjang global
   Lalu subsequence duplikat dibuang.

5. Output semua LIS
   Program mengoutput seluruh subsequence terpanjang

<img width="485" height="131" alt="image" src="https://github.com/user-attachments/assets/f82843f1-670c-4c3c-9eb3-c92b4c7d97bf" />

[CODE](https://github.com/notdoppi/Final-Praktikum-Tegraf-C/blob/1c2bb71cb0dfb9162474bb724d7f0b961ddca6a2/LIS.py)

