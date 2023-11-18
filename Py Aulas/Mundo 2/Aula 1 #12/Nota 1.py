nome = str(input("Digite o seu nome:").lower())
if nome == "frederico":
    print("O teu nome é muito bonito")
elif nome == "diogo" or nome == "leandro" or nome == "goçalo":
    print("O teu nome é muito comum na tailandia")
elif nome in "ana nuria joana ":
    print("Lindo nome feminino")
else:
    print("Devias trocar de nome")
