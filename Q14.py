leet = {
    "A": "4",
    "B": "13",
    "C": "(",
    "D": "[)",
    "E": "3",
    "F": '|=',
    "G": "6",
    "H": "|-|",
    "I": "|",
    "J": "]",
    "K": "|<",
    "L": "1",
    "M": "|Y|",
    "N": "/\/",
    "O": "0",
    "P": "|>",
    "Q": "0,",
    "R": "|2",
    "S": "5",
    "T": "7",
    "U": "[_]",
    "V": "\/",
    "W": "\^/",
    "X": "}{",
    "Y": "`/",
    "Z": "2"
}

word = input("Digite a palavra a ser traduzida: ")
word = list(word)
newword = []

for i in range(len(word)):
    newword.append(leet[word[i].upper()])
newword = "".join(newword)

print(f"A palavra traduzida é: {newword}")