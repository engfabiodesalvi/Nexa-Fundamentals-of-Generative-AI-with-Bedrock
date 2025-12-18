entrada = input()

def descrever_ferramenta(nome):
  if nome == "Token":
    return "Unidade de texto que modelos de linguagem processam."

  elif nome == "Fine-tuning":
    return "Adapta um modelo treinado com dados novos e específicos."

  elif nome == "Inference":
    return "Uso do modelo treinado para gerar saída da entrada."

  elif nome == "Dataset":
    return "Conjunto de dados para treinar ou ajustar um modelo de IA."

print(descrever_ferramenta(entrada))
