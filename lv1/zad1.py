sati=int(input("Radni sati: "))
satnica=float(input("eura/h: "))

def total_euro(sati,satnica):
    ukupno= sati*satnica
    return print("Ukupno: ",ukupno)

total_euro(sati,satnica)