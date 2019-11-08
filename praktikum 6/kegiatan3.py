Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> Nama = 'Nurma Trisnawati'
>>> NIM = 'L200190187'
>>> x = '1' + NIM[7:]
>>> a = int(x)
>>> b= len(Nama)
>>> type(a)
<class 'int'>
>>> #Karena data "x" telah berubah menjadi type data integer
>>> type(b)
<class 'int'>
>>> #Karena data "Nama" memiliki intruksi len
>>> a / b
74.1875
>>> #Karena 1187 dibagi dengan 16 hasilnya adalah 74.1875
>>> a // b
74
>>> #Karena "//" merupakan pembagian yang dibulatkan ke bawah
>>> 10 * (a - 999)
1880
>>> #Karena nilai "a" dikurangi 999 adalah 188, kemudian dikalikan 10 adalah 1880
>>> b ** 2
256
>>> #Karena pengertian dari "**" adalah perpangkatan, maka nilai "b" dipangkatkan "2" adalah 256
>>> a % b
3
>>> #Karena arti dari "%" adalah sisa hasil bagi, maka nilai sisa hasil baginya dalah 3
>>> c = 12.5
>>> type(c)
<class 'float'>
>>> #Karena 12.5 adalah bilangan desimal sehingga termasuk kedalam type data float
>>> a / c
94.96
>>> #Karena arti dari 1187 dibagi dengan 12.5 adalah 94.96
>>> a // c
94.0
>>> #Karena arti dari "//" adalah pembagian dibulatkan kebawah jadi hasilnya 94.0
>>> a % c
12.0
>>> #Karena arti dari "%" adalah sisa bagi, dan sisa dari 1187 dibagi dengan 12.5 adalah 12.0
>>> c > b
False
>>> #Karena nila "c" lebih besar dari "b" adalah salah
>>> type(c > b)
<class 'bool'>
>>> #Karena c > b hanya memiliki kedua kemungkinan yaitu True atau False
>>> a > b and b > c
True
>>> #Karena logika "DAN" True and True menghasilkan nilai True
>>> a > 1100 or b < 10
True
>>> #Karena logika "ATAU" True  or False menghasilkan nilai True
