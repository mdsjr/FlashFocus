import time
from tkinter import *
import tkinter as tk

# Variável global para controlar o estado da exibição
executando = False
indice_atual = 0

def encontrar_letra_central(palavra):
    """Encontra e retorna a letra central de uma palavra."""
    tamanho = len(palavra)
    if tamanho == 0:
        return "" 
    indice_meio = tamanho // 2 
    return palavra[indice_meio]

def exibir_palavras():
    global executando, indice_atual
    texto = caixa_texto.get("1.0", tk.END).strip()
    palavras = texto.split()

    while executando and indice_atual < len(palavras):
        palavra = palavras[indice_atual]
        letra_central = encontrar_letra_central(palavra)
        indice_meio = len(palavra) // 2

        parte1 = palavra[:indice_meio]
        parte2 = palavra[indice_meio + 1:]

        # Limpa o conteúdo anterior do Text widget
        label_palavra.delete("1.0", tk.END)

        # Adiciona parte1
        label_palavra.insert(tk.END, parte1, "center")

        # Adiciona a letra central com a tag de formatação e centralização
        label_palavra.insert(tk.END, letra_central, "central center")

        # Adiciona parte2
        label_palavra.insert(tk.END, parte2, "center")

        # Atualiza a exibição
        janela.update()
        time.sleep(0.3)

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

# Cria a janela principal
janela = tk.Tk()
janela.title("Flash Focus")

# Cria um widget Text para exibir as palavras com o anchor centralizado
label_palavra = tk.Text(janela, height=2, font=("Helvetica", 24))
label_palavra.pack(pady=20)

# Configura a tag de formatação para a letra central
label_palavra.tag_configure("central", font=("Helvetica", 24, "bold"), foreground="red")

# Configura a tag para centralizar o texto
label_palavra.tag_configure("center", justify='center')

# Cria uma caixa de texto para inserir o texto
caixa_texto = tk.Text(janela, height=5, width=30)
caixa_texto.insert(tk.END, "Você pode ler mais rápido do que imagina!")
caixa_texto.pack()

# Cria um frame para alinhar os botões na horizontal
frame_botoes = tk.Frame(janela)
frame_botoes.pack(pady=10)

# Cria os botões dentro do frame
botao_iniciar = tk.Button(frame_botoes, text="Iniciar", command=iniciar)
botao_iniciar.pack(side=tk.LEFT, padx=5)

botao_pausar = tk.Button(frame_botoes, text="Pausar", command=pausar)
botao_pausar.pack(side=tk.LEFT, padx=5)

botao_continuar = tk.Button(frame_botoes, text="Continuar", command=continuar)
botao_continuar.pack(side=tk.LEFT, padx=5)

janela.mainloop()
