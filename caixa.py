def tempo_atendimento(itens):
    return 2 + 0.5 * itens


num_caixas = int(input("Quantidade de caixas: "))
num_clientes = int(input("Quantidade de clientes: "))

caixas = []
tempos = []

for i in range(num_caixas):
    caixas.append([])
    tempos.append(0)

for i in range(num_clientes):
    print("Cliente", i + 1)

    codigo = input("Código: ")
    itens = int(input("Quantidade de itens: "))

    while itens < 0:
        itens = int(input("Digite novamente (não pode ser negativo): "))

    tempo = tempo_atendimento(itens)

   
    menor = 0

    for j in range(num_caixas):
        if tempos[j] < tempos[menor]:
            menor = j

    
    caixas[menor].append(codigo)
    tempos[menor] = tempos[menor] + tempo


print("RESULTADO")

total_clientes = 0
soma_tempos = 0

for i in range(num_caixas):
    print("Caixa", i + 1)
    print("Clientes:", caixas[i])
    print("Tempo total:", tempos[i])

    total_clientes = total_clientes + len(caixas[i])
    soma_tempos = soma_tempos + tempos[i]

media = soma_tempos / num_caixas


maior = 0
menor = 0

for i in range(num_caixas):
    if tempos[i] > tempos[maior]:
        maior = i
    if tempos[i] < tempos[menor]:
        menor = i

print("Tempo médio por caixa:", media)
print("Caixa com maior tempo:", maior + 1)
print("Caixa com menor tempo:", menor + 1)
print("Tempo total do sistema:", tempos[maior])