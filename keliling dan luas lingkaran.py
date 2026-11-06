import math

print("=== Program Lingkaran ===")
print("1. Hitung keliling lingkaran")
print("2. Hitung luas lingkaran")

pilihan = int(input("Masukkan pilihan (1/2): "))
r = float(input("Masukkan jari-jari: "))

if pilihan == 1:
    keliling = 2 * 3.14 * r
    print(f"Keliling lingkaran = {keliling:.2f}")
elif pilihan == 2:
    luas = 3.14 * r * r
    print(f"Luas lingkaran = {luas:.2f}")
else:
    print("Pilihan tidak valid! Masukkan angka 1 atau 2.")
