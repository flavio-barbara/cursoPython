def soma (valor1, valor2):
    return valor1 + valor2

resultado = soma(4, 5)
print("O resultado da soma de 4 + 5 = ", resultado)

def rgb_html(r=0, g=0, b=0):
    """Converte R, G, B em #RRGGBB"""
    return '#%02x%02x%02x' % (r, g, b)

print(rgb_html(23, 23, 111))
print(rgb_html(b=200, r=255, g=100))

def somatoria(*argumentos):
    """Somatoria dos argumentos"""
    soma = 0
    for i in argumentos:
        soma+=i

    return soma

print(somatoria(1,2,3,4,5,10,-20))

def func(**parametro):

    print(parametro)

func(kilo='k', metro='m', quilometro='km')