# casting = mengubah satu tipe data ke tipe data lain
# tipe data = int, float, str, bool

# Inisialisasi data integer
data_int = 10
print("Isian data: ", data_int)  # Menampilkan nilai data integer
print("Tipe data: ", type(data_int))  # Menampilkan tipe data dari data integer

# Konversi ke float
data_float = float(data_int)
print("Isian data: ", data_float)  # Menampilkan nilai data float setelah konversi
print("Tipe data: ", type(data_float))  # Menampilkan tipe data dari data float

# Konversi ke string
data_str = str(data_int)
print("Isian data: ", data_str)  # Menampilkan nilai data string setelah konversi
print("Tipe data: ", type(data_str))  # Menampilkan tipe data dari data string

# Konversi ke boolean
data_bool = bool(data_int)
print("Isian data: ", data_bool)  # Menampilkan nilai data boolean setelah konversi
print("tipe data : ", type(data_bool)) # Menampilkan nilai data boolean setelah konversi
# true, kecuali dia = 0, dia akan false


# angka klw mau dibuat string dari awal itu pake tanda petik ""
# walaupun outputnya itu sama kek "number" tapi klw di "type" pasti akan beda
hello = "10"
print(hello)