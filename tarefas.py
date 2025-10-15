
import json
import os

class GerenciadorTarefas:
    def __init__(self, arquivo_dados="tarefas.json"):
        self.arquivo_dados = arquivo_dados
        self.tarefas = []
        self.carregar_tarefas()

    def carregar_tarefas(self):
        """Carrega as tarefas do arquivo JSON, se existir."""
        if os.path.exists(self.arquivo_dados):
            try:
                with open(self.arquivo_dados, "r", encoding="utf-8") as f:
                    self.tarefas = json.load(f)
            except (json.JSONDecodeError, FileNotFoundError):
                self.tarefas = []
        else:
            self.tarefas = []

    def salvar_tarefas(self):
        """Salva as tarefas no arquivo JSON."""
        with open(self.arquivo_dados, "w", encoding="utf-8") as f:
            json.dump(self.tarefas, f, indent=4, ensure_ascii=False)

    def adicionar_tarefa(self, descricao):
        if not descricao.strip():
            raise ValueError("A descrição da tarefa não pode ser vazia.")
        self.tarefas.append({"descricao": descricao, "concluida": False})
        self.salvar_tarefas()

    def listar_tarefas(self):
        return self.tarefas

    def concluir_tarefa(self, indice):
        if indice < 0 or indice >= len(self.tarefas):
            raise IndexError("Tarefa não encontrada.")
        self.tarefas[indice]["concluida"] = True
        self.salvar_tarefas()

    def remover_tarefa(self, indice):
        if indice < 0 or indice >= len(self.tarefas):
            raise IndexError("Tarefa não encontrada.")
        del self.tarefas[indice]
        self.salvar_tarefas()

    def limpar_tarefas(self):
        self.tarefas = []
        self.salvar_tarefas()
