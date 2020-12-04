#Pengiriman Barang
#Author Chenko_07


print("=== Program Pengiriman Barang ===")

def pilihan(i):
        switcher={
            1:'----Thai Thea----',
            2:'----Bento Box----',
            3:'----Handphone----',
            4:'----Laptop----',
            5:'----Drone----',
            6:'----Kasur----',
            7:'----Kipas----',
            8:'----Kompor----',
            9:'----Mouse----',
            10:'----Keyboard----'
        }

print("""
      BARANG YANG DIJUAL

      1. Thai Tea    : 10000
      2. Bento Box   : 30000
      3. Handphone   : 2000000
      4. Laptop      : 5000000
      5. Drone       : 10000000
      6. Kasur       : 1000000
      7. Kipas       : 500000
      8. Kompor      : 700000
      9. Mouse       : 150000
      10. Keyboard   : 450000
      """)

nomor=int (input("Masukan Pilihan: "))

jumlah=int (input("Masukan Jumlah Barang: "))


if nomor==1:
      total1=jumlah*10000
      print("Hasil1 =", total1)
      jenis1=("Thai tea")
elif nomor==2:
      total1=jumlah*30000
      print("Hasil1 =", total1)
      jenis1=("Bento Box")
elif nomor==3:
      total1=jumlah*2000000
      print("Hasil1 =", total1)
      jenis1=("Handphone")
elif nomor==4:
      total1=jumlah*5000000
      print("Hasil1 =", total1)
      jenis1=("Laptop")
elif nomor==5:
      total1=jumlah*10000000
      print("Hasil1 =", total1)
      jenis1=("Drone")
elif nomor==6:
      total1=jumlah*1000000
      print("Hasil1 =", total1)
      jenis1=("Kasur")
elif nomor==7:
      total1=jumlah*500000
      print("Hasil1 =", total1)
      jenis1=("Kipas")
elif nomor==8:
      total1=jumlah*700000
      print("Hasil1 =", total1)
      jenis1=("Kompor")
elif nomor==9:
      total1=jumlah*150000
      print("Hasil1 =", total1)
      jenis1=("Mouse")
elif nomor==10:
      total=jumlah*450000
      print("Hasil1 =", total1)
      jenis1=("Keyboard")

print(""" 
   JENIS LAYANAN
   
    1. JNE
    2. JNT
    3. TIKI
    """)

jenislayanan = input("Masukan Jenis Pengiriman: ")
if jenislayanan == '1':
    layanan = "JNE"
elif jenislayanan == '2':
      layanan = "JNT"
elif jenislayanan == '3':
      layanan = "TiKI"

def pilihan(i):
        switcher={
            1:'----Temanggung----',
            2:'----Magelang----',
            3:'----Klaten----',
            4:'----Surakarta----',
            5:'----Semarang----',
        }

print(""" 
      KOTA TUJUAN

      1. Temanggung
      2. Magelang
      3. Klaten
      4. Surakarta
      5. Semarang
      6. Kota Lain
      """)

nomor = int (input("Masukan Pilihan: "))
berat = int (input("Berat barang (Kg): "))
volume = int (input("Volume barang (item): "))
asal = input("Alamat Asal: ")
tujuan= input("Alamat Tujuan: ")

if nomor==1:
      total2=40*500 + berat*200
      print("Hasil2 =", total2)
      jenis2=("Temanggung")
elif nomor==2:
      total2=35*400 + berat*200
      print("Hasil2 =", total2)
      jenis2=("Magelang")
elif nomor==3:
      total2=20*300 + berat*200
      print("Hasil2 =", total2)
      jenis2=("Klaten")
elif nomor==4:
      total2=50*450 + berat*200
      print("Hasil2 =", total2)
      jenis2=("Surakarta")
elif nomor==5:
      total2=70*600 + berat*200
      print("Hasil2 =", total2)
      jenis2=("Semarang")
elif nomor==6:
      jarak=int (input("Masukan Jarak: "))
      KotaLain= input("Masukan Kota: ")
      total2=jarak*1000 + berat*300
      print("Hasil2 =", total2)
      jenis2=("KotaLain")


tagihan=total1+total2
print("\n=========================")
print("=====STRUK PENGIRIMAN=====")
print("===========================")
print("== Pembeli             :",nama)
print("== Item                :",jenis1)
print("== Alamat Asal         :",asal)
print("== Alamat Tujuan       :",tujuan)
print("== Tujuan              :",jenis2)
print("== Berat               :",berat)
print("== Volume              :",volume)
print("== Jarak               : KM.",jarak)
print("== Layanan             :",layanan)
print("== Tagihan             : Rp.",tagihan)
print("==========================")
print("==========================")
