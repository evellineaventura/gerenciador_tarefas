
class GerenciadorTarefas:
    def __init__(self):
        self.tarefas = []

    def adicionar_tarefa(self, descricao):
        if not descricao.strip():
            raise ValueError("A descrição da tarefa não pode ser vazia.")
        self.tarefas.append({"descricao": descricao, "concluida": False})

    def listar_tarefas(self):
        return self.tarefas

    def concluir_tarefa(self, indice):
        if indice < 0 or indice >= len(self.tarefas):
            raise IndexError("Tarefa não encontrada.")
        self.tarefas[indice]["concluida"] = True

    def remover_tarefa(self, indice):
        if indice < 0 or indice >= len(self.tarefas):
            raise IndexError("Tarefa não encontrada.")
        del self.tarefas[indice]
