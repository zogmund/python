# Második dolgozat v1. A feladatok sorszáma mellett zárójelben szerepel a pontértékük.
# Értékelés:
# 14-15 - Príma!
# 12-13 - Egész jó, már csak egy kevéske hiányzik!
# 10-11 - Már van egy alap tudásod ebből a tananyagból, de még nem elég stabil.
# 7-9   - Látszik, hogy tanultál, de még kell gyakorolj, hogy továbblépj!
# 0-6   - Ezt még bizony meg kell tanulni :-)

#1 (1) Fordítsd meg a listát és írasd ki
list1 = [10, 20, 30, 40, 50]

# várt kimenet
# [50, 40, 30, 20, 10]


#2 (2) Adott az alábbi lista, írj egy programz, ami minden elemét a négyzetre emeli és kiírja

numbers = [1, 2, 3, 4, 5, 6, 7]

# várt kimenet
# [1, 4, 9, 16, 25, 36, 49]

#3 (3) Írj egy programot, ami az alábbi listába közvetlen a 6000 után beírja, hogy 7000

list3 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

# várt kimenet:
# [10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]

#4 (4) Adott két lista, fűzd össze az első minden eleméhez a második minden elemét ebben a sorrendben

list41 = ["Szia ", "Hello "]
list42 = ["Ponti", "Báltin"]

# várt kimenet
# ["Szia Ponti", "Szia Bálint", "Hello Ponti", "Hello Bálint"]

#5 (5) Adott két lista. Írj egy programot, ami végig iterál mindkettőt párhuzamosan és kiírja az elemeit egymás mellé elsőt eredeti sorrendbe, a másidokat fordított sorrendbe

list51 = [10, 20, 30, 40]
list52 = [100, 200, 300, 400]

# várt kimenet
# 10 400
# 20 300
# 30 200
# 40 100