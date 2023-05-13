n = int(input())
matriz = []

for i in range(n):
	listainterna = []
	for j in range(n):
		entrada = int(input())
		listainterna.append(entrada)
	matriz.append(listainterna)

def transposta(na):
	for i in range(n):
		for j in range(n):
			print(matriz[j][i], end=" ")
		print("")

def identidade(nb):
	cont = 0
	for a in range(n):
		for b in range(n):
			if a == b:
				if matriz[a][b] == 1:
					cont += 1
			else:
				if matriz[a][b] == 0:
					cont += 1
	if cont == n**2:
		print("Verdadeiro")
	else:
		print("Falso")

def esparsa(nc):
	cont1 = 0
	for c in range(n):
		for d in range(n):
			if matriz[c][d] == 0:
				cont1 += 1
	if cont1 > (n**2)/2:
		print("Verdadeiro")
	else:
		print("Falso")

def girar90(nd):
	for e in range(n):
		for f in range(n-1,-1,-1):
			print(matriz[f][e], end=" ")
		print("")





x = int(input())

if x == 1:
	transposta(matriz)
if x == 2:
	identidade(matriz)
if x == 3:
	esparsa(matriz)
if x == 4:
	girar90(matriz)




