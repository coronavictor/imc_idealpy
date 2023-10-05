import sys

sexo=input("Digite seu sexo >>> M (Masculino) ou F (Feminino):").upper()
if sexo == "M":
    print()
elif sexo == "F":
    print()
else:
    print("Siga as instrucoes acima e tente novamente!")
    sys.exit()
nome=input("Digite seu nome: ")
peso=float(input("Digite seu peso: "))
altura=float(input("Digite sua altura em metros: "))
imc=peso/altura**2
ideal=21.7*altura**2
print("Ola " + nome + "!" )
print("Seu peso e:" , peso , "e sua altura e:" ,altura)
print("Portanto, seu indice de massa corporal e de:" , round(imc,1))
if imc < 18.5:
    print("Voce esta abaixo do peso ideal")
elif imc < 24.9:
    print("Voce esta no peso ideal")
elif imc < 29.9:
    print("Voce esta com sobrepeso")
elif imc < 34.9:
    print("Voce esta com Obesidade Grau I")
elif imc < 39.9:
    print("Voce esta com Obesidade Grau II")
else:
    print("Voce esta com Obesidade Grau III")

print("Peso ideal para sua altura e:", round(ideal,1))



