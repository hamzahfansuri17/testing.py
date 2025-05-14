# todo.py

def tampilkan_menu():
    print("\n=== TO-DO LIST ===")
    print("1. Lihat daftar tugas")
    print("2. Tambah tugas")
    print("3. Hapus tugas")
    print("4. Keluar")

def tampilkan_tugas(tugas):
    if not tugas:
        print("Daftar tugas kosong.")
    else:
        for idx, item in enumerate(tugas, start=1):
            print(f"{idx}. {item}")

def tambah_tugas(tugas):
    item = input("Masukkan nama tugas: ")
    tugas.append(item)
    print(f"Tugas '{item}' berhasil ditambahkan.")

def hapus_tugas(tugas):
    tampilkan_tugas(tugas)
    try:
        index = int(input("Masukkan nomor tugas yang ingin dihapus: ")) - 1
        if 0 <= index < len(tugas):
            hapus = tugas.pop(index)
            print(f"Tugas '{hapus}' berhasil dihapus.")
        else:
            print("Nomor tugas tidak valid.")
    except ValueError:
        print("Masukkan angka yang benar.")

def main():
    tugas = []
    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu (1-4): ")
        
        if pilihan == "1":
            tampilkan_tugas(tugas)
        elif pilihan == "2":
            tambah_tugas(tugas)
        elif pilihan == "3":
            hapus_tugas(tugas)
        elif pilihan == "4":
            print("Keluar dari program. Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid. Coba lagi.")

if __name__ == "__main__":
    main()
