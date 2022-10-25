#coletando dados 

gasolina = float(input("Digite o preço da gasolina: "))
alcool = float(input("Digite o preço do alcool: "))
divisão = alcool/gasolina 

if divisão <0.7:
    print("Alcool")
else: 
    print("Gasolina") 
