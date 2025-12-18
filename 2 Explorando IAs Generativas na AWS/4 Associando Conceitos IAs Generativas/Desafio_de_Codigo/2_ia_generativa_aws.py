entrada = input()

def descrever_ferramenta(nome):
  if nome == "Amazon Bedrock":
    return "Serviço de acesso via API a múltiplos modelos fundacionais."

  elif nome == "Amazon Titan":
    return "Modelos base da AWS para gerar e resumir texto."

  elif nome == "Amazon Q":
    return "ssistente de IA para devs e TI integrado aos serviços AWS."

  elif nome == "AWS Trainium":
    return "Chip da AWS para treinar modelos de ML em larga escala."

print(descrever_ferramenta(entrada))
