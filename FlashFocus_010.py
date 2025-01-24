import time
from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image

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
    # velocidade = float(value) / 1000  # Converte milissegundos para segundos
    # Inverte o valor para que 100 seja lento e 1000 seja rápido
    velocidade = 1 - (float(value) - 100) / 900

def centralizar(widget):
    widget.pack(pady=10)  # Adiciona um espaçamento acima e abaixo do widget
    widget.place(relx=0.5, anchor="center") # Centraliza o widget na janela

# Cria a janela principal
janela = tk.Tk()
janela.title("Flash Focus")
janela.config(bg="#0E1724")
janela.state("zoomed")

imagem = Image.open("logo.png")  # Substitua "sua_imagem.png" pelo caminho da sua imagem
imagem_tk = ImageTk.PhotoImage(imagem)
label_imagem = tk.Label(janela, image=imagem_tk, bg="#0E1724")


# Cria um widget Text para exibir as palavras com o anchor centralizado
label_palavra = tk.Text(janela, height=2, font=("Helvetica", 24))
label_palavra.pack(pady=20)

label_imagem.place(relx=0.5, rely=0.2, anchor="center")

# Configura a tag de formatação para a letra central
label_palavra.tag_configure("central", font=("Helvetica", 24, "bold"), foreground="#FF0000")  # Vermelho puro


# Configura a tag para centralizar o texto
label_palavra.tag_configure("center", justify='center', background="#E0FFFF")


# Cria uma caixa de texto para inserir o texto
caixa_texto = tk.Text(janela, height=10, width=30)
caixa_texto.insert(tk.END, "Você pode ler mais rápido do que imagina!")
caixa_texto.pack()

# Cria o controle deslizante para ajustar a velocidade de exibição
slider_velocidade = tk.Scale(janela, from_=100, to=900, orient=HORIZONTAL, label="Velocidade", command=ajustar_velocidade)
slider_velocidade.set(700)  # Define uma velocidade média como padrão
slider_velocidade.pack(pady=10)

# Cria um frame para alinhar os botões lado a lado
frame_botoes = tk.Frame(janela)
frame_botoes.pack(pady=10)

# Cria o botão para iniciar a exibição
botao_iniciar = tk.Button(frame_botoes, text="Iniciar", command=iniciar)
botao_iniciar.grid(row=0, column=0, padx=5)

# Cria o botão para pausar a exibição
botao_pausar = tk.Button(frame_botoes, text="Pausar", command=pausar)
botao_pausar.grid(row=0, column=1, padx=5)

# Cria o botão para continuar a exibição
botao_continuar = tk.Button(frame_botoes, text="Continuar", command=continuar)
botao_continuar.grid(row=0, column=2, padx=5)

janela.mainloop()
