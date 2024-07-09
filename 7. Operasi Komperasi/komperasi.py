# setiap hasil dari komperasi adalah boolean (true/false)

# >, <, >=, <=, ==, !=, is, is not

a = 4
b = 2

print ("nilai a:", a)
print("nilai b:", b)

# lebih besar dari ">"
hasil = a > 3
print("apakah benar a > 3? :",hasil)

# lebih besar dari atau sama dengan  ">="
hasil = a >= b 
print("apakah benar a >= b? :", hasil)

# kurang dari "<"
hasil = a < b
print("apakah benar a < b? :", hasil)

# kurang dari atau sama dengan "<="
hasil = a <= b
print("apakah benar a <= b? :", hasil)

# sama dengan "=="
hasil = a == b
print("apakah benar a = b? :", hasil)
# skefo: bahwa di python hanya ada "==" tidak ada "==="

# tidak sama dengan "!="
hasil = a != b
print("apakah benar a != b? :", hasil)

# is membandingkan memory atau object
# membandingkan identitas dua objek
# memeriksa apakah kedua objek tersebut merujuk ke lokasi yang sama di memori.
x = 5
y = 5

print("nilai x=", x, "id = ", hex(id(x)))
print("nilai y=", y, "id = ", hex(id(y)))
# niali x dan y = 5

print("x is y :", x is y)

print ("x is 5 :", x is 5) # 5 itu adalah literal dan dia tidak makan memory

print(x is not y)


