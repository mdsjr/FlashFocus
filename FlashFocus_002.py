import time
from tkinter import *
import tkinter as tk

def exibir_palavras():
  """
  Exibe as palavras do texto na caixa de texto, uma de cada vez.
  """
  texto = caixa_texto.get("1.0", tk.END).strip()  # Obtém o texto da caixa de texto
  palavras = texto.split()

  for palavra in palavras:
    label_palavra.config(text=palavra)  # Atualiza o texto do label
    janela.update()  # Atualiza a janela para exibir a mudança
    time.sleep(0.3)

# Cria a janela principal
janela = tk.Tk()
janela.title("Exibidor de Palavras")

# Cria um label para exibir as palavras
label_palavra = tk.Label(janela, text="", font=("Helvetica", 24))
label_palavra.pack(pady=20)

# Cria uma caixa de texto para inserir o texto
caixa_texto = tk.Text(janela, height=5, width=30)
caixa_texto.pack()

# Cria um botão para iniciar a exibição
botao_exibir = tk.Button(janela, text="Exibir Palavras", command=exibir_palavras)
botao_exibir.pack(pady=10)

janela.mainloop()