# program konversi satuan celcius ke satuan lain

print("selamat datang di Program Konversi Celcius!")
celcius = float(input("masukkan suhu celcius: "))
print("suhu yang kamu masukkan: ", celcius, "Celcius")

print(f"suhu inputan {celcius:.2f} celcius") # cara agar dibelakang koma 2

# Reamur
reamur = 4/5 * celcius

# fahrenheit
fahrenheit = 9/5 * celcius + 32

# kelvin
kelvin = celcius + 273

# hasil konversi
print("Hasil Konversi:")
print("reamur: ", reamur)
print("fahrenheit: ", fahrenheit)
print("kelvin: ", kelvin)