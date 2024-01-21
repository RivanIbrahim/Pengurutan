def tukar_data(arr, i, j):
    """
    Fungsi ini bertugas menukar nilai antara dua elemen di dalam array arr pada posisi i dan j.

    Parameters:
        - arr: Array yang berisi elemen-elemen yang akan ditukar.
        - i, j: Indeks elemen yang akan ditukar.
    """
    arr[i], arr[j] = arr[j], arr[i]

def bubble_sort(arr):
    """
    Fungsi ini mengimplementasikan algoritme pengurutan gelembung untuk mengurutkan array arr secara ascending.

    Parameters:
        - arr: Array yang akan diurutkan.
    """
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                tukar_data(arr, j, j+1)

def input_angka():
    """
    Fungsi ini meminta pengguna untuk memasukkan jumlah angka yang akan diurutkan,
    dan kemudian meminta input untuk setiap angka.

    Returns:
        - Array yang berisi angka-angka yang diinput oleh pengguna.
    """
    jumlah_angka = int(input("Masukkan jumlah angka yang akan diinput: "))
    angka = []
    print("\nInput Angka Secara Acak")
    print("-------------------------------------------------")
    for i in range(1, jumlah_angka + 1):
        angka.append(int(input(f"Angka {i} : ")))
    return angka

def simpan_hasil_ke_file(arr):
    """
    Fungsi ini menyimpan hasil pengurutan dalam array arr ke dalam file teks dengan nama "hasil_pengurutan.txt".

    Parameters:
        - arr: Array yang berisi hasil pengurutan.
    """
    with open("hasil_pengurutan.txt", "w") as file:
        for angka in arr:
            file.write(str(angka) + "\n")

def tampilkan_menu():
    """
    Fungsi ini menampilkan menu pilihan untuk pengguna.
    """
    print("\nTampilan menu")
    print("1. Input angka")
    print("2. Tampil hasil pengurutan")
    print("3. Selesai")

if __name__ == "__main__":
    angka = []
    
    while True:
        tampilkan_menu()
        pilihan = input("Masukkan pilihan [1/2/3] : ")

        if pilihan == "1":
            angka = input_angka()
            bubble_sort(angka)
            simpan_hasil_ke_file(angka)
            print("Angka telah diurutkan.")
        elif pilihan == "2":
            try:
                hasil_pengurutan = []
                with open("hasil_pengurutan.txt", "r") as file:
                    lines = file.readlines()
                    hasil_pengurutan = [int(line.strip()) for line in lines]
                print(f"Hasil pengurutan: {hasil_pengurutan}")
            except FileNotFoundError:
                print("File hasil_pengurutan.txt tidak ditemukan. Silakan input angka terlebih dahulu.")
        elif pilihan == "3":
            print("Terima kasih, program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih 1, 2, atau 3.")
