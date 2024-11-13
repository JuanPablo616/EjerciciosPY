Notas = []
while len(Notas)<3 :
    try:
        num = float(input("introduce un numero" ))
        
        Notas.append(num)
    except: 
        print("introduzca un numero valido")
Notas.sort(reverse=True)
Promedio = (Notas[0] + Notas[1]) /2
print("su nota final es:" , Promedio)