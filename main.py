import tkinter as tk
from tkinter import messagebox
from tarefas import GerenciadorTarefas

class AppGerenciadorTarefas:
    def __init__(self, root):
        self.root = root
        self.root.title("🗂️ Gerenciador de Tarefas")
        self.root.geometry("500x570")
        self.root.configure(bg="#1E1E1E")

        self.gerenciador = GerenciadorTarefas()

        
        titulo = tk.Label(
            self.root,
            text="🗓️ GERENCIADOR DE TAREFAS",
            font=("Segoe UI", 18, "bold"),
            bg="#1E1E1E",
            fg="#00ADB5",
        )
        titulo.pack(pady=15)

        
        self.frame_top = tk.Frame(self.root, bg="#1E1E1E")
        self.frame_top.pack(pady=10)

        self.entry_tarefa = tk.Entry(
            self.frame_top,
            width=32,
            font=("Segoe UI", 12),
            bg="#2E2E2E",
            fg="#FFFFFF",
            insertbackground="white",
            relief="flat",
        )
        self.entry_tarefa.grid(row=0, column=0, padx=5)

        self.btn_adicionar = tk.Button(
            self.frame_top,
            text="➕ Adicionar",
            command=self.adicionar_tarefa,
            bg="#00ADB5",
            fg="white",
            font=("Segoe UI", 11, "bold"),
            relief="flat",
            activebackground="#00CED1",
            cursor="hand2",
            width=12
        )
        self.btn_adicionar.grid(row=0, column=1, padx=8)

        #Lista de tarefas
        self.listbox = tk.Listbox(
            self.root,
            width=55,
            height=15,
            font=("Consolas", 11),
            bg="#2E2E2E",
            fg="#EEEEEE",
            selectbackground="#00ADB5",
            selectforeground="#000000",
            borderwidth=0,
            highlightthickness=0,
        )
        self.listbox.pack(pady=15)

        #Botões inferiores
        self.frame_bottom = tk.Frame(self.root, bg="#1E1E1E")
        self.frame_bottom.pack(pady=10)

        self.btn_concluir = tk.Button(
            self.frame_bottom,
            text="✅ Concluir",
            command=self.concluir_tarefa,
            bg="#007ACC",
            fg="white",
            font=("Segoe UI", 11, "bold"),
            relief="flat",
            activebackground="#0099FF",
            cursor="hand2",
            width=12
        )
        self.btn_concluir.grid(row=0, column=0, padx=8)

        self.btn_remover = tk.Button(
            self.frame_bottom,
            text="🗑️ Remover",
            command=self.remover_tarefa,
            bg="#FF4B5C",
            fg="white",
            font=("Segoe UI", 11, "bold"),
            relief="flat",
            activebackground="#FF6B6B",
            cursor="hand2",
            width=12
        )
        self.btn_remover.grid(row=0, column=1, padx=8)

        self.btn_limpar = tk.Button(
            self.frame_bottom,
            text="🧹 Limpar Todas",
            command=self.limpar_tarefas,
            bg="#FFB300",
            fg="white",
            font=("Segoe UI", 11, "bold"),
            relief="flat",
            activebackground="#FFD54F",
            cursor="hand2",
            width=12
        )
        self.btn_limpar.grid(row=0, column=2, padx=8)

        self.btn_sair = tk.Button(
            self.frame_bottom,
            text="🚪 Sair",
            command=self.root.quit,
            bg="#393E46",
            fg="white",
            font=("Segoe UI", 11, "bold"),
            relief="flat",
            activebackground="#50575F",
            cursor="hand2",
            width=12
        )
        self.btn_sair.grid(row=0, column=3, padx=8)

        self.label_contador = tk.Label(
            self.root,
            text="Carregando tarefas...",
            font=("Segoe UI", 11, "italic"),
            bg="#1E1E1E",
            fg="#AAAAAA"
        )
        self.label_contador.pack(pady=10)

        self.atualizar_lista()

    #Funções 
    def adicionar_tarefa(self):
        descricao = self.entry_tarefa.get()
        try:
            self.gerenciador.adicionar_tarefa(descricao)
            self.entry_tarefa.delete(0, tk.END)
            self.atualizar_lista()
        except ValueError as e:
            messagebox.showerror("Erro", str(e))

    def concluir_tarefa(self):
        try:
            indice = self.listbox.curselection()[0]
            self.gerenciador.concluir_tarefa(indice)
            self.atualizar_lista()
        except IndexError:
            messagebox.showwarning("Aviso", "Selecione uma tarefa para concluir.")

    def remover_tarefa(self):
        try:
            indice = self.listbox.curselection()[0]
            self.gerenciador.remover_tarefa(indice)
            self.atualizar_lista()
        except IndexError:
            messagebox.showwarning("Aviso", "Selecione uma tarefa para remover.")

    def limpar_tarefas(self):
        resposta = messagebox.askyesno("Confirmação", "Deseja realmente apagar todas as tarefas?")
        if resposta:
            self.gerenciador.limpar_tarefas()
            self.atualizar_lista()
            messagebox.showinfo("Sucesso", "Todas as tarefas foram removidas!")

    def atualizar_lista(self):
        self.listbox.delete(0, tk.END)
        tarefas = self.gerenciador.listar_tarefas()

        # Atualiza listbox
        for i, tarefa in enumerate(tarefas):
            status = "✔️" if tarefa["concluida"] else "❌"
            self.listbox.insert(tk.END, f"{i+1}. {tarefa['descricao']} {status}")

        # Atualiza o rodapé
        total = len(tarefas)
        concluidas = sum(1 for t in tarefas if t["concluida"])
        pendentes = total - concluidas
        self.label_contador.config(
            text=f"📋 Total: {total} | ⏳ Pendentes: {pendentes} | ✅ Concluídas: {concluidas}"
        )

 #excuta
if __name__ == "__main__":
    root = tk.Tk()
    app = AppGerenciadorTarefas(root)
    root.mainloop()


if __name__ == "__main__":
    main()

