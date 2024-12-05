st=input("Digite algo: ").lower()
vo=0
es=0
for i in st:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
        vo=vo+1
    if i==' ':
        es=es+1
print(f"Há {vo} vogais e {es} espaços")