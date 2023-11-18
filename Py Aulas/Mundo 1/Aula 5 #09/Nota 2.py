frase = ("Curso em Vídeo Python")

print(len(frase))
print(frase.count("o"))
print(frase.count("o",0,13))
print(frase.find("deo"))
print(frase.find("Android"))
print("Curso" in frase)
print(frase.replace("Python", "Android"))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())

                #O ULTIMO VALOR É SEMPRE IGNORADO#

# 1|quantos caracteres existe na frase 
# 2|contar quantas vezes aparece a letra o minuscula
# 3!contar quantos o tem do 0 ao 13
# 4|diz a posiçao onde começa a frase/palavra/numero
# 5|-1 quer dizer que nao existe
# 6|existe dentro da frase curso ?
# 7|subestitui o que queres
# 8|troca as letras para MAIUSCULO
# 7|troca as letras para minusculo
# 8|troca tudo para minusculo e a primeira letra para MAIUSCULO
# 9|torna as primeiras letras de cada palavra MAUISCULAS

#[C][u][r][s][o][][e][m][][V][í][d][e][o] [] [P][y][t][h][o][n]
# 0  1  2  3  4 5  6  7 8  9  10 11 12 13 14 15 16 17 18 19 20  21