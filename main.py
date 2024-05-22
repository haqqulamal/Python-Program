import os

# Nama file untuk menyimpan data
FILE_NAME = 'data_keuangan.txt'

def load_data():
    data = {}
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r') as file:
            for line in file:
                tanggal, keterangan, jumlah, tipe = line.strip().split(';')
                data[tanggal] = {
                    'keterangan': keterangan,
                    'jumlah': float(jumlah),
                    'tipe': tipe
                }
    return data

def save_data(data):
    with open(FILE_NAME, 'w') as file:
        for tanggal, info in data.items():
            file.write(f"{tanggal};{info['keterangan']};{info['jumlah']};{info['tipe']}\n")

def tampilkan_data(data):
    print("Data Keuangan:")
    for key, value in data.items():
        print(f"Tanggal: {key}")
        print(f"  Keterangan: {value['keterangan']}")
        print(f"  Jumlah: {value['jumlah']}")
        print(f"  Tipe: {value['tipe']}")
        print()

def tambah_data(data):
    tanggal = input("Masukkan tanggal (YYYY-MM-DD): ")
    keterangan = input("Masukkan keterangan: ")
    jumlah = float(input("Masukkan jumlah: "))
    tipe = input("Masukkan tipe (pemasukan/pengeluaran): ").lower()

    data[tanggal] = {
        'keterangan': keterangan,
        'jumlah': jumlah,
        'tipe': tipe
    }
    save_data(data)
    print("Data berhasil disimpan!")

def hapus_data(data):
    tanggal = input("Masukkan tanggal data yang akan dihapus (YYYY-MM-DD): ")
    if tanggal in data:
        del data[tanggal]
        save_data(data)
        print("Data berhasil dihapus!")
    else:
        print("Data tidak ditemukan!")

def main():
    data = load_data()
    
    while True:
        print("\nMenu:")
        print("1. Tampilkan data keuangan")
        print("2. Tambah data keuangan")
        print("3. Hapus data keuangan")
        print("4. Keluar")

        pilihan = input("Pilih menu (1/2/3/4): ")

        if pilihan == '1':
            tampilkan_data(data)
        elif pilihan == '2':
            tambah_data(data)
        elif pilihan == '3':
            hapus_data(data)
        elif pilihan == '4':
            print("Terima kasih telah menggunakan program ini!")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

if __name__ == "__main__":
    main()
