# -*- coding: latin1 -*-

# Amplitude de um vetor 3D
amp = lambda x, y, z: (x ** 2 + y ** 2 + z ** 2) ** .5

print(amp(1, 1, 1))
print(amp(3, 4, 5))

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# Dividindo por 3
print (list(map(lambda x: x * 3, nums)))

# -*- coding: latin1 -*-
def pares(x):
    """
    Retorna true que o valor for par
    """
    if x%2==0:
        return True
    else:
        return False

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# Selecionando apenas os ímpares
print(filter(lambda x: x % 2, nums))

# Selecionando apenas os pares
print(filter(pares, nums))

# -*- coding: latin1 -*-
from functools import reduce

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# Soma com reduce
print(reduce(lambda x, y: x * y, nums))

#reduce func
letras = ['F','l','a','vio']
print(reduce(lambda x, y: x +'.'+ y, letras))

# Soma mais simples, mas só para números
print(sum(nums))

# Transposta de uma matriz
matriz = [[1, 2, 3,'1'], [4, 5, 6,'1'], [7, 8, 9,'1'],['a','b','c','d','e']]
print (zip(*matriz))

# -*- coding: latin1 -*-

print(zip(range(101,110), range(1, 10)))