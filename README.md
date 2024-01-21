#Documentation


Program Pengurutan dengan Bubble Sort
Deskripsi
Program ini mengimplementasikan algoritme pengurutan gelembung untuk mengurutkan array secara ascending. Pengguna diminta untuk memasukkan jumlah angka yang akan diurutkan dan kemudian memasukkan angka-angka tersebut. Program akan menyimpan hasil pengurutan dalam file teks dengan nama "hasil_pengurutan.txt".

Fungsi-fungsi Utama
1. tukar_data(arr, i, j)
Fungsi ini bertugas menukar nilai antara dua elemen di dalam array arr pada posisi i dan j.

Parameters
arr: Array yang berisi elemen-elemen yang akan ditukar.
i, j: Indeks elemen yang akan ditukar.
2. bubble_sort(arr)
Fungsi ini mengimplementasikan algoritme pengurutan gelembung untuk mengurutkan array arr secara ascending.

Parameters
arr: Array yang akan diurutkan.
3. input_angka()
Fungsi ini meminta pengguna untuk memasukkan jumlah angka yang akan diurutkan, dan kemudian meminta input untuk setiap angka.

Returns
Array yang berisi angka-angka yang diinput oleh pengguna.
4. simpan_hasil_ke_file(arr)
Fungsi ini menyimpan hasil pengurutan dalam array arr ke dalam file teks dengan nama "hasil_pengurutan.txt".

Parameters
arr: Array yang berisi hasil pengurutan.
5. tampilkan_menu()
Fungsi ini menampilkan menu pilihan untuk pengguna.

Penggunaan Program
Jalankan program.
Pilih opsi menu:
1. Input angka: Memasukkan angka untuk diurutkan.
2. Tampil hasil pengurutan: Menampilkan hasil pengurutan yang disimpan dalam file.
3. Selesai: Keluar dari program.
Program akan terus berjalan hingga pengguna memilih opsi "Selesai".

Catatan: Pastikan file "hasil_pengurutan.txt" ada sebelum memilih opsi "Tampil hasil pengurutan".
