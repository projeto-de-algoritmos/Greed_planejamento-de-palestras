import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class Palestra:
    def __init__(self, nome, tempo_total):
        self.nome = nome
        self.tempo_total = tempo_total

class App:
    def __init__(self, master=None):
        self.palestras = []
        #Fonte padrão
        self.fontePadrao = ("Arial", "10")

        #Containers
        self.container1 = Frame(master)
        self.container1["pady"] = 10
        self.container1.pack()

        self.container2 = Frame(master)
        self.container2["padx"] = 20
        self.container2.pack()

        self.container3 = Frame(master)
        self.container3["padx"] = 20
        self.container3.pack()

        self.container4 = Frame(master)
        self.container4["pady"] = 20
        self.container4.pack()

        self.container5 = Frame(master)
        self.container5["pady"] = 20
        self.container5.pack()

        self.container6 = Frame(master)
        self.container6["pady"] = 20
        self.container6.pack()

        self.container7 = Frame(master)
        self.container7["pady"] = 20
        self.container7.pack()

        self.container8 = Frame(master)
        self.container8["pady"] = 20
        self.container8.pack()                

        #titulo
        self.titulo = Label(self.container1, text="Cadastro de Palestra")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        #Nome
        self.nomeLabel = Label(self.container2,text="Nome", font=self.fontePadrao)
        self.nomeLabel.pack(side=LEFT)

        self.nome_entry = Entry(self.container2)
        self.nome_entry["width"] = 30
        self.nome_entry["font"] = self.fontePadrao
        self.nome_entry.pack(side=LEFT)

        #Horario de Inicio
        self.horario_inicio_Label = Label(self.container3, text="Horario de Inicio", font=self.fontePadrao)
        self.horario_inicio_Label.pack(side=LEFT)

        self.horario_inicio_entry = Entry(self.container3)
        self.horario_inicio_entry["width"] = 30
        self.horario_inicio_entry["font"] = self.fontePadrao
        self.horario_inicio_entry.pack(side=LEFT)

        #Horario de Fim
        self.horario_fim_Label = Label(self.container4, text="Horario de Fim", font=self.fontePadrao)
        self.horario_fim_Label.pack(side=LEFT)

        self.horario_fim_entry = Entry(self.container4)
        self.horario_fim_entry["width"] = 30
        self.horario_fim_entry["font"] = self.fontePadrao
        self.horario_fim_entry.pack(side=LEFT)

        #Botao adicionar palestra
        self.addicionar_palestra = Button(self.container5)
        self.addicionar_palestra["text"] = "Adicionar Palestra"
        self.addicionar_palestra["font"] = ("Calibri", "8")
        self.addicionar_palestra["width"] = 12
        self.addicionar_palestra["command"] = self.adicionar_palestra
        self.addicionar_palestra.pack()

        #Local para ver quais palestras tem
        self.tree = ttk.Treeview(self.container6, columns=("Nome", "Horario Incio", ))
        self.tree.heading("#1", text="Nome")
        self.tree.heading("#2", text="Tempo")
        self.tree.column("#1", width=200)
        self.tree.column("#2", width=200)
        self.tree.grid(row=5, columnspan=7)

        columns = ('first_name', 'last_name', 'email')

        tree = ttk.Treeview(root, columns=columns, show='headings')

        # define headings
        tree.heading('first_name', text='First Name')
        tree.heading('last_name', text='Last Name')
        tree.heading('email', text='Email')

        #Botao otimizar evento
        self.addicionar_palestra = Button(self.container7)
        self.addicionar_palestra["text"] = "Otimizar evento"
        self.addicionar_palestra["font"] = ("Calibri", "8")
        self.addicionar_palestra["width"] = 12
        self.addicionar_palestra["command"] = self.otimizar_palestras_e_mostrar
        self.addicionar_palestra.pack()

        #Botao excluir palestra
        self.addicionar_palestra = Button(self.container8)
        self.addicionar_palestra["text"] = "Excluir palestra"
        self.addicionar_palestra["font"] = ("Calibri", "8")
        self.addicionar_palestra["width"] = 12
        self.addicionar_palestra["command"] = self.excluir_palestra
        self.addicionar_palestra.pack()

    #Método verificar horario_inicio
    def verificahorario_inicio(self):
        usuario = self.nome.get()
        horario_inicio = self.horario_inicio.get()
        if usuario == "usuariodevmedia" and horario_inicio == "dev":
            self.mensagem["text"] = "Autenticado"
        else:
            self.mensagem["text"] = "Erro na autenticação"
    
    #função de adicionar palestra
    def adicionar_palestra(self):
        nome = self.nome_entry.get()
        horario_inicio = self.horario_inicio_entry.get()
        horario_fim = self.horario_fim_entry.get()
        try:
            horario_inicio = int(horario_inicio)
            horario_fim = int(horario_fim)
            if horario_inicio >= horario_fim:
                tk.messagebox.showerror("Erro de Validação", "O início da janela deve ser anterior ao fim da janela.")
            else:
                palestra = Palestra(nome, (horario_inicio, horario_fim))
                self.palestras.append(palestra)
                self.tree.insert("", "end", values=(palestra.nome, palestra.tempo_total))
                self.nome_entry.delete(0, tk.END)
                self.horario_inicio_entry.delete(0, tk.END)
                self.horario_fim_entry.delete(0, tk.END)
        except ValueError:
            tk.messagebox.showerror("Erro de Validação", "Os valores de início e fim devem ser números inteiros.")
    
    #Função Otimizar Palestras
    def otimizar_palestras(self):
        palestras_ordenadas = sorted(self.palestras, key=lambda palestra: palestra.tempo_total[1])
        horario_atual = 0
        palestras_agendadas = []
        for palestra in palestras_ordenadas:
            if palestra.tempo_total[0] >= horario_atual:
                palestras_agendadas.append(palestra)
                horario_atual = palestra.tempo_total[1]
        return palestras_agendadas
    
    #Otimizar e mostrar
    def otimizar_palestras_e_mostrar(self):
        if not self.palestras:
            tk.messegebox.showarning("Aviso", "Nenhuma palestra para otimizar.")
            return
        palestras_otimizadas = self.otimizar_palestras()
        for row in self.tree.get_children():
            self.tree.delete(row)

        for palestra in palestras_otimizadas:
            self.tree.insert("", "end", values=(palestra.nome, palestra.tempo_total))

    def excluir_palestra(self):
        selected_item = self.tree.selection()
        if selected_item:
            for item in selected_item:
                index = self.tree.index(item)
                del self.palestras[index]
                self.tree.delete(item)



root = Tk()
App(root)

w = 1000
h = 1000

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width/2) - (w/2)
y = (screen_height/2) - (h/2)

root.geometry('%dx%d+%d+%d' % (w, h, x, y))

root.title("Planejamento de palestras em evento")

root.mainloop()