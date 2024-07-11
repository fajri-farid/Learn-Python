# operasi biner, binary
# operasi dari masing" bit

a = 9
b = 5

# bitwise or | 
c = a | b
print("======OR======")
print("nilai:", a, ", binary :", format(a,"08b"))
# Berikut penjelasan rincinya:
# b : Ini adalah format spesifikasi untuk biner. Artinya, angka akan dikonversi menjadi representasi biner.
# 08: Bagian ini terdiri dari dua komponen:
# 0 : Ini berarti hasil format akan diisi dengan angka nol (0) di bagian awal jika hasil biner memiliki 
#     panjang kurang dari yang ditentukan.
# 8 : Ini menunjukkan panjang minimal string hasil format. Jika panjang hasil biner kurang dari 8 
#     karakter, nol akan ditambahkan di bagian awal hingga mencapai panjang 8 karakter.

print("nilai:", b, ", binary :", format(b,"08b"))
print("---------------------------- (|)")
print("nilai:", c, ", binary :", format(c,"08b"))

# and
c = a & b
print("======AND======")
print("nilai:", a, ", binary :", format(a,"08b"))
print("nilai:", b, ", binary :", format(b,"08b"))
print("---------------------------- (&)")
print("nilai:", c, ", binary :", format(c,"08b"))

# not
c = ~a
print("======NOT======")
print("nilai:", a, ", binary :", format(a,"08b"))
print("---------------------------- (~)")
print("nilai:", c, ", binary :", format(c,"08b"))

#cara lain!
d = 0b0000001001
e = 0b1111111111
print("nilai:", e^d, "binary: ", format(e^d,"08b") )
# balikan dari biner 1 dengan basis 8

# shifting

# shift right (>>), pindahkan angka
a = 9
c = a >> 2;
print("======>>======")
print("nilai:", a, ", binary :", format(a,"08b"))
print("---------------------------- (>>)")
print("nilai:", c, ", binary :", format(c,"08b"))

# shift left (<<), pindahkan angka
a = 9
c = a << 2;
print("======<<======")
print("nilai:", a, ", binary :", format(a,"08b"))
print("---------------------------- (<<)")
print("nilai:", c, ", binary :", format(c,"08b"))


# jadi terjawab sudah perbedaan dari:
# or dengan |
# and dengan &
# perbedaan or dan and itu ya string biasa dan balikannya true false, sedangkan | dan & dia akan 
# ke biner (angka)


