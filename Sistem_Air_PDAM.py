# Sistem Air PDAM Sederhana

tarif_per_m3 = 2500
pelanggan_list = [
    ("Attar", 100, 100 * tarif_per_m3),
    ("Doni", 15, 15 * tarif_per_m3),
    ("Bastian", 10, 10 * tarif_per_m3)
]

print("========== Sistem Air PDAM ==========")
print("1. Tambah Data Pemakaian")
print("2. Lihat Data")
print("3. Hapus Data")
print("4. Keluar")

pilihan = input("Pilih menu (1-4): ")

if pilihan == "1":
    nama = input("Masukkan nama pelanggan: ")
    pemakaian = float(input("Masukkan pemakaian air (m3): "))
    tagihan = pemakaian * tarif_per_m3
    pelanggan = (nama, pemakaian, tagihan)
    pelanggan_list.append(pelanggan)
    print(f"Data {nama} berhasil ditambahkan. Tagihan: Rp {tagihan}")

elif pilihan == "2":
    if not pelanggan_list:
        print("Data belum ada")
    
    else:
        print("==========Daftar Tagihan Air==========")
        nama, pemakaian, tagihan = pelanggan_list[0]
        print(f"1. {nama} | Pemakaian: {pemakaian} m3 | Tagihan: Rp {tagihan}")

        nama, pemakaian, tagihan = pelanggan_list[1]
        print(f"2. {nama} | Pemakaian: {pemakaian} m3 | Tagihan: Rp {tagihan}")

        nama, pemakaian, tagihan = pelanggan_list[2]
        print(f"3. {nama} | Pemakaian: {pemakaian} m3 | Tagihan: Rp {tagihan}")

elif pilihan == "3":
    print("==========Hapus data pelanggan==========")
    nama, pemakaian, tagihan = pelanggan_list[0]
    print(f"1. {nama} | Pemakaian: {pemakaian} m3 | Tagihan: Rp {tagihan}")

    nama, pemakaian, tagihan = pelanggan_list[1]
    print(f"2. {nama} | Pemakaian: {pemakaian} m3 | Tagihan: Rp {tagihan}")

    nama, pemakaian, tagihan = pelanggan_list[2]
    print(f"3. {nama} | Pemakaian: {pemakaian} m3 | Tagihan: Rp {tagihan}")

    hapus = int(input("Masukkan nomor pelanggan yang ingin di hapus (1-3): "))
    
    if hapus == 1:
        data = pelanggan_list.pop(0)
        print(f"Data {data[0]} berhasil dihapus")

    elif hapus == 2:
        data = pelanggan_list.pop(1)
        print(f"Data {data[0]} berhasil dihapus")

    elif hapus == 3:
        data = pelanggan_list.pop(2)
        print(f"Data {data[0]} berhasil dihapus")

    print("==========Daftar pelanggan==========")
    print(pelanggan_list)
    
elif pilihan == "4":
    print("==========Program sudah ditutup==========")

else:
    print("==========Input tidak valid==========")