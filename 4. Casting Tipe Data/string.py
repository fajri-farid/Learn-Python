# casting = mengubah satu tipe data ke tipe data lain
# tipe data = int, float, str, bool

# Konversi ke integer
# data_str = "hello" # akan eror
data_str = "123" # aman
data_int = int(data_str)
print("Isian data: ", data_int)  
print("Tipe data: ", type(data_int))  
# Konversi ke int:
# Bisa       : Jika string hanya berisi karakter angka (0-9) dan tanda minus (-) untuk bilangan negatif.
# Tidak bisa : Jika string mengandung karakter selain angka dan tanda minus. Termasuk tanda koma


# Konversi ke float
# data_str = "hello" # akan eror
data_str = "123.123" 
data_float = float(data_str)
print("Isian data: ", data_float) 
print("Tipe data: ", type(data_float)) 
# Konversi ke float:
# Bisa       : Jika string berisi karakter angka (0-9), tanda minus (-), dan titik desimal (.).
# Tidak bisa : Jika string mengandung karakter selain angka, tanda minus, dan titik desimal. 


# Konversi ke boolean
# data_str = "hello" 
data_str = "123.123" 
data_bool = bool(data_str)
print("Isian data: ", data_bool)  
print("tipe data : ", type(data_bool)) 
# Bisa  : String apa pun bisa dikonversi ke bool.

# Hasil :
# True  : jika string tidak kosong.
# False : jika string kosong ("").


