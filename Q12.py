num = input("Digite um número de telefone: ")
aux = list(num)

if '-' in list(num):
    if len(num) == 8:
        print("Telefone possui 7 dígitos. Vou acrescentar o digito três na frente.")
        aux.insert(0, '3')
        num = "".join(aux)
else:
    if len(num) == 7:
        print("Telefone possui 7 dígitos. Vou acrescentar o digito três na frente.")
        aux.insert(0, '3')
        num = "".join(aux)

num_s = num
num_c = num
aux = list(num)

if '-' in list(num):
    aux.remove('-')
    num_s = "".join(aux)
else:
    aux.insert(3, '-')
    num_c = "".join(aux)

print(f"Telefone corrigido sem formatação: {num_s}")
print(f"Telefone corrigido com formatação: {num_c}")