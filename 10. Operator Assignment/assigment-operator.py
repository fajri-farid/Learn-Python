# menetapkan nilai ke variabel

a = 5 # adalah assigment (penetapan ke dalam variabel)
print("nilai a:", a)

# * tambah
a += 1 # sama aja dengan a = a + 1
print("nilai a += 1:, sekarang nilai a:", a)

print("")

# * kurang
print("nilai a:", a)
a -= 2 # sama aja dengan a = a - 2
print("nilai a -= 2:, sekarang nilai a:", a)

print("")

# * kali
print("nilai a:", a)
a *= 2 # sama aja dengan a = a * 2
print("nilai a *= 2:, sekarang nilai a:", a)

print("")

# * bagi
print("nilai a:", a)
a /= 2 # sama aja dengan a = a / 2
print("nilai a /= 2:, sekarang nilai a:", a) # bagi defaultnya itu float

print("")

# * modulo
print("nilai a:", a)
a %= 3 # sama aja dengan a = a % 3
print("nilai a /= 3:, sekarang nilai a:", a) 


print("")
a = 10

# * bagi bulatkan
print("nilai a:", a)
a //= 3 # sama aja dengan a = a // 3
print("nilai a //= 3:, sekarang nilai a:", a) # "//" pembulatannya itu floor

# pake round() klw mau sesuai prinsip mtk

print("")

# * pangkat
print("nilai a:", a)
a **= 3 # sama aja dengan a = a^3
print("nilai a **= 3:, sekarang nilai a:", a)

# * bitwise or
c = True
print("nilai c:", c)
c |= False # sama aja dengan a = a^3
print("nilai c |= False:, sekarang nilai c:", c)

# * bitwise and
c = True
print("nilai c:", c)
c &= False # sama aja dengan a = a^3
print("nilai c &= False:, sekarang nilai c:", c)

# * bitwise xor
c = True
print("nilai c:", c)
c ^= False # sama aja dengan a = a^3
print("nilai c ^= False:, sekarang nilai c:", c)
print("nilai c:", c)
c ^= True # sama aja dengan a = a^3
print("nilai c ^= True:, sekarang nilai c:", c)

print("")

# * geser-geser
d = 0b0100
# ob menunjukkan klw itu adalah biner
print("nilai d:", d)
# di format ke biner, karena tadi itu di dalam angka biasa
print("nilai d biner:", format(d, "04b")) # ke biner dengan basis 4

d >>= 2;
print("nilai d:", d)
print("nilai biner setelah di geser ke kanan 2 kali:", format(d, "04b"))
# mudahnya ini semua 0100 digeser ke kanan 2 kali jadi (basis 4) 0001(00)
# basis yang kosong atau tidak ada di kasih 0

print("")

d = 0b0100
print("nilai d:", d)
print("nilai d biner:", format(d, "04b"))
d <<= 2;
print("nilai d:", d)
print("nilai biner setelah di geser ke kiri 2 kali:", format(d, "04b"))
# berbeda dengan ">>" ini beda lagi, di itu di geser ke kiri dan basisnya tidak akan selalu sama
# misal pada kasus diatas itu akan jadi basis 5, karena 0100 kita geser ke kiri 2 kali:
# 1x :(0)1000, nol didepan pasti hilang
# 2x : 10000, hasil akhir!

# jadi klw >> itu dia tetap basisnya dan yang di hilangkan di akhir 
# klw << itu tidak selalu sama basisnya dan dihilangkan 0 didepan



