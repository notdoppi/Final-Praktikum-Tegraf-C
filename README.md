# Final-Praktikum-Tegraf-C

| Name           | NRP        | Kelas     |
| ---            | ---        | ----------|
| Dwinanda Rakhish Baley | 5025241198 | C |
| Mirza Rifai Dhiaurrahman | 5025241205 | C |


## Knight's Problem

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
