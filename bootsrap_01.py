import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.style import Style
import time
from tkinter import *

# Variável global para controlar o estado da exibição
executando = False
indice_atual = 0
velocidade = 0.3  # Velocidade padrão de exibição

def encontrar_letra_central(palavra):
    """Encontra e retorna a letra central de uma palavra."""
    tamanho = len(palavra)
    if tamanho == 0:
        return "" 
    indice_meio = tamanho // 2 
    return palavra[indice_meio]

def exibir_palavras():
    global executando, indice_atual
    texto = caixa_texto.get("1.0", END).strip()
    palavras = texto.split()

    while executando and indice_atual < len(palavras):
        palavra = palavras[indice_atual]
        letra_central = encontrar_letra_central(palavra)
        indice_meio = len(palavra) // 2

        parte1 = palavra[:indice_meio]
        parte2 = palavra[indice_meio + 1:]

        # Limpa o conteúdo anterior do Text widget
        label_palavra.delete("1.0", END)

        # Adiciona parte1
        label_palavra.insert(END, parte1, "center")

        # Adiciona a letra central com a tag de formatação e centralização
        label_palavra.insert(END, letra_central, "central center")

        # Adiciona parte2
        label_palavra.insert(END, parte2, "center")

        # Atualiza a exibição
        janela.update()
        time.sleep(velocidade)  # Utiliza a velocidade selecionada pelo usuário

        # Próxima palavra
        indice_atual += 1

def iniciar():
    global executando, indice_atual
    executando = True
    indice_atual = 0  # Reinicia o índice ao começar novamente
    exibir_palavras()

def pausar():
    global executando
    executando = False

def continuar():
    global executando
    executando = True
    exibir_palavras()

def ajustar_velocidade(value):
    global velocidade
    velocidade = 1 - (float(value) - 100) / 900

# Cria a janela principal
app = ttk.Window("FlashFocus")
style = Style(theme="superhero")
app.state("zoomed")  # Inicia a janela em tela cheia

# Exemplo de LabelFrame corrigido
label_palavra = ttk.LabelFrame(app, text="Exemplo de LabelFrame")
label_palavra.pack(pady=10, padx=10, fill="x")
ttk.Label(label_palavra,).pack(pady=20)

nome = ttk.Frame(app)
nome.pack(pady=18, padx=10, fill="x")
ttk.Label(nome, text="Nome:").pack(side=LEFT, padx=5)
ttk.Entry(nome).pack(side=LEFT, fill="x", expand=True, padx=5)

email = ttk.Frame(app)
email.pack(pady=18, padx=10, fill="x")
ttk.Label(email, text="Email:").pack(side=LEFT, padx=5)
ttk.Entry(email).pack(side=LEFT, fill="x", expand=True, padx=5)

idade = ttk.Frame(app)
idade.pack(pady=18, padx=10, fill="x")
ttk.Label(idade, text="Idade:").pack(side=LEFT, padx=5)
ttk.Entry(idade).pack(side=LEFT, fill="x", expand=True, padx=5)

checkbox = ttk.Frame(app)
checkbox.pack(pady=15, padx=10, fill="x")
ttk.Checkbutton(checkbox, bootstyle="round-toggle", text="Lembrar dados?").pack(side=LEFT, padx=5)

botao = ttk.Frame(app)
botao.pack(pady=30, padx=10, fill="x")
ttk.Button(botao, text="Enviar", bootstyle=SUCCESS).pack(side=LEFT, padx=15)
ttk.Button(botao, text="Cancelar", bootstyle=DANGER).pack(side=LEFT, padx=15)

app.mainloop()
