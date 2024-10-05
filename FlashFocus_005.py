import time
from tkinter import *
import tkinter as tk

def encontrar_letra_central(palavra):
    """Encontra e retorna a letra central de uma palavra."""
    tamanho = len(palavra)
    if tamanho == 0:
        return "" 
    indice_meio = tamanho // 2 
    return palavra[indice_meio]

def exibir_palavras():
    texto = caixa_texto.get("1.0", tk.END).strip()
    palavras = texto.split()

    for palavra in palavras:
        letra_central = encontrar_letra_central(palavra)
        indice_meio = len(palavra) // 2

        parte1 = palavra[:indice_meio]
        parte2 = palavra[indice_meio + 1:]

        # Limpa o conteúdo anterior do Text widget
        label_palavra.delete("1.0", tk.END)

        # Adiciona parte1
        label_palavra.insert(tk.END, parte1)

        # Adiciona a letra central com uma tag de formatação
        label_palavra.insert(tk.END, letra_central, "central")

        # Adiciona parte2
        label_palavra.insert(tk.END, parte2)

        # Atualiza a exibição
        janela.update()
        time.sleep(0.3)

# Cria a janela principal
janela = tk.Tk()
janela.title("Exibidor de Palavras")

# Cria um widget Text para exibir as palavras
label_palavra = tk.Text(janela, height=2, font=("Helvetica", 24))
label_palavra.pack(pady=20)

# Configura a tag de formatação para a letra central
label_palavra.tag_configure("central", font=("Helvetica", 24, "bold"), foreground="red")

# Cria uma caixa de texto para inserir o texto
caixa_texto = tk.Text(janela, height=5, width=30)
caixa_texto.pack()

# Cria um botão para iniciar a exibição
botao_exibir = tk.Button(janela, text="Exibir Palavras", command=exibir_palavras)
botao_exibir.pack(pady=10)

janela.mainloop()