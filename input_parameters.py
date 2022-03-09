import sys

# Megvizsgáljuk, hogy pontosan egy bemeneti paramétert kaptunk-e
if len(sys.argv) == 1:
	print ("Nem 1 paramétert kaptunk!")
# Megvizsgáljuk, hogy számot kaptunk-e
elif sys.argv[1].isnumeric() == False:
	print("Nem számot kaptunk paraméterként!")
# Megvizsgáljuk, hogy páros-e vagy páratlan
elif int(sys.argv[1]) % 2 == 0:
	print("Páros számot kaptunk!")
else:
	print("Páratlan számot kaptunk")