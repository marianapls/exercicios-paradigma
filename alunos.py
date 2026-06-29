alunos = []


quantidade = int(input("Quantos alunos tem na turma? "))


soma_media = 0

aprovados = 0
recuperacao = 0
reprovados = 0


for i in range(quantidade):

    print("Aluno", i + 1)

    nome = input("Nome: ")

    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    nota3 = float(input("Nota 3: "))

   
    media = (nota1 + nota2 + nota3) / 3

    
    if media >= 7:
        situacao = "Aprovado"
        aprovados = aprovados + 1

    elif media >= 5:
        situacao = "Recuperacao"
        recuperacao = recuperacao + 1

    else:
        situacao = "Reprovado"
        reprovados = reprovados + 1

   
    aluno = [nome, nota1, nota2, nota3, media, situacao]

    alunos.append(aluno)

   
    soma_media = soma_media + media


media_geral = soma_media / quantidade


maior_media = alunos[0][4]
menor_media = alunos[0][4]

aluno_maior = alunos[0][0]
aluno_menor = alunos[0][0]

for aluno in alunos:

    if aluno[4] > maior_media:
        maior_media = aluno[4]
        aluno_maior = aluno[0]

    if aluno[4] < menor_media:
        menor_media = aluno[4]
        aluno_menor = aluno[0]


print("RESULTADO FINAL")

for aluno in alunos:

    print("Nome:", aluno[0])
    print("Nota 1:", aluno[1])
    print("Nota 2:", aluno[2])
    print("Nota 3:", aluno[3])
    print("Média:", round(aluno[4], 2))
    print("Situação:", aluno[5])


print("DADOS DA TURMA")

print("Média geral da turma:", round(media_geral, 2))

print("Aluno com maior média:", aluno_maior)
print("Maior média:", round(maior_media, 2))

print("Aluno com menor média:", aluno_menor)
print("Menor média:", round(menor_media, 2))

print("Quantidade de aprovados:", aprovados)
print("Quantidade em recuperação:", recuperacao)
print("Quantidade de reprovados:", reprovados)