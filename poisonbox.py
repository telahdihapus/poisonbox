import os

banner = open('banner.txt').read()
print(banner)

gar_ = 0
garis = ''
while gar_ < os.get_terminal_size().columns:
	garis = garis+'-'
	gar_ += 1
print(garis)
pilihan = int(input('1. encrypt\n2. decrypt\nmasukan pilihan (1/2) : '))
print(garis)

def a(data):
	dx = {}
	dy = []
	i = 1
	a = 48
	while i <= 1000:
		if chr(a) == ':':
			a = a + 7
		elif chr(a) == '[':
			a = a + 6
		dy.append(chr(a))
		if chr(a) == 'z':
			break
		a = a + 1
		i = i + 1

	w = 0
	ang = 0
	while w < i:
		e = 0
		while e < i:
			dx[ang] = dy[w]+dy[e]
			ang = ang + 1
			e = e + 1
		w = w + 1
	return dx[data]

def b(data):
	dx = {}
	dy = []
	i = 1
	a = 48
	while i <= 1000:
		if chr(a) == ':':
			a = a + 7
		elif chr(a) == '[':
			a = a + 6
		dy.append(chr(a))
		if chr(a) == 'z':
			break
		a = a + 1
		i = i + 1

	w = 0
	ang = 0
	while w < i:
		e = 0
		while e < i:
			dx[dy[w]+dy[e]] = ang
			ang = ang + 1
			e = e + 1
		w = w + 1
	return dx[data]

def kunci(kunci1, kunci2, kunci3):
	kunci = []
	kunci.append(str(kunci1))
	kunci.append(str(kunci2))
	kunci.append(str(kunci3))

	kunci_baru1 = []
	i = 0
	while i < len(kunci):
		for x in kunci[i]:
			kunci_baru1.append(int(x))
		i = i+1

	kunci_baru2 = []
	for i in kunci_baru1:
		kunci_baru2.append(i)

	i = 1
	for x in kunci_baru1:
		if i == len(kunci_baru1):
			break
		y = int(x)+int(kunci_baru1[i])
		kunci_baru2.append(y)
		i = i+1

	kunci_baru3 = []
	for i in kunci_baru2:
		kunci_baru3.append(i)

	i = 1
	for x in kunci_baru2:
		if i == len(kunci_baru2):
			break
		y = int(x)^int(kunci_baru2[i])
		kunci_baru3.append(y)
		i = i+1

	kunci_baru4 = []
	for i in kunci_baru3:
		kunci_baru4.append(i)

	i = 1
	for x in kunci_baru3:
		if i == len(kunci_baru3):
			break
		y = int(x)*int(kunci_baru3[i])
		kunci_baru4.append(y)
		i = i+1
	return kunci_baru4

if pilihan == 1:
	plain = input('masukan data yang akan di enkripsi = ')
	print(garis)
	kunci_1 = str(input('masukan 4 digit angka\nkunci 1 = '))
	kunci_2 = str(input('kunci 2 = '))
	kunci_3 = str(input('kunci 3 = '))
	print(garis)

	semua_kunci = kunci_1+kunci_2+kunci_3

	if (len(kunci_1) != 4) or (len(kunci_2) != 4) or (len(kunci_3) != 4):
		print('digit kunci salah, pastikan memasukan 4 digit setiap kunci')
		print(garis)
		exit()
	elif(semua_kunci.isalpha == True):
		print('terdapat alfabet dalam kunci, masukan kunci kembali dengan benar')
		print(garis)
		exit()

	kunci_utama = kunci(kunci_1, kunci_2, kunci_3)

	if len(kunci_utama) > len(plain):
		panj = len(kunci_utama)
		panj_ = panj
		i = 0
		while i < panj_:
			panj = panj - 1
			if panj >= len(plain):
				del kunci_utama[panj]
			else:
				break
	elif len(kunci_utama) < len(plain):
		for i in kunci_utama:
			if len(kunci_utama) == len(plain):
				break
			kunci_utama.append(i)

	bagix = [ord(c) for c in plain]
	i = 0
	for bagix_ in bagix:
		bagix[i] = (bagix_^int(kunci_utama[i]))
		i = i +1
	jadi1 = ''.join(a(i) for i in bagix)
	print(jadi1)

elif pilihan == 2:
	enkrip = input('masukan data yang akan di dekripsi = ')
	print(garis)
	kunci_1 = str(input('masukan 4 digit angka\nkunci 1 = '))
	kunci_2 = str(input('kunci 2 = '))
	kunci_3 = str(input('kunci 3 = '))
	print(garis)

	semua_kunci = kunci_1+kunci_2+kunci_3

	if (len(kunci_1) != 4) or (len(kunci_2) != 4) or (len(kunci_3) != 4):
		print('digit kunci salah, pastikan memasukan 4 digit setiap kunci')
		print(garis)
		exit()
	elif(semua_kunci.isalpha == True):
		print('terdapat alfabet dalam kunci, masukan kunci kembali dengan benar')
		print(garis)
		exit()

	kunci_utama = kunci(kunci_1, kunci_2, kunci_3)

	if len(kunci_utama) > (len(enkrip)/2):
		panj = len(kunci_utama)
		panj_ = panj
		i = 0
		while i < panj_:
			panj = panj - 1
			if panj >= (len(enkrip)/2):
				del kunci_utama[panj]
			else:
				break
	elif len(kunci_utama) < (len(enkrip)/2):
		for i in kunci_utama:
			if len(kunci_utama) == (len(enkrip)/2):
				break
			kunci_utama.append(i)

	bagix = []
	x = 0
	z = 0
	for i in kunci_utama:
		if (len(enkrip)/2) == (x+2):
			break
		bagix.append(chr(b(enkrip[x:(x+2)])^i))
		x = x + 2
		z = z + 1

	jadi2 = ''.join(i for i in bagix)
	print(jadi2)

else:
	print('pilihan yang anda masukan belum benar.')
