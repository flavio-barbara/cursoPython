
def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print ("Divisao por zero!")
    else:
        print ("Resultado", result)
    finally:
        print ("Executando a causa finally")
divide(1,0)
divide(10,2)