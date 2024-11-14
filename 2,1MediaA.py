print("MEDIA DE ALGUMA COISA AI")

nome = input("primeiro, qual seu nome: ")

a = float(input("digite sua primeira nota: "))
b = float(input("digite sua segunda nota: "))
c = float(input("digite sua terceira nota: "))
d = float(input("digite sua quarta nota: "))

soma = a+b+c+d

media = soma/4

if media >= 5.0:
    print("Ola", nome ,"a sua media é", media ,"continue assim, vc esta indo bem:)")

else:
    print("Ola", nome ,"essa é sua media", media ,"parece que vc precisa melhorar:/")