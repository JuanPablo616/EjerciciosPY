# Aumento del 15% si el sueldo es inferior a 300.000

sueldo = float(input("Ingrese el sueldo del trabajador: "))

if sueldo < 300000:
    aumento = sueldo * 0.15
    sueldo += aumento

print("El sueldo a pagar al trabajador es:", sueldo)