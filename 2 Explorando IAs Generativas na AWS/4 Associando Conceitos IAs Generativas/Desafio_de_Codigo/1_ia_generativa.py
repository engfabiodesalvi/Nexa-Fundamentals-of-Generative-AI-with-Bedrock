entrada = input()

def descrever_conceito(conceito):
  if conceito == "Modelos de Linguagem":
    return "IA treinada em textos para prever e gerar linguagem natural."

  elif conceito == "Treinamento Supervisionado":
    return "Aprendizado com dados rotulados para ensinar a IA a prever."

  elif conceito == "Prompt Engineering":
    return "Técnica para guiar modelos via comandos (prompts) escritos."

  elif conceito == "Modelos Diffusion":
    return "Modelo que gera imagens por refinamentos iterativos do ruído."

print(descrever_conceito(entrada))
