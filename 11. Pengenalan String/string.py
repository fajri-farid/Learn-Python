
# * Membuat String!
data = "ini adalah string"
print(data)
print(type(data)) # ada class, karena ini semua adalah object

# * Cara Membuat String
'''
    1. Dengan menggunakan single quote ''
    2. Dengan menggunakan double quote ""
'''
data = ('menggunakan single quote')
print(data)

data = ("menggunakan double quote")
print(data)

# bisa digabung keduanya (single dan double)
data = ('fajri: "hello apa kabar?"')
print(data)

data = ("ini adalah hari jum'at")
print(data)
# jadi single dan double bisa di gunakan sesuai keadaan

# * kasus klw ketimpa single single double (single ketimpa karena dua)
data = "fajri: \"ini hari jum'at nggk sih?\""
# pake tanda "\" sebagai penanda ini bukan tanda penutup string
print(data)

# tanda backash "\" itu kita tidak bisa print karena dia ada peran khusus
# gimana cara printnya? dengan menambahkan "\" lagi
# contoh
data = "C:\\user\\docomunet\\python"
print(data) # output: C:\user\docomunet\python


# * tab 
data = "fajri \t fajri"
print(data)

# * backspace (delete)
data = "fajri farid" # biasa
print(data)
data = "fajri \bfarid" # jadi dekat, no spasi
print(data)

# * newline
data = "baris pertama.\nbaris kedua" # LF -> Carriage Return ==> unix, macos, linux
print(data)

print("")

data = "baris pertama.\rbaris kedua" # CR -> Carriage Return ==> commodore, acorn, lisp
print(data) # output: baris keduama.

print("")

data = "baris pertama.\r\nbaris kedua" #CRLF -> Carriage Return Carriage Return => dipakai oleh windows
print(data)

print("")

# * String literal atau raw
# ! Hati-Hati!
print("C:\nnew folder")
print("C:\\new folder")

# itu klw dikit enak klw ada banyak kan bakal kesulitan juga
# terus gimana solusinya?
print(r"C:\new folder") # pake "r"

# jadi segala bentuk kek kode untuk buat hal baru itu tidak berfungsi, ex:
print(r"C:\new \t \t folder") # untuk tanda single double masih berlaku

# * Multiline Literal String
print("""
      hello saya 
      fajri 
      farid
      \ssss
      """) # dia akan ngikutin format yang didalam print

# * Multiline Literal String dan Raw
print(r"""
hello\n nanana
      nananan \t 
      akakkak
""")
