##Progam akun
##Dibuat oleh Nurma L200190187
import random
angka = random.randint(0,1000)

Nama = 'Nurma Trisnawati'
TanggalLahir = '15 Februarai 2002'
NamaSingkat = Nama[0]+ '.' + Nama[6:16]
Username = Nama[0] + TanggalLahir[0:2] + TanggalLahir[13:17]
Password = Nama[0:3] + str(angka)


print(Nama)
print(TanggalLahir)
print(NamaSingkat)
print(Username)
print(Password)
