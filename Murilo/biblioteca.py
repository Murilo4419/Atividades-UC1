import tkinter as tk

janela = tk.Tk()
janela.title("Meu primeiro aplicativo")
janela.geometry("400x300")


titulo = tk.Label(
    janela,
    text="Cadastro de Alunos",
    font=("Arial", 16)
)

titulo.pack()
campo_nome = tk.Entry(janela)
campo_nome.pack()
nome = campo_nome.get()
print(nome)


def cadastrar():
    nome = campo_nome.get()
    print("Nome cadastrado:", nome)
    
botao = tk.Button(
    janela,
    text="Cadastrar",
    command=cadastrar
)


botao.pack()



# O mainloop sempre deve tá na ultima linha do código, pois ele mantém a janela aberta e em execução.
janela.mainloop()