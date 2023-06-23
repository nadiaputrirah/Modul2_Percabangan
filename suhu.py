sh = int(input("Masukan besarnya suhu: "))
if(sh <= 0):
    print("Pada suhu  ", sh ," derajat celcius, air akan berwujud es")
elif(sh > 0 & sh < 100):
    print("Pada suhu ", sh ," derajat celcius, air akan berwujud cair")
else:
    print("Pada suhu ", sh ," derajat celcius, air akan berwujud gas")