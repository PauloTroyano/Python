"""
Exemplo simples: programa que fica esperando o usuário digitar comandos
e executa uma ação diferente para cada um.
"""

def main():
    print("Digite um comando (ou 'ajuda' para ver as opções).")

    while True:
        comando = input("> ").strip().lower()

        if comando == "sair":
            print("Encerrando o programa...")
            break

        elif comando == "ajuda":
            print("Comandos disponíveis:")
            print("  ajuda  - mostra esta mensagem")
            print("  hora   - mostra a data e hora atual")
            print("  sair   - encerra o programa")

        elif comando == "hora":
            from datetime import datetime
            print("Agora são:", datetime.now().strftime("%d/%m/%Y %H:%M:%S"))

        elif comando == "":
            continue

        else:
            print(f"Comando '{comando}' não reconhecido. Digite 'ajuda' para ver as opções.")


if __name__ == "__main__":
    main()