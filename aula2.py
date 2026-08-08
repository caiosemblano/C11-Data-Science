x = True
print(type(x))




# --- LIST ---
# Ordenada, mutável, aceita duplicados
frutas = ["maçã", "banana", "laranja", "banana"]
frutas.append("uva")
print("List:", frutas)

# --- TUPLE ---
# Ordenada, imutável
coordenadas = (10.5, -23.1)
print("Tuple:", coordenadas)

# --- SET ---
# Não ordenado, mutável, apenas itens únicos
tags = {"python", "código", "python", "dev"}
tags.add("backend")
print("Set:", tags)  # "python" aparece apenas uma vez

# --- FROZENSET ---
# Versão imutável do set
categorias_fixas = frozenset(["admin", "user", "guest"])
print("Frozenset:", categorias_fixas)

# --- DICT ---
# Chave-valor, mutável
usuario = {"nome": "Caio", "idade": 22}
usuario["cargo"] = "Desenvolvedor"
print("Dict:", usuario)