
n = int(input())

nomes =[]
n1 = []
n2 = []
med = []
medtot = 0
ver = n // 10 #numero total de alunos que serao 'printados'.
maior = 0

for i in range (n):
	nome = input()
	nomes.append(nome)
	nota1 = float(input())
	n1.append(nota1)
	nota2 = float(input())
	n2.append(nota2)
	media = (nota1 + nota2) / 2
	med.append(media)

for a in range(len(nomes)):
	medtot += med[a]
medtot = medtot / n

for e in range(len(nomes)):
	troca = False
	for j in range(1, len(nomes) - e):
		if nomes[j] < nomes[j - 1]:
			nomes[j], nomes[j - 1] = nomes[j - 1], nomes[j]
			n1[j], n1[j - 1] = n1[j - 1], n1[j]
			n2[j], n2[j - 1] = n2[j - 1], n2[j]
			med[j], med[j - 1] = med[j - 1], med[j]
			troca = True
	if not troca:
		break

for h in range(len(nomes)):
	print(nomes[h])
	print("%.1f" % med[h])

for q in range(len(nomes)):
	if med[q] > medtot:
		maior += 1

print(maior)

for w in range(len(nomes)):
	troca = False
	for r in range(len(nomes) - 1):
		if med[r] < med[r + 1]:
			med[r], med[r + 1] = med[r + 1], med[r]
			nomes[r], nomes[r + 1] = nomes[r + 1], nomes[r]
			troca = True
	if not troca:
		break

for u in range(len(nomes)//10):
	print(nomes[u])

















