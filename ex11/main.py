import json
import random
chutes=set()
tentativas=6
lacunas=[]
with open(f'./ex11/palavras.json', 'r') as file:
    palavras=json.load(file)
palavra=palavras[random.randint(0, len(palavras)-1)].lower()
for i in range(len(palavra)):
    lacunas.append('_')
while tentativas>0:
    if '_' not in lacunas:
        print(f"Parabéns, você acertou! Com {len(chutes)} chutes e {tentativas} tentativas restantes")
        exit()
    print(f"{lacunas}\n{tentativas} tentativas restantes\nChutes: {chutes}")
    chute=input("Digite uma letra: ").lower()
    while chute in chutes or len(chute)!=1:
        chute=input("Digite uma letra: ").lower()
        if chute in chutes:
            print("Você já chutou essa letra")
        elif len(chute)!=1:
            print("É só 1 letra pra chutar")
    chutes.add(chute)
    if chute in palavra:
        print("Você acertou!")
        for i in range(len(palavra)):
            if chute==palavra[i]:
                lacunas[i]=chute
    else:
        print("Você errou!")
        tentativas=tentativas-1
print(f"Perdeu! Com {chutes} chutes. A palavra era {palavra}")
             

    

        