#if  satu kondisi
nilai  = int(input("masukkan bilangan bulat:"))
if  (nilai > 0):
    print("Bilangan",nilai, "merupakan bilangan positif")
# else :#if dua kondisi
#     print("bilangan",nilai,"merupakan bilangan negatif")
elif (nilai < 0):
    print("bilangan",nilai,"merupakan bilangan negatif")
else:
    print("bilangan nol")