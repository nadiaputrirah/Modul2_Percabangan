print("=== Menentukan Tahun Kabisat atau Bukan ===")
kabisat = int(input("Masukkan tahun: "))
if (kabisat % 4 == 0) :
    print(kabisat, "adalah tahun kabisat")
else:
    print(kabisat, "bukan tahun kabisat")
