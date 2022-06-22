h = 0
m = 0

for t in range(0, 56):
    nome = input("Escreva seu nome: ")
    sexo = str(input("Digite (m) para masculino ou digite (f) para feminino: "))

    if sexo == "m":
        h = h+1
        print(nome)
        print("você é homem")

    elif sexo == "f":
        m = m+1
        print(nome)
        print("você é mulher")

   
print("A quantidade de mulheres é {}".format(m))
print("A quantidade de homens é {}".format(h))