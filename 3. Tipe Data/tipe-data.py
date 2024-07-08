# tipe data angka (tanpa koma) = integer
data_integer = 1
print("isian data : ", data_integer)
print("bertipe data : ", type(data_integer) )

print("")

# tipe data desimal (angka dengan koma) = float
data_float = 12.27;
print("isian data : ", data_float)
print("bertipe data : ", type(data_float) )

print("")

# tipe data string (kek "fajri", "fajri123")
data_string = "fajri"
print("isian data : ", data_string)
print("bertipe data : ", type(data_string) )

print("")

# tipe data boolean (true false)
data_boolean = False
print("isian data : ", data_boolean)
print("bertipe data : ", type(data_boolean) )

# tipe data khusus
data_complex = complex(5,6);
print("isian data : ", data_complex)
print("bertipe data : ", type(data_complex) )

# tipe data dari bahasa C
# karena dari tipe data diatas itu ternyata ada beberapa yang tidak ada
# jadi kita bisa pake yang tidak ada dengan pake lib dari "C"
# fun fact "python dibuat dari bahasa C"
from ctypes import c_double
# koma disini itu tanda titik "."
data_c_double = c_double(10.5)
print("isian data : ", data_c_double)
print("bertipe data : ", type(data_c_double) )