word = input("Digite uma palavra: ")

if word == ''.join(reversed(word)):
    print(f"{word} é um palíndromo!")
else:
    print(f"{word} não é um palíndromo!")