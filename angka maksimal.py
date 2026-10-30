# Program mencari angka maksimal dari 2 angka
a = float(input("Masukkan angka pertama: "))
b = float(input("Masukkan angka kedua  : "))

if a > b:
    maks = a
elif b > a:
    maks = b
else:
    maks = a  

if a == b:
    print("Kedua angka sama besar:", maks)
else:
    print("Angka maksimal adalah:", maks)