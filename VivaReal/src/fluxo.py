#-*- coding: latin1 -*-
temp = input("Informe a temperatura:")
temp = int(temp)

if temp < 0:
    print("Está congelando...")
elif 0 <= temp <= 20:
    print("Está frio")
elif 21 <= temp <= 25:
    print("Está bom")
elif 26 <= temp <= 35:
    print("Está quente")
else:
    print("Está muito quente!")
    
x = temp if temp==0 else 1
print(temp if temp==0 else 'temp<>0')