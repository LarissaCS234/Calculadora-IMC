# coletando dados do usuario: 
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))
imc = peso/altura**2 #Formula para calcular o imc

#saida de dados 
print("-" * 30)
print("os dados coletados foram:")
print("NOME: ",nome)
print("IDADE: ",idade," anos")
print("ALTURA: ",altura," cm")
print("PESO: ",peso," Kgs")
print("IMC: ", imc)
print("-" * 30)

if imc < 16:
    print("Magreza grave!")
elif imc >=16.1 and imc <18.5: 
    print("Abaixo do normal")
elif imc >18.5 and imc <24.9: 
    print("Peso Normal")
elif imc >25 and imc <29.9:
    print("Excesso de peso")
elif imc >30 and imc <34.9:
    print("Obesidade clase I")
elif imc >35 and imc <39.9:
    print("Obesidade classe II")
elif imc >=40:
    print("Obesidade classe III")
else: 
    print("Dado invalido")
print("Seja feliz, saudável e que se dane o resto.")
print("-" * 30)
