class Aeronave:
    def __init__(self):
        self.assentos = [['-' for _ in range(6)] for _ in range(30)]
        self.preco_primeira_classe = 100.0
        self.preco_classe_normal = 80.0

    def mostrar_assentos(self):
        for i in range(len(self.assentos)):
            fileira = chr(65 + i % 6)
            print(f"Fileira {i+1} - {fileira}: {self.assentos[i]}")

    def verificar_disponibilidade(self, fileira, coluna):
        if self.assentos[fileira][coluna] == '-':
            return True
        return False

    def marcar_assento(self, fileira, coluna, nome):
        if self.verificar_disponibilidade(fileira, coluna):
            self.assentos[fileira][coluna] = nome
            print(f"Assento {chr(65 + coluna)}{fileira+1} reservado para {nome}.")
        else:
            print(f"Assento {chr(65 + coluna)}{fileira+1} já está ocupado.")

    def desmarcar_assento(self, fileira, coluna):
        if not self.verificar_disponibilidade(fileira, coluna):
            print(f"Assento {chr(65 + coluna)}{fileira+1} desmarcado.")
            self.assentos[fileira][coluna] = '-'
        else:
            print(f"O assento {chr(65 + coluna)}{fileira+1} já está vazio.")

    def remarcar_assento(self, assento_atual, fileira_nova, coluna_nova):
        coluna_atual = ord(assento_atual[0].upper()) - 65
        fileira_atual = int(assento_atual[1:]) - 1

        if not self.verificar_disponibilidade(fileira_atual, coluna_atual):
            nome = self.assentos[fileira_atual][coluna_atual]
            self.desmarcar_assento(fileira_atual, coluna_atual)
            self.marcar_assento(fileira_nova, coluna_nova, nome)
        else:
            print(f"O assento {assento_atual} já está vazio.")

    def relatorio_assentos(self):
        ocupados = 0
        primeira_classe = 0
        classe_normal = 0
        valor_primeira_classe = 0
        valor_classe_normal = 0
        ocupados_lista = []

        for i in range(len(self.assentos)):
            for j in range(6):
                if self.assentos[i][j] != '-':
                    ocupados += 1
                    assento_str = f"{chr(65+j)}{i+1}"
                    ocupados_lista.append(assento_str)
                    if i < 6:
                        primeira_classe += 1
                        valor_primeira_classe += self.preco_primeira_classe
                    else:
                        classe_normal += 1
                        valor_classe_normal += self.preco_classe_normal

        total_pago = valor_primeira_classe + valor_classe_normal
        total_assentos = 30 * 6
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

# Interface para o atendente
def main():
    aeronave = Aeronave()

    print("Bem-vindo ao sistema de reservas de assentos da aeronave.")
    print("Você pode começar a marcar assentos.")

    # Etapa de marcação inicial de vários assentos
    while True:
        fileira = int(input("Digite a fileira (1 a 30) ou '0' para parar de marcar: ")) - 1
        if fileira == -1:
            break
        coluna = input("Digite a coluna (A a F): ").upper()
        nome = input("Digite o nome do passageiro: ")
        aeronave.marcar_assento(fileira, ord(coluna) - 65, nome)

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
            aeronave.marcar_assento(fileira, ord(coluna) - 65, nome)

        elif opcao == '2':
            fileira = int(input("Digite a fileira (1 a 30): ")) - 1
            coluna = input("Digite a coluna (A a F): ").upper()
            aeronave.desmarcar_assento(fileira, ord(coluna) - 65)

        elif opcao == '3':
            assento_atual = input("Digite o assento atual (exemplo: A 15): ")
            fileira_nova = int(input("Digite a nova fileira (1 a 30): ")) - 1
            coluna_nova = input("Digite a nova coluna (A a F): ").upper()
            aeronave.remarcar_assento(assento_atual, fileira_nova, ord(coluna_nova) - 65)

        elif opcao == '4':
            aeronave.relatorio_assentos()

        elif opcao == '5':
            aeronave.mostrar_assentos()

        elif opcao == '6':
            print("Encerrando sistema...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()