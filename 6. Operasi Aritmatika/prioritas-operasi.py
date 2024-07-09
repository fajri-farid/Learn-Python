x = 3
y = 2
z = 4 

hasil = x ** y * z + x / y - y % z // x
print(x,"**",y,"*",z,"+",x,"/",y,"-",y,"%",z,"//", x, "=", hasil)

hasil = x ** y * (z + x) / y - y % z // x
print(x,"**",y,"*", "(",z,"+",x,")","/",y,"-",y,"%",z,"//", x, "=", hasil)

# prioritas operasi

# Parentheses (Kurung) (): 
# Ekspresi di dalam kurung dievaluasi terlebih dahulu.

# Exponents (Eksponen) **: 
# Penghitungan pangkat.

# Multiplication (Perkalian) *, Division (Pembagian) /, Floor Division (Pembagian Bulat) //, 
# Modulus (Sisa Bagi) %: 
# Diurutkan dari kiri ke kanan.

# Addition (Penjumlahan) +, Subtraction (Pengurangan) -: 
# Diurutkan dari kiri ke kanan.