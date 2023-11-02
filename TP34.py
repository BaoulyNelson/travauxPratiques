import random
import string
import re

#1. kreye yon fonksyon ki ap pran yon paramèt yon mo, epi li retounen envès la.
def tounen_enves(mo):
    return mo[::-1]

mo = "Hello"
rezilta = tounen_enves(mo)
print(rezilta)

#2. kreye yon fonksyon ki pou jenere yon kòd aleyatwa ki gen n karaktè alfabetik.
def kod_aleyatwa(n):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(n))

n = 10
kod = kod_aleyatwa(n)
print(kod)

#3. kreye yon fonksyon ki pou jenere yon kòd aleyatwa ki gen n karaktè alfabetik, 
#san repetisyon
def kod_aleyatwa_san_repetisyon(n):
    karakte_yo = string.ascii_lowercase
    kod = ''.join(random.sample(karakte_yo, n))
    return kod

n = 10
kod = kod_aleyatwa_san_repetisyon(n)
print(kod)

#4. kreye yon fonksyon ki pou jenere yon kòd aleyatwa ki gen n karaktè 
#alafanimerik, san repetisyon
def kod_aleyatwa_alfanimerik_san_repetisyon(n):
    karakte_yo = string.ascii_letters + string.digits
    kod = ''.join(random.sample(karakte_yo, n))
    return kod

n = 10
kod = kod_aleyatwa_alfanimerik_san_repetisyon(n)
print(kod)

#5. Ou gen yon lis chenn. Jenere yon SLUG apati chenn nan. Nan yon SLUG, tout 
#karaktè ki akseptab yo se: alfanimerik ak "-"
def jenere_slug(chenn):
    slug = re.sub(r'[^a-zA-Z0-9-]', '-', chenn)
    slug = re.sub(r'-+', '-', slug)  # Retire doublon nan '-'
    slug = slug.strip('-')  # Retire '-' nan kòmansman ak nan fen
    return slug.lower()

chenn = "Hello World! This is a Slug Example."
slug = jenere_slug(chenn)
print(slug)

#6. Kreye yon fonksyon ki ap separe chak lèt nan yon mo ak yon vigil
def separe_avek_vigil(mo, vigil):
    mo_separe = vigil.join(mo)
    return mo_separe

mo = "Hello"
vigil = "-"
mo_separe = separe_avek_vigil(mo, vigil)
print(mo_separe)

#7. Kreye yon fonksyon ki ap kripte yon mo, avèk endèks li nan alfabè a. Chak 
#karaktè dwe separe ak yon tirè.
def kripte_alfabe(mo):
    kripte = '-'.join(str(ord(k) - ord('a')) for k in mo.lower())
    return kripte

mo = "ALO"
kripte = kripte_alfabe(mo)
print(kripte)

#11. Kreye yon fonksyon ki ap dekripte yon mo ki fèt ak endèks chak lèt nan alfabè 
#a, separe ak yon tirè
def dekripte_alfabe(kripte):
    dekripte = ''.join(chr(int(k) + ord('a')) for k in kripte.split('-'))
    return dekripte

kripte = "0-11-14"
dekripte = dekripte_alfabe(kripte)
print(dekripte)

#15. Kreye yon fonksyon ki ap pran 2 paramèt, epi ki pèmite valè yo. Answit li 
#retounen tou 2 valè yo sou fòm Tuple
def pran_2_paramet(paramet1, paramet2):
    return paramet1, paramet2

vale1 = "vale1"
vale2 = "vale2"
rezilta = pran_2_paramet(vale1, vale2)
print(rezilta)

#16. Kreye yon fonksyon ki ap pran yon non an paramèt, epi ki retounen inisyal yo. 
#Atansyon ak non konpoze ak tirè yo
def jenere_inisyal_non(non):
    inisyal = ''.join(part[0].upper() for part in non.split('-'))
    return inisyal

non = "Jean-Baptiste Jean"
inisyal = jenere_inisyal_non(non)
print(inisyal)
