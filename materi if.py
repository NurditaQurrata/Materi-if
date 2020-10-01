'''
kunci="python"
password=input("Masukkan kata: ")
if password == kunci:
    print("password benar")
else:
    print("password salah")
'''

'''
angka=int(input("Masukkan sebuah bilangan: "))
if angka > 0:
    print("Angka merupakan bilangan positif")
elif angka < 0:
    print("Angka merupakan bilangan negatif")
else:
    print("Angka merupakan 0")
'''

'''
x=int(input("Masukkan nilai x= "))
y=int(input("Masukkan nilai y= "))
if x == y:
    print("nilai",x,"dan",y,"mempunyai nilai yang sama")
else:
    if x > y:
        print(x, "lebih besar dari", y)
    if x < y:
        print(x, "lebih kecil dari", y)
'''

k=1
while k < 5:
    n=int(input("Masukkan angka ghaib: "))
    if n < 10:
        print("angka terlalu kecil")
        n=0
    elif n == 10:
        print("yapss kamu benar")
        k=6
    else:
        print("angka teerlalu besar")
    n+=1
    
