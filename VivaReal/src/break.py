#-*- coding: latin1 -*-
while 1:
    num = int(input("Informe um numero:"))
    primo = 0
    if num == 0:
        print("end") 
        break
    for i in range(2,num):
        if num % i == 0:
            primo = 1
            print ("Numero nao primo")
            break

    if primo == 0:
        print ("Primo!!!")
        
# continue
x = 0
while x <= 10:
    x = x + 1
    if x % 2 == 0:
        print ("Num " + str(x) + " e' par!")
        continue
    print ("x = ",x)