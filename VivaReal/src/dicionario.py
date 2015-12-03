#-*- coding: latin1 -*-
livro = {"autor": "George R.R. Martin", "titulo": "A Guerra dos Tronos"}

livro["saga"] = "As cronicas de gelo e fogo"
print(livro)
print(livro["autor"])
del(livro["titulo"])
print(livro)

print("Itens: ", livro.items())
print("Chaves: ", livro.keys())
print("Valores: ", livro.values())