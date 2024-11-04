# Programa de resposta simples

# Solicita uma entrada do usuário
mensagem = input("Digite algo: ")

# Verifica se a entrada é "olá" (ignora maiúsculas e minúsculas)
if mensagem.lower() == "ola":
    print("Olá, tudo bem?")
else:
    print("Não entendi o que você disse.")
