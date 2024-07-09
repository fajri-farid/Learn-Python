data = input("masukkan data: ")

# print("masukan data: ",data)
print("masukan: ",data, "tipe data: ", type(data))

# didapatkan bahwa data yang dimasukkan akan selalu string
# maka klw mau ambil diluar string kita harus convert dulu
# apalagi klw mau buat kalkulator sederhana

# contoh klw mau inputan angka
angka = float(input("masukkan angka: "))
print("angka yang dimasukkan: ", angka, "tipe datanya: ", type(angka))

# masukan bool
bool = bool(int(input("masukkan boolean (0/1): ")))
print("bool yang dimasukkan: ",bool, "tipe datanya: ", type(bool))