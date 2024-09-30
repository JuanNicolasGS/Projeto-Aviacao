# Projeto-Aviacao

## 0rientações
<p>Ofereçam um menu ao usuário (no console)
para a escolha do que ele pode fazer.
Exemplo: menu com os possíveis relatórios.</p>

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
                

<p>Inicialmente vocês devem oferecer uma forma
de começar a marcar assentos, vários de uma
só vez e uma forma de parar de marcar
assentos.</p>
<p><b>OBS: O menu completo deve ser oferecido apenas
quando parar de marcar assentos.</b></p>

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