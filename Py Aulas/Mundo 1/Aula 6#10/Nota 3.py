n1 = int(input("Digite a primeira nota:"))
n2 = int(input("Digite a segunda nota:"))
media = (n1+n2)/2
if media >=15:
    print(f"Tiveste uma nota boa {media}")
elif media<=13:
    print(f"Tiveste uma nota de treta {media}")