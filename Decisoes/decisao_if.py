nome=input("Digite o nome do paciente: ")
idade=int(input("Digite a idade do paciente: "))
if idade >= 65:
    print("O paciente " + nome + " possui atendimento prioritario!")
else:
    print("O paciente " + nome + " nao possui atendimento prioritario!")
print("FIM!")
