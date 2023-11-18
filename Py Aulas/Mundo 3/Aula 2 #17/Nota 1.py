lanche = ["hamburger","sumo","pizza","pudim "]

lanche.append("sopa")#adiciona no final da lista
print(lanche)
print("-"*30)


if "pizza" in lanche:
    lanche.remove("pizza")


lanche.insert(0,"roupa")#adiciona onde eu quiser
print(lanche)


valores = list(range(4,11))
print(len(valores))

valores1 = [1,4,6,2,7,9]
valores1.sort()
print(valores1)

valores2 = [1,4,6,2,7,9]
valores2.sort(reverse=True)
print(valores2)


# tres formas de remover um item da lista

#del lanche[1]
#lanche.pop[1]
#lanche.remove("pizza")
