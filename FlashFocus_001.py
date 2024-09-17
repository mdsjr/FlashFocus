import time

def exibir_palavras(texto):
  """
  Exibe as palavras de um texto uma de cada vez com um pequeno intervalo entre elas.

  Args:
  
      texto: O texto a ser exibido.
  """
  palavras = texto.split()  # Divide o texto em uma lista de palavras

  for palavra in palavras:
    print(palavra)
    time.sleep(0.3)  # Aguarda 0.3 segundos antes de exibir a próxima palavra

# Exemplo de uso
texto = "Este é um exemplo de texto para ser exibido palavra por palavra."
exibir_palavras(texto)