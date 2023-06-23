print("=== Pembagian Bilangan ===")
bil1 = float(input("Masukkan bilangan pertama: "))
bilBagi= float(input("Masukkan bilangan pembagi: "))

if bilBagi == 0:
    print("Tidak dapat melakukan pembagian dengan nol")
else:
    hasil = bil1 / bilBagi
    print("Hasil pembagian bilangan: ", hasil)
