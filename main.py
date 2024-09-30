numFileiras = 30
numColunas = 6
precoPrimeiraClasse = 100.0
precoClasseNormal = 80.0

def inicializarAssentos():
    assentos = []
    for x in range(numFileiras):
        fileira = []
        for x in range(numColunas):
            fileira.append('-')
        assentos.append(fileira)
    return assentos
def mostrarAssentos(assentos):
    print("Mapa de Assentos (colunas A a F):")
    for i in range(len(assentos)):
        fileira = f"{i+1:02d}"
        print(f"Fileira {fileira}: {assentos[i]}")
def verificarDisponibilidade(assentos, fileira, coluna):
    if assentos[fileira][coluna] == '-':
        return True
    return False
def marcarAssento(assentos, fileira, coluna, nome):
    if verificarDisponibilidade(assentos, fileira, coluna):
        assentos[fileira][coluna] = nome
        print(f"Assento {chr(65 + coluna)}{fileira+1} reservado para {nome}.")
    else:
        print(f"Assento {chr(65 + coluna)}{fileira+1} já está ocupado.")
def desmarcarAssento(assentos, fileira, coluna):
    if not verificarDisponibilidade(assentos, fileira, coluna):
        print(f"Assento {chr(65 + coluna)}{fileira+1} desmarcado.")
        assentos[fileira][coluna] = '-'
    else:
        print(f"O assento {chr(65 + coluna)}{fileira+1} já está vazio.")
def remarcarAssento(assentos, assentoAtual, fileiraNova, colunaNova):
    colunaAtual = ord(assentoAtual[0].upper()) - 65
    fileiraAtual = int(assentoAtual[1:]) - 1
    if not verificarDisponibilidade(assentos, fileiraAtual, colunaAtual):
        nome = assentos[fileiraAtual][colunaAtual]
        print(f"Assento {chr(65 + colunaAtual)}{fileiraAtual + 1} será liberado.")
        desmarcarAssento(assentos, fileiraAtual, colunaAtual)
        marcarAssento(assentos, fileiraNova, colunaNova, nome)
    else:
        print(f"O assento {assentoAtual} já está vazio.")
def relatorioAssentos(assentos):
    ocupados = 0
    primeiraClasse = 0
    classeNormal = 0
    valorPrimeiraClasse = 0
    valorClasseNormal = 0
    ocupadosLista = []
    i = 0
    while i < len(assentos):
        j = 0
        while j < numColunas:
            if assentos[i][j] != '-':
                ocupados += 1
                assentoStr = f"{chr(65+j)}{i+1}"
                ocupadosLista.append(assentoStr)
                if i < 6:
                    primeiraClasse += 1
                    valorPrimeiraClasse += precoPrimeiraClasse
                else:
                    classeNormal += 1
                    valorClasseNormal += precoClasseNormal
            j += 1
        i += 1
    totalPago = valorPrimeiraClasse + valorClasseNormal
    totalAssentos = numFileiras * numColunas
    vazios = totalAssentos - ocupados
    print("Relatório de Assentos:")
    print(f"Total de assentos ocupados: {ocupados}")
    print(f"Total de assentos vazios: {vazios}")
    print(f"Assentos ocupados: {', '.join(ocupadosLista)}")
    print(f"Quantidade de assentos na primeira classe: {primeiraClasse}")
    print(f"Quantidade de assentos na classe normal: {classeNormal}")
    print(f"Total pago (R$): {totalPago}")
    print(f"Total pago pela primeira classe (R$): {valorPrimeiraClasse}")
    print(f"Total pago pela classe normal (R$): {valorClasseNormal}")


assentos = inicializarAssentos()
print("Bem-vindo ao sistema de reservas de assentos da aeronave.")
print("Você pode começar a marcar assentos.")
while True:
    fileira = int(input("Digite a fileira (1 a 30) ou '0' para parar de marcar: ")) - 1
    if fileira == -1:
        break
    coluna = input("Digite a coluna (A a F): ").upper()
    nome = input("Digite o nome do passageiro: ")
    marcarAssento(assentos, fileira, ord(coluna) - 65, nome)
print("\nVocê parou de marcar assentos. O menu completo será exibido agora.")
while True:
    print("\nMenu:")
    print("1. Marcar assento")
    print("2. Desmarcar assento")
    print("3. Remarcar assento")
    print("4. Relatório")
    print("5. Mostrar mapa de assentos")
    print("6. Sair")
    opcao = input("Escolha uma opção: ")
    if opcao == '1':
        fileira = int(input("Digite a fileira (1 a 30): ")) - 1
        coluna = input("Digite a coluna (A a F): ").upper()
        nome = input("Digite o nome do passageiro: ")
        marcarAssento(assentos, fileira, ord(coluna) - 65, nome)
    elif opcao == '2':
        fileira = int(input("Digite a fileira (1 a 30): ")) - 1
        coluna = input("Digite a coluna (A a F): ").upper()
        desmarcarAssento(assentos, fileira, ord(coluna) - 65)
    elif opcao == '3':
        assentoAtual = input("Digite o assento atual (exemplo: A15): ").replace(' ', '')
        fileiraNova = int(input("Digite a nova fileira (1 a 30): ")) - 1
        colunaNova = input("Digite a nova coluna (A a F): ").upper()
        remarcarAssento(assentos, assentoAtual, fileiraNova, ord(colunaNova) - 65)
    elif opcao == '4':
        relatorioAssentos(assentos)
    elif opcao == '5':
        mostrarAssentos(assentos)
    elif opcao == '6':
        print("Encerrando sistema...")
        break
    else:
        print("Opção inválida. Tente novamente.")