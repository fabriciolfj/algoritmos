import math

# GRAFO - Estrutura de adjacência com pesos
graph = {}
graph["start"] = {}
graph["start"]["a"] = 5
graph["start"]["b"] = 2

graph["a"] = {}
graph["a"]["c"] = 4
graph["a"]["d"] = 2

graph["b"] = {}
graph["b"]["a"] = 8
graph["b"]["d"] = 7

graph["c"] = {}
graph["c"]["d"] = 6
graph["c"]["fin"] = 3

graph["d"] = {}
graph["d"]["fin"] = 1

graph["fin"] = {}

# CUSTOS - Distâncias do nó inicial
infinity = math.inf
costs = {}
costs["a"] = 5      # ✅ Custo direto de start -> a
costs["b"] = 2      # ✅ Custo direto de start -> b
costs["c"] = infinity  # ✅ Ainda não conhecemos o caminho
costs["d"] = infinity  # ✅ Ainda não conhecemos o caminho
costs["fin"] = infinity

# PARENTS - Para reconstruir o caminho
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["c"] = None    # ✅ Adicionado
parents["d"] = None    # ✅ Adicionado
parents["fin"] = None

processed = set()


processed = set()

def find_lowest_cost_node(costs):
    lowest_cost = math.inf
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.add(node)
    node = find_lowest_cost_node(costs)

print("Custos finais:", costs)
print("Pais:", parents)
print(f"\nMenor caminho até 'fin': {costs['fin']}")

# RECONSTRUIR O CAMINHO
def reconstruct_path(parents, start, end):
    path = [end]
    while path[-1] != start:
        path.append(parents[path[-1]])
    path.reverse()
    return path

caminho = reconstruct_path(parents, "start", "fin")
print(f"Caminho: {' -> '.join(caminho)}")