#1. Kreye yon lis eleman ki divizib pa 2, nan entèval [0-n] enklizif
n = 10
lis_divizib_pa_de = [i for i in range(n+1) if i % 2 == 0]
print(lis_divizib_pa_de)

#2. 2. Ou gen yon lis antye, konvèti l an yon lis chenn.
lis_antye = [1, 2, 3, 4, 5]
lis_chenn = [str(x) for x in lis_antye]
print(lis_chenn)

#3. Ou gen yon lis chenn ki an miniskil, konvèti an yon lis chenn majiskil
lis_miniskil = ["ayiti", "kapab", "avanse"]
lis_majiskil = [word.upper() for word in lis_miniskil]
print(lis_majiskil)

#4. Ou gen yon lis, kreye yon nouvo lis ki fèt ak eleman ki nan endèks ki divizib pa 
#3 yo sèlman
lis = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
nouvo_lis = [elem for i, elem in enumerate(lis) if i % 3 == 0]
print(nouvo_lis)

#5. Ou gen lis eleman, kreye yon nouvo lis ki gen chak 3 eleman yo gwoupe 
#anndan yon tipl.
lis = [1, 2, 3, 4, 5, 6, 7, 8, 9]
nouvo_lis = [tuple(lis[i:i+3]) for i in range(0, len(lis), 3)]
print(nouvo_lis)

#Ou gen yon lis, ki gen yon pakèt eleman ki repete. Konvèti l an yon lis, ki pa 
#gen okenn doublon
lis = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
lis_san_doublon = list(set(lis))
print(lis_san_doublon)

#Ou gen 2 lis. Kreye yon nouvo lis, ki genyen sèlman eleman komen ant 2 lis yo.
lis1 = [1, 2, 3, 4, 5]
lis2 = [3, 4, 5, 6, 7]
lis_komen = list(set(lis1).intersection(lis2))
print(lis_komen)

#10. Ou gen 2 lis. Kreye yon nouvo lis, ki genyen sèlman eleman distenge ant 2 lis 
#yo
lis1 = [1, 2, 3, 4, 5]
lis2 = [3, 4, 5, 6, 7]
lis_distenge = list(set(lis1).symmetric_difference(lis2))
print(lis_distenge)

#11. Ou gen yon diksyonè. Kreye yon nouvo lis ak kle yo sèlman, epi yon lòt ak valè 
#yo sèlman.
diksyonè = {"kle1": "valè1", "kle2": "valè2", "kle3": "valè3"}
lis_kle = list(diksyonè.keys())
lis_valè = list(diksyonè.values())
print(lis_kle)
print(lis_valè)

#12. Reyini 3 lis ansanm, san okenn doublon.
lis1 = [1, 2, 3]
lis2 = [2, 3, 4]
lis3 = [3, 4, 5]
lis_kombinez = list(set(lis1 + lis2 + lis3))
print(lis_kombinez)


