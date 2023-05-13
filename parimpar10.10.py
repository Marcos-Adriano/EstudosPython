qnt=int(input())
cont1=0
cont2=0
cont3=0
soma=0
soma2=0
m=0
maior=-1
menor=1000
for i in range(1,qnt+1):
	n=int(input())
	fat=1
	for k in range(1,n+1):
		fat=fat*k
	div=0
	for w in range(1,n+1):
		if n%w==0:
			div=div+1
	if n%2==0:
		cont1=cont1+1
		if div==2:
			print("Par Primo %d %d" %(n**2,fat))
			cont3=cont3+1
		else:
			print("Par %d %d" %(n**2,fat))
	if n%2!=0:
		cont2=cont2+1
		if div==2:
			print("Impar Primo %d %d" %(n**2,fat))
			cont3=cont3+1
		else:
			print("Impar %d %d" %(n**2,fat))
	soma=soma+n
	méd=soma/i
	soma2=soma2+n**2
	while m<qnt:
		m=m+1
	if n<menor:
		menor=n
	if n>maior:
		maior=n
print(cont1)
print(cont2)
print(cont3)
print("%.2f"%méd)
print(soma2)
print(maior)
print(menor)
