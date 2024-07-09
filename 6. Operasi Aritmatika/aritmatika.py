import math # untuk bisa gunakan math.ceil/floor

a = 12
b= 2

# operasi "+" penjumlahan
jumlah = a+b
print("hasil", a, "+", b, "=", jumlah) # udh auto spasi btw jadi nda usah buatkan spasi

# operasi "-" pengurangan
pengurangan = a-b
print("hasil", a, "-", b, "=", pengurangan)

# operasi "*" perkalian
perkalian = a*b
print("hasil", a, "*", b, "=", perkalian)

# operasi "/" pembagian
pembagian = a/b
print("hasil", a, "/", b, "=", pembagian) #pembagian akan membuat tipe datanya auto jadi float

# pangkat (eksponen)
pangkat = a**b # a pangkat b
print("hasil", a, "pangkat", b, "=", pangkat)

# modulo (sisa bagi)
modulo = a%b
print("hasil", a, "modulo", b, "=", modulo)

# floor (bulatkan kebawah)
# ada dua cara :
# cara pertama:
a = 12.5
floor1 = a//b
print("hasil floor1-1", a, "bagi", b, "=", floor1)

a = 12
floor1 = a//b
print("hasil floor1-2", a, "bagi", b, "=", floor1)

# dari diatas didapatkan  pola bahwa klw kita pakai "//" itu tipe data hasilnya tergantung 
# angka-nya. Klw ada salah satu float maka hasil akan float

# cara kedua:
# harus import math dulu
a = 13
bagi = a/b
print("hasil pembagian (floor)", a, "/",b, "=",math.floor(bagi))
# math.floor itu pasti int (tanpa koma)

print("hasil pembagian (ceil)", a, "/",b, "=",math.ceil(bagi))