nome=input("Digite seu nome: ")
idade=int (input("Digite sua idade: "))
#and = E
#or = ou
if idade >= 18 and idade <=70:
    
    print(f"{nome} Seu voto é obrigatorio")

elif idade > 70 or idade >=16:
    
    print(f"{nome} seu voto é facultativo")

else:
    print(f"{nome} seu voto é proibido")  




