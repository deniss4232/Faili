vards=input("Ievadi savu vārdu nominatīvā locijumā (Kas?):")

vards=vards.lower() 
# funkcija .lower()- visus burtus kovertē par mazajiem burtiem.

vards=vards.capitalize()
# funkcija .capitalize()- simbolu virknē pirmo burtu konvertē par lielo.

UzminiVardu1="K.L"

while True:
    minejums=input(f"Uzmini vārdu- {UzminiVardu1[1]+UzminiVardu1[0]+UzminiVardu1[2]}: ")
    if UzminiVardu1==minejums:
        print("Tu uzminēji!")
        break
    else:
        print("mini velreiz!")
 UzminiVardu1="L.K"
while minejums!=UzminiVardu1:
    