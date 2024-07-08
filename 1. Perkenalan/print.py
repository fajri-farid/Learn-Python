import time

start_time = time.time()

print("fajri")
print("farid") # membuat baris baru
# karena baris ini tidak ada code, maka di output "wkwkwkw" akan berada dibawah "farid"
print("wkwkwkw")
"""hello broo
fajri
farid
test
ini ada
lah
comment 
multi line
breeee"""

a = "hello bro"
print(a)

print(time.time() - start_time, "detik")
# akan di eksekusi berdasarkan urutan atas kebawah
# tahan alt untuk pindah pindah, sambil pointer atas bawah

# bytecode:
# python -m py_compile (nama file)
# pastikan sudah berada di folder tempat file berada

# cara compile-nya gimana?
# caranya dengan ke direktorinya dulu
# terus ketik di terminal
# # python -u " nama file"
# atau klw kasus ini
# python -u .\print.cpython-312.pyc

# kenapa harus di compile gitu? ke bytecode
# kita akan coba pakai library time 
# untuk mengukur perbedaan waktunya
# waktu akan berbeda-beda setiap saat nge-run pastinya tergantung kekuatan komputer saat itu