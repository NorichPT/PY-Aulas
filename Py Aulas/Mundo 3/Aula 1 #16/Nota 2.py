lanche = ("hamburger","sumo","pizza","pudim ")

for comida in lanche:
    print(f"{comida}")
print("-"*30)
for cont in range(len(lanche)):
    print(f"{lanche[cont]}")
print("-"*30)
for pos, comida in enumerate(lanche):
    print(f"{comida} na posiçao {pos}")
print("-"*30)