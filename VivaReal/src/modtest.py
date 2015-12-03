# -*- coding: latin1 -*-
# Arquivo ListCalc.py
""" Modulo que contem duas funcoes
    Uma que calcula a media de uma lista
    E outra que calcula a soma de uma lista
"""
def media(lista):
    """Calcula a media dos itens de uma lista"""
    return float(sum(lista))/len(lista)

def somalista(lista):
    """Calcula a soma dos itens de uma lista"""
    return sum(lista)