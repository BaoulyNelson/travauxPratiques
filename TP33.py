#1. Ou gen yon diksyonè. Rekipere tout valè yo, gras ak kle yo epi retounen yon 
#lis valè
diksyone = {"kle1": "valè1", "kle2": "valè2", "kle3": "valè3"}
lis_vale = list(diksyone.values())
print(lis_vale)

#2. Mande itilizatè a, tape yon valè... epi verifye si l gen akolad devan ak dèyè.
vale = input("Tape yon valè: ")
si vale.startswith("{") and vale.endswith("}"):
    print("Valè a gen akolad devan ak dèyè.")
    
#3. Pakouri yon diksyonè, epi afiche tout kle yo.
diksyone = {"kle1": "valè1", "kle2": "valè2", "kle3": "valè3"}
kle = list(diksyone.keys())
print(kle)

#4. Pakouri yon diksyonè, epi afiche tout valè yo.
diksyone = {"kle1": "valè1", "kle2": "valè2", "kle3": "valè3"}
valè = list(diksyone.values())
print(valè)

#5. Pakouri yon diksyonè, pou w kapab kreye yon kopi(nouvo) sou disksyonè sa.
diksyone_1 = {"kle1": "valè1", "kle2": "valè2", "kle3": "valè3"}
diksyone_2 = dict(diksyone_1)
print(diksyone_2)

#6. Anndan yon diksyonè ki gen kle ak valè(valè yo ka nenpòt tip done). Ajoute 
#yon underscore devan ak dèyè tout valè ki se chenn yo.
diksyone = {"name": "Lub", "age": 14, "assets": ["laptop", "phone"]}
diksyonè_modifye = {k: f"_{v}_" if isinstance(v, str) else v for k, v in diksyone.items()}
print(diksyone_modifye)

#10. Nan yon diksyonè ki gen valè ki se chenn sèlman. Kreye yon nouvo diksyonè 
#ki gen tout eleman ki gen valè ki dijit yo sèlman.
diksyone = {"a": "12", "b": "abc", "c": "12r", "d": "90"}
diksyonè_sèlman_dijit = {k: v for k, v in diksyone.items() if v.isdigit()}
print(diksyonè_sèlman_dijit)

#14. Pakouri yon disksyonè, pou w mete l sou fòm lis, kote chak eleman nan 
#disksyonè sa, vin sou fòm tipl(kle, valè) anndan lis la. 
diksyone = {"a": 1, "b": 2}
lis_eleman = list(diksyone.items())
print(lis_eleman)

#18. Pakouri yon lis tipl, pou w mete l sou fòm diksyonè. Ekzanp
lis_eleman = [("a", 1), ("b", 2)]
diksyone = dict(lis_eleman)
print(diksyonè)

#2. Kole 2 diksyonè ansanm pou fè youn, kote si gen eleman ki gen menm kle ap 
#konkatene valè
diksyone1 = {"a": 1, "b": "hello", "c": [1, 2]}
diksyone2 = {"a": 2, "b": "world", "d": {3, 4}}

diksyone_konbit = {}

for k in set(diksyone1.keys()).union(diksyone2.keys()):
    if k in diksyone1 and k in diksyone2:
        vale1 = diksyone1[k]
        vale2 = diksyone2[k]
        if isinstance(vale1, int) and isinstance(vale2, int):
            diksyone_konbit[k] = vale1 + vale2
        else:
            diksyone_konbit[k] = str(vale1) + str(vale2)
    elif k in diksyone1:
        diksyone_konbit[k] = diksyone1[k]
    else:
        diksyone_konbit[k] = diksyone2[k]

print(diksyone_konbit)


