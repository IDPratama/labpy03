# PRAKTIKUM 3
alur logaritma program latihan1.py, latihan2.py, dan program1.py



# Alur logaritma latihan1.py

Sebelum membuatnya, buka notepad terlebih dahulu.
>![untitled4](https://user-images.githubusercontent.com/46734001/52701019-d02c7b80-2fab-11e9-899e-2735367c1db4.png)
>![notepad](https://user-images.githubusercontent.com/46734001/52701098-02d67400-2fac-11e9-8237-7098ec03cf36.png)

# Langkah 1

ketikan perintah seperti dibawah ini, Dan perhatikan setiap tanda baca dan hurufnya.
>![latihan1](https://user-images.githubusercontent.com/46734001/52701401-c0616700-2fac-11e9-89b3-08e4b1cf677f.png)

Berikut adalah penjelasannya

```
print ('masukkan nilai N: 5')
import random
jumlah = 5
a = 0
for x in range(jumlah):
	i = random.uniform(.0,.5)
	a+=1
	print('data ke:',a,'==>',i)
print ('selesai')
"print"     :berfungsi untuk menampilkan hasil ke layar monitor.
"import"    :fungsi lanjut yang dipanggil oleh statement import.
"ramdom"    :untuk menentukan suatu pilihan.
"range"     :merupakan fungsi yang menghasilkan list dengan rentang nilai tertentu.
"uniform"   :berfungsi untuk menampilkan bilangan float random dengan dengan batas awal bilangan x, dan batas akhir bilangan y.

```
# Langkah 2

Jika sudah, dan sama seperti apa yang ada di langkah 1. save dengan format ".py"
dan jika program yang kita buat berhasil, maka akan tampil seperti ini :
>![hasil1](https://user-images.githubusercontent.com/46734001/52702638-27801b00-2faf-11e9-87ec-32b74ca9ae06.png)


# Alur logaritma latihan2.py

Langkah pertama mari kita buka aplikasi text editor. aplikasi yang saya gunakan adalah notepad.
>![untitled4](https://user-images.githubusercontent.com/46734001/52701019-d02c7b80-2fab-11e9-899e-2735367c1db4.png)
>![notepad](https://user-images.githubusercontent.com/46734001/52701098-02d67400-2fac-11e9-8237-7098ec03cf36.png)

# Langkah 1

Kemudian masukkan codingan/perintah seperti dibawah ini, dan perhatikan tanda bacanya.
>![latihan2](https://user-images.githubusercontent.com/46734001/52925992-738fde80-3366-11e9-8454-d3abcee72b9b.png)

Berikut ini adalah penjelasan codingan/perintah yang kita buat

```
max=0
while True:
	a=int(input('masukkan bilangan='))
	if max < a:
		max = a
	if a==0:
		break
print('bilangan terbesarnya adalah',max)

"max"		:berfungsi bulid-in untuk mencari nilai tertinggi. Fungsi ini dapat diberikan sebuah parameter berupa angka.
"while True"	:untuk perulangan yang memiliki syarat dan tidak tentu berapa banyak perulangannya.
"int"		:untuk memasukkan bilangan.
"break"		:menghentikan operasi dibawahnya jika suatu kondisi yang ditentukan telah tercapai.
"print"		:berfungsi untuk menampilkan hasil ke layar monitor.

```
# Langkah 2

Jika sudah, dan sama seperti apa yang ada di langkah 1. simpan/save file dengan format ".py"
dan jika program yang kita buat berhasil, maka akan tampil seperti ini :
>![hasil2](https://user-images.githubusercontent.com/46734001/52926626-22cdb500-3369-11e9-8df5-1e3e7de026e7.png)

# Alur logaritma program1.py

Langkah pertama mari kita buka aplikasi text editor. aplikasi yang saya gunakan adalah notepad.
>![untitled4](https://user-images.githubusercontent.com/46734001/52701019-d02c7b80-2fab-11e9-899e-2735367c1db4.png)
>![notepad](https://user-images.githubusercontent.com/46734001/52701098-02d67400-2fac-11e9-8237-7098ec03cf36.png)

# Langkah 1

Kemudian masukkan codingan/perintah seperti dibawah ini, dan perhatikan tanda bacanya.
>![program1](https://user-images.githubusercontent.com/46734001/52926903-7096ed00-336a-11e9-927d-cf611832f5cf.png)

penjelasan :

```

a = 100000000
for x in range(1,9):
	if(x>=1 and x<=2):
		b=a*0
		print("laba bulan ke-",x,":",b)
	if(x>=3 and x<=4):
		c=a*0.1
		print("laba bulan ke-",x,":",c)
	if(x>=5 and x<=7):
		d=a*0.5
		print("laba bulan ke-",x,":",d)
	if(x==8):
		e=a*0.2
		print("laba bulan ke-",x,":",e)
total = b+b+c+c+d+d+d+e
print("\nTotal:",total)

"range"     	:merupakan fungsi yang menghasilkan list dengan rentang nilai tertentu.
">,<,>=,<="	:merupakan tanda pembanding dalam matematika.
"+"		:untuk menjumlahkan (menambah) angka.
"print"		:berfungsi untuk menampilkan hasil ke layar monitor.

```

# Langkah 2

Jika sudah, dan sama seperti apa yang ada di langkah 2. simpan/save file dengan format ".py"
dan jika program yang kita buat berhasil, maka akan tampil seperti ini :
>![hasil3](https://user-images.githubusercontent.com/46734001/52927216-fcf5df80-336b-11e9-8b88-5a5176a460c7.png)
