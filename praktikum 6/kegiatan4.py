Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> Nama = "Nurma Trisnawati"
>>> NIM = 187
>>> Tinggi = 1.61
>>> Berat = 43
>>> TahunLahir = 2002
>>> Aku = (TahunLahir, Berat, Tinggi, NIM, Nama)
>>> Data = [TahunLahir, Berat, Tinggi, NIM, Nama]
>>> type(Aku)
<class 'tuple'>
>>> #Karena data "Aku" ditulis dengan menggunakan tanda kurung biasa dan item di dalamnya tidak dapat diubah
>>> Aku[0]
2002
>>> #Karena item pertama dari data "Aku" adalah "TahunLahir", dan nilai dari "TahunLahir" adalah 2002
>>> a = NIM % 4; Aku[a]
187
>>> #Karena sisa hasil bagi dari 187 dibagi 4 adalah 3, jadi hasil dari Aku[3] adalah 187
>>> type(Aku[a])
<class 'int'>
>>> #Karena nilai dari "NIM" adalah 3, 3 adalah data tipe integer
>>> Aku[a:4]
(187,)
>>> #Karena a adalah 3 maka data yang keluar 1 data yaitu "NIM"
>>> type(Aku[4])
<class 'str'>
>>> #Karena data ke-4 dari "Aku" adalah "Nama", nilai dari data "Nama" adalah "Nurma Trisnawati"
>>> Aku[0] = 'ok'
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    Aku[0] = 'ok'
TypeError: 'tuple' object does not support item assignment
>>> #Karena isi tuple tidak dapat diubah (immutable) sehingga terjadi error
>>> type(Data)
<class 'list'>
>>> #Karena data "Data" ditulis dengan menggunakan kurung siku dan koleksi item di dalamnya dapat berubah, bertambah, dan berkurang secara dinamis
>>> type(Data[4])
<class 'str'>
>>> #Karena nilai dari "Nama" adalah "Nurma Trisnawati", "Nurma Trisnawati" adalah data bertipe string
>>> Data[4][5]
' '
>>> #Karena data dari "Nama" adalah "Nurma Trisnawati" yang indeks ke-5 adalah ' '
>>> Data[4][a:6]
'ma '
>>> #Karena data dari "Nama" adalah "Nurma Trisnawati", lalu indeks yang diminta dari ketiga sampai keenam, nilainya adalah 'ma '
>>> Data[0] = 'ok'; Data
['ok', 43, 1.61, 187, 'Nurma Trisnawati']
>>> #Karena data berupa list merupakan tipe data koleksi dimana objeknya dapat berubah (mutable)
>>> Data[-a]
1.61
>>> #Karena a adalah 2, jadi indeks 2 dari "Data" adalah objek ketiga yaitu 1.61
>>> range(a)
range(0, 3)
>>> #Karena jadi range(3) adalah range dari 0 sampai 3
