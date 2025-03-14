# Criação de um dicionario

dicionario = {
    "chave1": "valor1",
    "chave2": "valor2",
    "chave3": "valor3"
}

print(dicionario["chave1"])

# Acesso a um valor

print(dicionario.get("chave1"))

# Adicionar um novo par chave-valor

dicionario["chave4"] = "valor4"

print(dicionario)

# Atualizar um valor

dicionario["chave1"] = "novo valor"

print(dicionario)

# Remover um item

del dicionario["chave1"]

print(dicionario)

# Iterar sobre as chaves

for chave in dicionario:
    print(chave)
    
# Iterar sobre os valores

for valor in dicionario.values():
    print(valor)
    
# Verificar a existencia de uma chave

if "chave1" in dicionario:
    print("A chave 'chave1' existe no dicionario.")
else:
    print("A chave 'chave1' nao existe no dicionario.")
    
# Combinar dois dicionarios 

dicionario1 = {"chave1": "valor1", "chave2": "valor2"}
dicionario2 = {"chave3": "valor3", "chave4": "valor4"}

dicionario3 = {**dicionario1, **dicionario2}

print(dicionario3)

# Contar quantidade de items 

print(len(dicionario))
