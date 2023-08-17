alunos = []
notas = []

while True:
    nome = input("Digite o nome do aluno (ou digite 'sair' para encerrar): ")
    if nome.lower() == "sair":
        break

    nota = float(input("Digite a nota do aluno: "))
    alunos.append(nome)
    notas.append(nota)

if len(alunos) == 0:
    print("Nenhum aluno foi inserido.")
else:
    media = sum(notas) / len(alunos)
    print("\n=== Relatório de Notas ===")
    for i in range(len(alunos)):
        print(f"Aluno: {alunos[i]}, Nota: {notas[i]}")
    print(f"Média da turma: {media:.2f}")