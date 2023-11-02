#1. Nan yon chenn karaktè, mete tout karaktè yo an miniskil.
chenn = "Ayiti"
nouvo_chenn = chenn.lower()
print(nouvo_chenn)

#2. Nan yon chenn karaktè, koupe chenn nan tout kote ki gen espas. Epi afiche 
#yon lis ki gen chak eleman yo
chenn = "Ayibobo Ayiti"
lis_chenn = chenn.split()
print(lis_chenn)

#3. Nan yon chenn karaktè, mete tout premye lèt chak mo an majiskil
chenn = "ayiti kapab avanse"
nouvo_chenn = ' '.join(word.capitalize() for word in chenn.split())
print(nouvo_chenn)

# Nan yon chenn karaktè, rekipere premye lèt chak mo. Epi afiche yon nouvo 
#chenn ak tout inisyal sa yo.
chenn = "Ayiti kapab avanse"
inisyal = ''.join(word[0] for word in chenn.split())
print(inisyal)

#Ranplase tout karaktè "a" ki nan yon chenn pa "@"
chenn = "Ayiti kapab avanse"
nouvo_chenn = chenn.replace("a", "@")
print(nouvo_chenn)

#9. Mete yon chenn karaktè devan dèyè, answit mete l an majiskil. 
chenn = "Ayiti"
nouvo_chenn = chenn[-1] + chenn[:-1].upper()
print(nouvo_chenn)

#13. Afiche endeks premye karaktè "a" ki nan yon chenn
chenn = "Ayiti kapab avanse"
endeks = chenn.index("a")
print(endeks)

#. Afiche total tout endeks karaktè "a" ki nan yon chenn (Kit se a majiskil oubyen 
# miniskil).
chenn = "Ayiti kapab avanse"
endeks_list = [i for i, letter in enumerate(chenn) if letter.lower() == "a"]
total_endeks = len(endeks_list)
print(total_endeks)

#Kreye yon lis ki gen endeks tout karaktè "a" ki nan yon chenn (Sèlman a 
#miniskil)
chenn = "Ayiti kapab avanse"
endeks_list = [i for i, letter in enumerate(chenn) if letter == "a"]
print(endeks_list)

#Retire tout espas ki nan yon chenn, epi kole chenn sa ak kantite karaktè li 
#genyen (Pa kontwole espas yo).
chenn = "Ayiti kapab avanse"
chenn_san_espas = chenn.replace(" ", "")
kantite_karakte = len(chenn_san_espas)
print(chenn_san_espas, kantite_karakte)
