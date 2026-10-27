#input
nilai = int(input("masukkan nilai: "))
#proses
if nilai >=80 and nilai<=100:
    print("anda mendapatkan nilai A")
elif nilai>=70 and nilai <=80:
    print("anda mendapatkan nilai B")
elif nilai>=50 and nilai<=70:
    print("anda mendapatkan nilai C")
elif nilai>=30 and nilai<=50:
    print("anda mendapatkan nilai D")
elif nilai>=0 and nilai <=20:
    print("anda mendapatkan nilai E")
else:
    print("data tidak valid")
print("=======LATIHAN=======")
#INPUT
namabarang =input("masukkan nama barang:")
hargabarang =int(input("masukkan harga barang:"))
#proses
if namabarang=="kulkas":
   print(hargabarang - 0.10)
elif namabarang == "tv":
   print(hargabarang - 0.5)
elif namabarang=="radio":
    print("Tidak dapat diskon")
else:
    print("angka tidak valid")