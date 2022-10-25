# coletando dados do usuario: 
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))
imc = peso/altura**2


print("-" * 30)
print("os dados coletados foram:")
print("NOME: ",nome)
print("IDADE: ",idade," anos")
print("ALTURA: ",altura," cm")
print("PESO: ",peso," Kgs")
print("IMC: ", imc)
print("-" * 30)
