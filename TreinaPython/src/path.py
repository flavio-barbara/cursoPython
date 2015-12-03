# -*- coding: latin1 -*-
import os.path
import glob

#mostra uma lista de nomes de arquivos
# e seus respectivos tamanhos

for arq in sorted(glob.glob('L*')):
    print(arq, os.path.getsize(arq))