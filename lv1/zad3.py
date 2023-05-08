lista=[]

while True:
    try:
       unos=input("Unesi broj:")
       lista.append(int(unos))
    except ValueError:
        if(unos=="Done"):
            break
        else:
            print("Nije unešen broj. Pokušajte ponovno")
            continue
            
print("Uneseno je",len(lista),"brojeva" )
print("Srednja vrijednost:", sum(lista)/len(lista))
print("Makismalna vrijednost:", max(lista))
print("Minimalna vrijednost:", min(lista))