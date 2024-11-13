Longitud = float(input("digite la longitud: "))
Diametro = float(input("digite el diametro: "))
Densidad = 3.5

if Longitud > 7.5 and Longitud <9 :
    if Diametro > 0.5 and Diametro < 1.3 :
        Masa = (Diametro * Longitud) / Densidad
        if Masa > 5.8 :
            print("rechazada , la masa es " , Masa)
        else: 
            print("aprobada , la masa es " , Masa)
    else:
        print("el diametro debe ser mayor a 0.5 y menor a 1.3")
else:
    print("la longitud debe ser mayor a 7.5 y menor a 9")
