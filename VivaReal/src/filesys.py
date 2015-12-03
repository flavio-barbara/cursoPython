# -*- coding: latin1 -*-
import os.path
import glob

#mostra uma lista de nomes de arquivos
# e seus respectivos tamanhos

for arq in sorted(glob.glob('*.py')):
    print(arq, os.path.getsize(arq), os.path.dirname(arq),os.path.basename(arq))
    
print(os.path.dirname('/home/flavio/python3/curso/workspace/VivaReal/src/filesys.py'))
print(os.path.dirname('/home/flavio/python3/curso/workspace/VivaReal/src'))
