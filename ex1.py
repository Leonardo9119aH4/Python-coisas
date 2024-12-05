str1=input("Digite um texto: ")
str2=input("Digite outro texto: ")
print(f"A string 1 tem tamanho {len(str1)} e a string 2 tem tamanho {len(str2)}")
if len(str1)==len(str2):
    print("As 2 strings tem mesmo tamanho")
else:
    print("As 2 strings tem tamanhos diferentes")
if str1==str2:
    print("As 2 strings tem mesmo conteúdo")
else:
    print("As 2 strings tem tamanhos diferentes")