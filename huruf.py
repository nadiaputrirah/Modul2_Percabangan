print("======= Menentukan Huruf Konsonan atau vokal =======")
h = input("Masukkan sebuah huruf : ")
if (h in ['a', 'e', 'i', 'o', 'u']):
    print(h, "Huruf vokal")
else:
    print(h, "Huruf konsonan")
