# 1. Mulai Program
print("===================================")
print("   APLIKASI KASIR RESTORAN")
print("===================================")
total = 0

# Data harga - sesuai di gambar
harga = {
    1: 25000, # Nasi Goreng
    2: 15000, # Mie Ayam
    3: 20000, # Ayam Geprek
    4: 30000, # Sate Ayam
    5: 18000  # Bakso
}

nama_menu = {
    1: "Nasi Goreng",
    2: "Mie Ayam",
    3: "Ayam Geprek",
    4: "Sate Ayam",
    5: "Bakso"
}

# 2, 3, 4. Tampilkan Menu & Proses Pemesanan (Perulangan while)
while True:
    # 2. Tampilkan Menu Makanan
    print("\n--- Daftar Menu Makanan ---")
    print("1. Nasi Goreng  - Rp25.000")
    print("2. Mie Ayam     - Rp15.000")
    print("3. Ayam Geprek  - Rp20.000")
    print("4. Sate Ayam    - Rp30.000")
    print("5. Bakso        - Rp18.000")
    print("0. Selesai Memilih")
    
    try:
        pilihan = int(input("Pilih Menu (0-5): "))
    except ValueError:
        print("Input tidak valid! Masukkan angka 0-5.")
        continue

    # 4. Apakah Pilihan 0?
    if pilihan == 0:
        break  # Ya -> lanjut ke hitung diskon
    
    # Tidak -> proses pesanan
    if pilihan in harga:
        try:
            jumlah = int(input(f"Masukkan jumlah {nama_menu[pilihan]}: "))
        except ValueError:
            print("Jumlah harus angka!")
            continue

        if jumlah <= 0:
            print("Jumlah harus lebih dari 0!")
            continue
            
        # Hitung Subtotal
        subtotal = harga[pilihan] * jumlah
        total += subtotal
        print(f"=> Ditambahkan: {jumlah} x {nama_menu[pilihan]} = Rp{subtotal}")
        print(f"Total sementara: Rp{total}")
    else:
        print("Pilihan tidak ada! Coba lagi.")
        continue

# 5. Hitung Diskon
print("\n===================================")
if total > 200000:
    diskon_persen = 20
    potongan = total * 0.20
else:
    diskon_persen = 0
    potongan = 0

total_bayar = total - potongan

# 6. Tampilkan Struk Pembayaran
print("      STRUK PEMBAYARAN")
print("===================================")
print(f"Total Belanja    : Rp {total}")
print(f"Diskon           : {diskon_persen}%")
print(f"Potongan         : Rp {int(potongan)}")
print("-----------------------------------")
print(f"Total Bayar      : Rp {int(total_bayar)}")
print("===================================")
print("          Terima Kasih!")
