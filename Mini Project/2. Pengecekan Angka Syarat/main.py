# jadi disini itu kita akan mengecek apakah suatu angka itu
# < 3 atau > 10

input1 = float(input("masukkan angka < 3 atau > 10: "))

# pengecekan apakah inputan tadi itu < 3 atau > 10
memenuhi = (input1 < 3 or input1 > 10)

print(memenuhi)

print("")

isKurangDari = (input1 < 3)
print("Kurang dari 3:", isKurangDari)

isLebihDari = (input1 > 10)
print("Lebih dari 10:", isLebihDari)

print("")

isCorrect = isKurangDari or isLebihDari
print("hasil dari isKurangDari or isLebihDari:", isCorrect)

input2 = float(input("Masukkan angka lebih dari 3 dan kurang dari 10: "))

isLebihDari = (input2 > 3)
print("Lebih dari 10:", isLebihDari)

isKurangDari = (input2 < 10)
print("Kurang dari 3:", isKurangDari)

print("")

isCorrect = isKurangDari and isLebihDari
print("hasil dari isKurangDari and isLebihDari:", isCorrect)

# kemungkinan akan ada eror karena sebelumnya nama var-nya itu:
# input dan input2, jadi ubah itu jadi input1 dan input2, sebagai solusi dari eror!