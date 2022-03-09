import sys

bemenet = sys.stdin
print('Írj be valamit (q-val tudsz kilépni)')
# Olvasunk a bemenetről. Akkor lépünk tovább, ha kapunkt a standard inputon (stdin) valamit
for line in bemenet:
	if line.strip().isnumeric() == True:
		print("Számot kaptunk: " + line)
	elif line.strip()=='q':
		sys.exit(0)
	else:
		print("Nem számot kaptunk: " + line )