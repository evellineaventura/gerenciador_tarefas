
import unittest
from tarefas import GerenciadorTarefas

class TestGerenciadorTarefas(unittest.TestCase):

    def setUp(self):
        self.app = GerenciadorTarefas()

    def test_adicionar_tarefa(self):
        self.app.adicionar_tarefa("Estudar Python")
        self.assertEqual(len(self.app.tarefas), 1)

    def test_nao_adicionar_tarefa_vazia(self):
        with self.assertRaises(ValueError):
            self.app.adicionar_tarefa("   ")

    def test_concluir_tarefa(self):
        self.app.adicionar_tarefa("Estudar Java")
        self.app.concluir_tarefa(0)
        self.assertTrue(self.app.tarefas[0]["concluida"])

    def test_remover_tarefa(self):
        self.app.adicionar_tarefa("Fazer exercício")
        self.app.remover_tarefa(0)
        self.assertEqual(len(self.app.tarefas), 0)

    def test_indice_invalido(self):
        with self.assertRaises(IndexError):
            self.app.concluir_tarefa(5)

if __name__ == "__main__":
    unittest.main()
