# Constantes globais
NUM_FILEIRAS = 30
NUM_COLUNAS = 6
PRECO_PRIMEIRA_CLASSE = 100.0
PRECO_CLASSE_NORMAL = 80.0

# Inicializando os assentos como um grid vazio ('-' para assento disponível)
def inicializar_assentos():
    assentos = []
    for _ in range(NUM_FILEIRAS):
        fileira = []
        for _ in range(NUM_COLUNAS):
            fileira.append('-')
        assentos.append(fileira)
    return assentos

# Exibir o mapa de assentos
def mostrar_assentos(assentos):
    print("Mapa de Assentos (colunas A a F):")
    for i in range(len(assentos)):
        fileira = f"{i+1:02d}"
        print(f"Fileira {fileira}: {assentos[i]}")

# Verificar se o assento está disponível
def verificar_disponibilidade(assentos, fileira, coluna):
    if assentos[fileira][coluna] == '-':
        return True
    return False

# Marcar um assento para um passageiro
def marcar_assento(assentos, fileira, coluna, nome):
    if verificar_disponibilidade(assentos, fileira, coluna):
        assentos[fileira][coluna] = nome
        print(f"Assento {chr(65 + coluna)}{fileira+1} reservado para {nome}.")
    else:
        print(f"Assento {chr(65 + coluna)}{fileira+1} já está ocupado.")

# Desmarcar um assento
def desmarcar_assento(assentos, fileira, coluna):
    if not verificar_disponibilidade(assentos, fileira, coluna):
        print(f"Assento {chr(65 + coluna)}{fileira+1} desmarcado.")
        assentos[fileira][coluna] = '-'
    else:
        print(f"O assento {chr(65 + coluna)}{fileira+1} já está vazio.")

# Remarcar um assento
def remarcar_assento(assentos, assento_atual, fileira_nova, coluna_nova):
    coluna_atual = ord(assento_atual[0].upper()) - 65
    fileira_atual = int(assento_atual[1:]) - 1

    if not verificar_disponibilidade(assentos, fileira_atual, coluna_atual):
        nome = assentos[fileira_atual][coluna_atual]
        desmarcar_assento(assentos, fileira_atual, coluna_atual)
        marcar_assento(assentos, fileira_nova, coluna_nova, nome)
    else:
        print(f"O assento {assento_atual} já está vazio.")

# Gerar relatório de ocupação e pagamento
def relatorio_assentos(assentos):
    ocupados = 0
    primeira_classe = 0
    classe_normal = 0
    valor_primeira_classe = 0
    valor_classe_normal = 0
    ocupados_lista = []

    i = 0
    while i < len(assentos):
        j = 0
        while j < NUM_COLUNAS:
            if assentos[i][j] != '-':
                ocupados += 1
                assento_str = f"{chr(65+j)}{i+1}"
                ocupados_lista.append(assento_str)
                if i < 6:
                    primeira_classe += 1
                    valor_primeira_classe += PRECO_PRIMEIRA_CLASSE
                else:
                    classe_normal += 1
                    valor_classe_normal += PRECO_CLASSE_NORMAL
            j += 1
        i += 1

    total_pago = valor_primeira_classe + valor_classe_normal
    total_assentos = NUM_FILEIRAS * NUM_COLUNAS
    vazios = total_assentos - ocupados

    print("Relatório de Assentos:")
    print(f"Total de assentos ocupados: {ocupados}")
    print(f"Total de assentos vazios: {vazios}")
    print(f"Assentos ocupados: {', '.join(ocupados_lista)}")
    print(f"Quantidade de assentos na primeira classe: {primeira_classe}")
    print(f"Quantidade de assentos na classe normal: {classe_normal}")
    print(f"Total pago (R$): {total_pago}")
    print(f"Total pago pela primeira classe (R$): {valor_primeira_classe}")
    print(f"Total pago pela classe normal (R$): {valor_classe_normal}")

# Função principal do sistema
def main():
    assentos = inicializar_assentos()

    print("Bem-vindo ao sistema de reservas de assentos da aeronave.")
    print("Você pode começar a marcar assentos.")

    # Etapa de marcação inicial de vários assentos
    while True:
        fileira = int(input("Digite a fileira (1 a 30) ou '0' para parar de marcar: ")) - 1
        if fileira == -1:
            break
        coluna = input("Digite a coluna (A a F): ").upper()
        nome = input("Digite o nome do passageiro: ")
        marcar_assento(assentos, fileira, ord(coluna) - 65, nome)

    print("\nVocê parou de marcar assentos. O menu completo será exibido agora.")

    # Menu completo após a marcação inicial
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
            marcar_assento(assentos, fileira, ord(coluna) - 65, nome)

        elif opcao == '2':
            fileira = int(input("Digite a fileira (1 a 30): ")) - 1
            coluna = input("Digite a coluna (A a F): ").upper()
            desmarcar_assento(assentos, fileira, ord(coluna) - 65)

        elif opcao == '3':
            assento_atual = input("Digite o assento atual (exemplo: A15): ").replace(' ', '')
            fileira_nova = int(input("Digite a nova fileira (1 a 30): ")) - 1
            coluna_nova = input("Digite a nova coluna (A a F): ").upper()
            remarcar_assento(assentos, assento_atual, fileira_nova, ord(coluna_nova) - 65)

        elif opcao == '4':
            relatorio_assentos(assentos)

        elif opcao == '5':
            mostrar_assentos(assentos)

        elif opcao == '6':
            print("Encerrando sistema...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()