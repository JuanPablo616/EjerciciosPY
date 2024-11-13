Numeros = []
while len(Numeros )<3 :
    try:
        num = int(input("introduce un numero: " ))
        if num not in Numeros:
            Numeros.append(num)
        else:
            print("El número ya ha sido introducido. Por favor, introduce un número único.")
    except: 
        print("introduzca un numero valido")
mayor = max(Numeros)
menor = min(Numeros)
medio = sum(Numeros) - mayor - menor
print("El número medio es: ", medio) 