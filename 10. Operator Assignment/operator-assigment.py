
# * 1. Operator Penugasan Dasar: =
# Menetapkan nilai 10 ke variabel 'a'
a = 10
print("a =", a)  # Output: a = 10

# * 2. Operator Penugasan Penambahan: +=
# Menambah nilai 5 ke 'a' dan menetapkan hasilnya ke 'a'
a += 5  # a sekarang 15
print("a += 5 -> a =", a)  # Output: a += 5 -> a = 15

# * 3. Operator Penugasan Pengurangan: -=
# Mengurangi nilai 3 dari 'a' dan menetapkan hasilnya ke 'a'
a -= 3  # a sekarang 12
print("a -= 3 -> a =", a)  # Output: a -= 3 -> a = 12

# * 4. Operator Penugasan Perkalian: *=
# Mengalikan nilai 'a' dengan 2 dan menetapkan hasilnya ke 'a'
a *= 2  # a sekarang 24
print("a *= 2 -> a =", a)  # Output: a *= 2 -> a = 24

# * 5. Operator Penugasan Pembagian: /=
# Membagi nilai 'a' dengan 4 dan menetapkan hasilnya ke 'a'
a /= 4  # a sekarang 6.0
print("a /= 4 -> a =", a)  # Output: a /= 4 -> a = 6.0

# * 6. Operator Penugasan Modulus: %=
# Menghitung sisa pembagian 'a' dengan 5 dan menetapkan hasilnya ke 'a'
a %= 5  # a sekarang 1.0
print("a %= 5 -> a =", a)  # Output: a %= 5 -> a = 1.0

# * 7. Operator Penugasan Pembagian Bulat: //=
# Membagi 'a' dengan 2 menggunakan pembagian bulat dan menetapkan hasilnya ke 'a'
a //= 2  # a sekarang 0.0
print("a //= 2 -> a =", a)  # Output: a //= 2 -> a = 0.0

# * 8. Operator Penugasan Pangkat: **=
# Menaikkan 'a' ke pangkat 3 dan menetapkan hasilnya ke 'a'
a **= 3  # a sekarang 0.0 (karena 0.0 pangkat berapapun tetap 0.0)
print("a **= 3 -> a =", a)  # Output: a **= 3 -> a = 0.0

# * Mengatur ulang nilai 'a' untuk contoh bitwise
a = 5  # 5 dalam biner adalah 0101

# * 9. Operator Penugasan AND Bitwise: &=
# Melakukan operasi AND bitwise antara 'a' dan 3 dan menetapkan hasilnya ke 'a'
a &= 3  # 0101 AND 0011 adalah 0001
print("a &= 3 -> a =", a)  # Output: a &= 3 -> a = 1

# * 10. Operator Penugasan OR Bitwise: |=
# Melakukan operasi OR bitwise antara 'a' dan 2 dan menetapkan hasilnya ke 'a'
a |= 2  # 0001 OR 0010 adalah 0011
print("a |= 2 -> a =", a)  # Output: a |= 2 -> a = 3

# * 11. Operator Penugasan XOR Bitwise: ^=
# Melakukan operasi XOR bitwise antara 'a' dan 3 dan menetapkan hasilnya ke 'a'
a ^= 3  # 0011 XOR 0011 adalah 0000
print("a ^= 3 -> a =", a)  # Output: a ^= 3 -> a = 0

# * Mengatur ulang nilai 'a' untuk contoh shift bitwise
a = 8  # 8 dalam biner adalah 1000

print("nilai a:", a)

# * 12. Operator Penugasan Penggeseran Kanan Bitwise: >>=
# Menggeser bit dari 'a' ke kanan sebanyak 2 posisi dan menetapkan hasilnya ke 'a'
a >>= 2  # 1000 >> 2 adalah 0010
print("a >>= 2 -> a =", a)  # Output: a >>= 2 -> a = 2

# * 13. Operator Penugasan Penggeseran Kiri Bitwise: <<=
# Menggeser bit dari 'a' ke kiri sebanyak 2 posisi dan menetapkan hasilnya ke 'a'
a <<= 2  # 0010 << 2 adalah 1000
print("a <<= 2 -> a =", a)  # Output: a <<= 2 -> a = 8
