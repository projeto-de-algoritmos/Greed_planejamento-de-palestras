import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class Palestra:
    def __init__(self, nome, tempo_total):
        self.nome = nome
        self.tempo_total = tempo_total

def otimizar_palestras(palestras):
    palestras_ordenadas = sorted(palestras, key=lambda palestra: palestra.tempo_total[1])
    horario_atual = 0
    palestras_agendadas = []

    for palestra in palestras_ordenadas:
        if palestra.tempo_total[0] >= horario_atual:
            palestras_agendadas.append(palestra)
            horario_atual = palestra.tempo_total[1]

    return palestras_agendadas

def adicionar_palestra():
    nome = nome_entry.get()
    horario_inicio = horario_inicio_entry.get()
    horario_fim = horario_fim_entry.get()

    try:
        horario_inicio = int(horario_inicio)
        horario_fim = int(horario_fim)

        if horario_inicio >= horario_fim:
            tk.messagebox.showerror("Erro de Validação", "O início da janela deve ser anterior ao fim da janela.")
        else:
            palestra = Palestra(nome, (horario_inicio, horario_fim))
            palestras.append(palestra)
            tree.insert("", "end", values=(palestra.nome, palestra.tempo_total))
            nome_entry.delete(0, tk.END)
            horario_inicio_entry.delete(0, tk.END)
            horario_fim_entry.delete(0, tk.END)
    except ValueError:
        tk.messagebox.showerror("Erro de Validação", "Os valores de início e fim devem ser números inteiros.")

def otimizar_palestras_e_mostrar():
    if not palestras:
        tk.messegebox.showarning("Aviso", "Nenhuma palestra para otimizar.")
        return

    palestras_otimizadas = otimizar_palestras(palestras)

    for row in tree.get_children():
        tree.delete(row)

    for palestra in palestras_otimizadas:
        tree.insert("", "end", values=(palestra.nome, palestra.tempo_total))

def excluir_palestra():
    selected_item = tree.selection()
    if selected_item:
        for item in selected_item:
            index = tree.index(item)
            del palestras[index]
            tree.delete(item)

palestras = []


root = tk.Tk()
root.title("Planejamento de palestras em evento")

frame = ttk.Frame(root)
frame.pack(padx=10, pady=10)

ttk.Label(frame, text="Planejamento de Palestras").grid(row=0, columnspan=4)

ttk.Label(frame, text="Nome:").grid(row=1, column=0)
nome_entry = ttk.Entry(frame)
nome_entry.grid(row=1, column=1)
ttk.Label(frame, text="Horario de inicio(numero inteiro):").grid(row=1, column=2)
horario_inicio_entry = ttk.Entry(frame)
horario_inicio_entry.grid(row=1, column=3)
ttk.Label(frame, text="Horario de termino(numero inteiro):").grid(row=1, column=4)
horario_fim_entry = ttk.Entry(frame)
horario_fim_entry.grid(row=1, column=5)

ttk.Button(frame, text="Adicionar palestra", command=adicionar_palestra).grid(row=2, column=6)
ttk.Button(frame, text="Otimizar evento", command=otimizar_palestras_e_mostrar).grid(row=3, column=6)
ttk.Button(frame, text="Excluir palestra", command=excluir_palestra).grid(row=4, column=6)

tree = ttk.Treeview(frame, columns=("Nome", "Tempo"))
tree.heading("#1", text="Nome")
tree.heading("#2", text="Tempo")
tree.column("#1", width=200)
tree.column("#2", width=200)
tree.grid(row=5, columnspan=7)

root.mainloop()