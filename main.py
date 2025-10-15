# main.py
from tarefas import GerenciadorTarefas

def menu():
    print("\n===== GERENCIADOR DE TAREFAS =====")
    print("1. Adicionar tarefa")
    print("2. Listar tarefas")
    print("3. Concluir tarefa")
    print("4. Remover tarefa")
    print("5. Sair")

def main():
    app = GerenciadorTarefas()

    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            descricao = input("Digite a descrição da tarefa: ")
            try:
                app.adicionar_tarefa(descricao)
                print("✅ Tarefa adicionada com sucesso!")
            except ValueError as e:
                print(f"Erro: {e}")

        elif opcao == "2":
            print("\n--- Lista de Tarefas ---")
            tarefas = app.listar_tarefas()
            if not tarefas:
                print("Nenhuma tarefa cadastrada.")
            else:
                for i, t in enumerate(tarefas):
                    status = "✔️" if t["concluida"] else "❌"
                    print(f"{i+1}. {t['descricao']} - {status}")

        elif opcao == "3":
            try:
                indice = int(input("Número da tarefa a concluir: ")) - 1
                app.concluir_tarefa(indice)
                print("✅ Tarefa concluída!")
            except (ValueError, IndexError) as e:
                print(f"Erro: {e}")

        elif opcao == "4":
            try:
                indice = int(input("Número da tarefa a remover: ")) - 1
                app.remover_tarefa(indice)
                print("🗑️ Tarefa removida.")
            except (ValueError, IndexError) as e:
                print(f"Erro: {e}")

        elif opcao == "5":
            print("Saindo... 👋")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
