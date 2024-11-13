Numeros = []
while len(Numeros )<3 :
    try:
        num = int(input("introduce un numero" ))
        
        Numeros.append(num)
    except: 
        print("introduzca un numero valido")
Numeros.sort(reverse=True)
print("los numeros ordenados de mayor a menor es:", Numeros)