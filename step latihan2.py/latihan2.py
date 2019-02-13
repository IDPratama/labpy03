max=0
while True:
	a=int(input('masukkan bilangan='))
	if max < a:
		max = a
	if a==0:
		break
print('bilangan terbesarnya adalah',max)