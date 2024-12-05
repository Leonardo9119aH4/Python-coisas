cpf=input("Digite o seu CPF (xxx.xxx.xxx-xx): ")
if cpf[3]=='.' and cpf[7]=='.' and cpf[11]=='-':
    dv=cpf[12:14]
    cpf=cpf[0:3]+cpf[4:7]+cpf[8:11]
    cpf=[int(c) for c in cpf]
    sd1=0
    for i in range(len(cpf)):
        sd1=sd1+cpf[i]*(i+1)
    sd1=sd1%11
    cpf.append(sd1)
    sd2=0
    for i in range(len(cpf)):
        sd2=sd2+cpf[i]*(i)
    sd2=sd2%11
    if sd2==10:
        sd2=0
    if sd1==int(dv[0]):
        if sd2==int(dv[1]):
            print("CPF válido")
        else:
            print("CPF inválido: erro no 2° dígito verificador")
    else:
        print("CPF inválido: erro no 1° dígito verificador")
else:
    print("CPF inválido: erro de formatação")