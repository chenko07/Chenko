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

print("1. Thai Tea : 10000")
print("2. Bento Box : 30000")
print("3. Handphone : 2000000")
print("4. Laptop : 5000000")
print("5. Drone : 10000000")
print("6. Kasur : 1000000")
print("7. Kipas : 500000")
print("8. Kompor : 700000")
print("9. Mouse : 150000")
print("10. Keyboard : 450000")
nomor=int (input("Masukan Pilihan: "))
jumlah=int (input("Masukan Jumlah Barang: "))
if nomor==1:
      total1=jumlah*10000
      print("Hasil1 =", total1)
      jenis1=("Thai tea")
elif nomor==2:
      total2=jumlah*30000
      print("Hasil1 =", total2)
      jenis1=("Bento Box")
elif nomor==3:
      total3=jumlah*2000000
      print("Hasil1 =", total3)
      jenis1=("Handphone")
elif nomor==4:
      total4=jumlah*5000000
      print("Hasil1 =", total4)
      jenis1=("Laptop")
elif nomor==5:
      total5=jumlah*10000000
      print("Hasil1 =", total5)
      jenis1=("Drone")
elif nomor==6:
      total6=jumlah*1000000
      print("Hasil1 =", total6)
      jenis1=("Kasur")
elif nomor==7:
      total7=jumlah*500000
      print("Hasil1 =", total7)
      jenis1=("Kipas")
elif nomor==8:
      total8=jumlah*700000
      print("Hasil1 =", total8)
      jenis1=("Kompor")
elif nomor==9:
      total9=jumlah*150000
      print("Hasil1 =", total9)
      jenis1=("Mouse")
elif nomor==10:
      total10=jumlah*450000
      print("Hasil1 =", total10)
      jenis1=("Keyboard")

def pilihan(i):
        switcher={
            1:'----Temanggung----',
            2:'----Magelang----',
            3:'----Klaten----',
            4:'----Surakarta----',
            5:'----Semarang----',
        }

print("1. Temanggung : 40KM")
print("2. Magelang : 35KM")
print("3. Klaten : 20KM")
print("4. Surakarta : 50KM")
print("5. Semarang : 70KM")
nomor=int (input("Masukan Pilihan: "))
berat= int (input("Berat barang: "))
jalan= str (input("Alamat Tujuan: "))
jarak=int (input("Masukan Jarak: "))
if nomor==1:
      total1=jarak*berat*1000
      print("Hasil2 =", total1)
      jenis2=("Temanggung")
elif nomor==2:
      total2=jarak*berat*2000
      print("Hasil2 =", total2)
      jenis2=("Magelang")
elif nomor==3:
      total3=jarak*berat*1500
      print("Hasil2 =", total3)
      jenis2=("Klaten")
elif nomor==4:
      total4=jarak*berat*3000
      print("Hasil2 =", total4)
      jenis2=("Surakarta")
elif nomor==5:
      total5=jarak*berat*3500
      print("Hasil2 =", total5)
      jenis2=("Semarang")
      
nama=str (input("Nama Pengirim: "))
print("\n=========================")
print("=====STRUK PENGIRIMAN=====")
print("===========================")
print("== Pembeli     :",nama)
print("== Item        :",jenis1)
print("== Alamat      :",jalan)
print("== Tujuan      :",jenis2)
print("== Jarak       :KM.",jarak)
print("==========================")
print("==========================")
