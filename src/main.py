import tkinter as tk
from tkinter import ttk

class Entrega:
    def __init__(self, localizacao, janela_tempo):
        self.localizacao = localizacao
        self.janela_tempo = janela_tempo

def otimizar_entregas(entregas):
    entregas_ordenadas = sorted(entregas, key=lambda entrega: entrega.janela_tempo[1])
    horario_atual = 0
    entregas_agendadas = []

    for entrega in entregas_ordenadas:
        if entrega.janela_tempo[0] >= horario_atual:
            entregas_agendadas.append(entrega)
            horario_atual = entrega.janela_tempo[1]

    return entregas_agendadas

def otimizar_entregas_e_mostrar():
    entregas = []
    error_messages = []

    for row in tree.get_children():
        tree.delete(row)

    for i in range(len(entrega_entries)):
        localizacao = entrega_entries[i][0].get()
        inicio_janela = entrega_entries[i][1].get()
        fim_janela = entrega_entries[i][2].get()

        try:
            inicio_janela = int(inicio_janela)
            fim_janela = int(fim_janela)

            if inicio_janela >= fim_janela:
                error_messages.append(f"Erro na entrega {i+1}: O início da janela deve ser anterior ao fim da janela.")
            else:
                entrega = Entrega(localizacao, (inicio_janela, fim_janela))
                entregas.append(entrega)
        except ValueError:
            error_messages.append(f"Erro na entrega {i+1}: Os valores de início e fim da janela devem ser números inteiros.")

    if error_messages:
        error_message = "\n".join(error_messages)
        tk.messagebox.showerror("Erros de Validação", error_message)
    else:
        entregas_otimizadas = otimizar_entregas(entregas)

        for entrega in entregas_otimizadas:
            tree.insert("", "end", values=(entrega.localizacao, entrega.janela_tempo))

def excluir_entrega():
    selected_item = tree.selection()
    if selected_item:
        for item in selected_item:
            tree.delete(item)

root = tk.Tk()
root.title("Planejamento de palestras em evento")

frame = ttk.Frame(root)
frame.pack(padx=10, pady=10)

ttk.Label(frame, text="Entregas (Localização, Janela de Tempo):").grid(row=0, columnspan=3)

entrega_entries = []

for i in range(3):
    ttk.Label(frame, text="Localização:").grid(row=i+1, column=0)
    localizacao_entry = ttk.Entry(frame)
    localizacao_entry.grid(row=i+1, column=1)
    ttk.Label(frame, text="Início do Envento:").grid(row=i+1, column=2)
    inicio_janela_entry = ttk.Entry(frame)
    inicio_janela_entry.grid(row=i+1, column=3)
    ttk.Label(frame, text="Fim do Evento:").grid(row=i+1, column=4)
    fim_janela_entry = ttk.Entry(frame)
    fim_janela_entry.grid(row=i+1, column=5)
    entrega_entries.append((localizacao_entry, inicio_janela_entry, fim_janela_entry))

ttk.Button(frame, text="Gerar Maximo de eventos", command=otimizar_entregas_e_mostrar).grid(row=4, column=6)
ttk.Button(frame, text="Excluir Entrega", command=excluir_entrega).grid(row=5, column=6)

tree = ttk.Treeview(frame, columns=("Localização", "Tempo"))
tree.heading("#1", text="Localização")
tree.heading("#2", text="Tempo")
tree.column("#1", width=200)
tree.column("#2", width=200)
tree.grid(row=6, columnspan=7)

root.mainloop()