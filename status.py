g = input("Perempuan atau laki-laki ? (L/P): ")
if(g == 'L'):
    status = input("Anda sudah menikah atau belum? (Y/N): ")
    if(status == 'Y'):
        print("Hallo Bapak!")
    elif(status == 'N'):
        print("Hallo Mas!")
    else:
        print("Tidak ada didalam pilihan")
elif(g == 'P'):
    status = input("Anda sudah menikah atau belum? (Y/N): ")
    if(status == 'Y'):
        print("Hallo Ibu!")
    elif(status == 'N'):
        print("Hallo Mba!")
    else:
        print("Tidak ada dalam pilihan")
else:
    print("Tidak ada dalam pilihan")