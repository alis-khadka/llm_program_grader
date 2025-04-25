def expo(a,b,c):
	if b == 0:
		return 1 % c

	if b == 1:
		return a % c

	elif b % 2 > 0:
		rek_a = (expo(a,(b-1)//2,c))
		return  (rek_a * rek_a * a) % c

	else:
		rek_a = expo(a,b//2,c)
		return (rek_a * rek_a) % c
