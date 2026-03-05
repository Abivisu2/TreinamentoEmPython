pilha = []

pilha.append("mariana");
pilha.append("banana");
pilha.append("abílio");

print(pilha)

item_desempilhado = pilha.pop();
print("item desimpilhado:", item_desempilhado)

item_desempilhado = pilha.pop();
print("item desimpilhado:", item_desempilhado)

if len(pilha) > 0:
    topo_da_pilha = pilha[-1]
    print("topo da pilha:", topo_da_pilha)
else:
    print("A pilha está vazia")