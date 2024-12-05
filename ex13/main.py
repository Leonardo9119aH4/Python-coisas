import json
import random   
chutes=set()
tentativas=6
with open(f'./ex11/palavras.json', 'r') as file:
    palavras=json.load(file)
palavra=palavras[random.randint(0, len(palavras)-1)].lower()
anagrama=list(palavra)
random.shuffle(anagrama)
anagrama=''.join(anagrama)
while tentativas>0:
    chute=input(f"Anagrama: {anagrama}\nChutes: {chutes}\nQual a palavra correta?\n").lower()
    while chute in chutes:
        chute=input("Você já chutou essa palavra\nQual a palavra correta?\n").lower()
    chutes.add(chute)
    if chute==palavra:
        print("Parabéns você acertou!")
        exit()
    else:
        print("Você errou!")
        tentativas=tentativas-1
print(f"Perdeu! Com {chutes} chutes. A palavra era {palavra}")
             

    

        