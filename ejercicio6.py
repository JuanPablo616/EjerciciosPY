#Digite un número entero que se convierta de °C a °K

Num1 = float(input("Digite la cantidad de grados: "))

K = Num1 + 273.15
print("El total de °K es: ", K)

if K > 10.5:
    print ("El número", K, "es mayor que 10.5")

elif 