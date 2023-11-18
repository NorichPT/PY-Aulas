# Define a palavra com os asteriscos
palavra = "cp****xt"

# Cria uma lista com todas as letras do alfabeto
alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Cria uma lista vazia para armazenar as combinações de palavras testadas
comb_testadas = []

# Percorre a lista de letras e tenta preencher os asteriscos na palavra
for letra1 in alfabeto:
  for letra2 in alfabeto:
    palavra_tentativa = palavra.replace("*", letra1, 1).replace("*", letra2, 1)
    if palavra_tentativa not in comb_testadas:
      comb_testadas.append(palavra_tentativa)
      print(palavra_tentativa)


