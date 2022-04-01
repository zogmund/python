import sys

# lista növekvő sorba rendezése
# megkeressük mindig a legkisebb elemet. Azt beletesszük egy másik listába, az eredetiből meg kivesszük

# bemeneti lista
l = [4,5,8,1,3,0,9,-6,8,5,3]

# ebbe a listába fogjuk elmenteni a sorbarendezett elemekt
sortedList = []

while len(l) > 0:
	# Ez a változó ahhoz kell, hogy tudjam hanyadik eleménél tartok a listának
	i = 0
	# Ebbe mentjük az aktuális legkisebb elemet (alapból az első eleme a listának)
	min1 = l[0]
	# Az index-be fogjuk elmenteni a legkisebb elemhez tartozó indexet, hogy ki tudjuk majd szedni az eredeti lisátból
	index = 0
	# Végigmegyünk az "l" listán. Az "a" változóban mindig az aktuális listaelem lesz
	for a in l:
		# Ha kisebbet találtunk, mint az aktuálisan legisebb, akkor elmentjük azt, mint legkisebb elem és a hozzá tartozó indexet
		if a <= min1:
			min1 = a
			index = i
		# Lépünk egyet a számlálóval, hogy hanyadik listaelemnél járunk
		i = i + 1
	# Kivesszük az eredeti listából a legkisebbet
	l.pop(index)
	# Hozzárakjuk az új listához a talált legkisebb értéket
	sortedList.append(min1)
# Kiiratjuk a növekvő sorba rendezett listát
print(sortedList)
