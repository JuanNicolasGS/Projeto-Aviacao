numFileiras = 30
numColunas = 6
precoPrimeiraClasse = 100.0
precoClasseNormal = 80.0
colunasValidas = ['A', 'B', 'C', 'D', 'E', 'F']

def linhas():
    print("-"*200)

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

def validarAssento(fileira, coluna):
    if 0 <= fileira < numFileiras and coluna in colunasValidas:
        return True
    return False

def marcarAssento(assentos, fileira, coluna, nome):
    colunaIndex = colunasValidas.index(coluna)
    if verificarDisponibilidade(assentos, fileira, colunaIndex):
        assentos[fileira][colunaIndex] = nome
        print(f"Assento {coluna}{fileira+1} reservado para {nome}.")
        linhas()
    else:
        print(f"Assento {coluna}{fileira+1} já está ocupado.")

def desmarcarAssento(assentos, fileira, coluna):
    colunaIndex = colunasValidas.index(coluna)
    if not verificarDisponibilidade(assentos, fileira, colunaIndex):
        print(f"Assento {coluna}{fileira+1} desmarcado.")
        assentos[fileira][colunaIndex] = '-'
    else:
        print(f"O assento {coluna}{fileira+1} já está vazio.")

def remarcarAssento(assentos, assentoAtual, fileiraNova, colunaNova):
    colunaAtual = assentoAtual[0].upper()
    fileiraAtual = int(assentoAtual[1:]) - 1
    if validarAssento(fileiraAtual, colunaAtual):
        colunaIndexAtual = colunasValidas.index(colunaAtual)
        if not verificarDisponibilidade(assentos, fileiraAtual, colunaIndexAtual):
            nome = assentos[fileiraAtual][colunaIndexAtual]
            print(f"Assento {colunaAtual}{fileiraAtual + 1} será liberado.")
            desmarcarAssento(assentos, fileiraAtual, colunaAtual)
            marcarAssento(assentos, fileiraNova, colunaNova, nome)
        else:
            print(f"O assento {assentoAtual} já está vazio.")
    else:
        print(f"Assento {assentoAtual} inválido.")

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
                assentoStr = f"{colunasValidas[j]}{i+1}"
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

linhas()
assentos = inicializarAssentos()
print("Bem-vindo ao sistema de reservas de assentos da aeronave.")
print("Você pode começar a marcar assentos.")
while True:
    fileira = int(input("Digite a fileira (1 a 30) ou '0' para parar de marcar: ")) - 1
    if fileira == -1:
        break
    coluna = input("Digite a coluna (A a F): ").upper()
    if validarAssento(fileira, coluna):
        nome = input("Digite o nome do passageiro: ")
        marcarAssento(assentos, fileira, coluna, nome)
    else:
        print("Assento inválido. Por favor, insira uma fileira entre 1 e 30 e uma coluna entre A e F.")
print("\nVocê parou de marcar assentos. O menu completo será exibido agora.")

def Menu():
    linhas()
    print("\nMenu:")
    print("1. Marcar assento")
    print("2. Desmarcar assento")
    print("3. Remarcar assento")
    print("4. Relatório")
    print("5. Mostrar mapa de assentos")
    print("6. Sair")
    linhas()

while True:
    Menu()

    opcao = input("Escolha uma opção: ")
    if opcao == '1':
        fileira = int(input("Digite a fileira (1 a 30): ")) - 1
        coluna = input("Digite a coluna (A a F): ").upper()
        if validarAssento(fileira, coluna):
            nome = input("Digite o nome do passageiro: ")
            marcarAssento(assentos, fileira, coluna, nome)
        else:
            print("Assento inválido.")
    elif opcao == '2':
        fileira = int(input("Digite a fileira (1 a 30): ")) - 1
        coluna = input("Digite a coluna (A a F): ").upper()
        if validarAssento(fileira, coluna):
            desmarcarAssento(assentos, fileira, coluna)
        else:
            print("Assento inválido.")
    elif opcao == '3':
        assentoAtual = input("Digite o assento atual (exemplo: A15): ").replace(' ', '')
        fileiraNova = int(input("Digite a nova fileira (1 a 30): ")) - 1
        colunaNova = input("Digite a nova coluna (A a F): ").upper()
        if validarAssento(fileiraNova, colunaNova):
            remarcarAssento(assentos, assentoAtual, fileiraNova, colunaNova)
        else:
            print("Novo assento inválido.")
    elif opcao == '4':
        relatorioAssentos(assentos)
    elif opcao == '5':
        mostrarAssentos(assentos)
    elif opcao == '6':
        print("Encerrando sistema...")
        break
    else:
        print("Opção inválida. Tente novamente.")