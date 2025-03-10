import networkx as nx

# Crear el grafo dirigido
G = nx.DiGraph()

# Añadir nodos y valores iniciales
G.add_node('t1', score_A=1.0)
G.add_node('t2', score_A=0.9, score_B=1.0)
G.add_node('t3', score_A=0.72, score_B=0.8)
G.add_node('t4', score_B=0.56)

# Añadir aristas con pesos
G.add_edge('t1', 't2', weight=0.9)
G.add_edge('t2', 't3', weight=0.8)
G.add_edge('t3', 't4', weight=0.7)

# Función para calcular la propagación de valores para un nodo
def propagate_scores(graph, start_node, score_attr, node_scores):
    for successor in graph.successors(start_node):
        edge_weight = graph[start_node][successor]['weight']
        node_scores[successor] = edge_weight * node_scores[start_node]
        propagate_scores(graph, successor, score_attr, node_scores)

# Calcular la propagación para SA y SB
scores_A = {'t1': 1.0}
propagate_scores(G, 't1', 'score_A', scores_A)
print("Puntuaciones de A (propagadas):", scores_A)

scores_B = {'t2': 1.0}
propagate_scores(G, 't2', 'score_B', scores_B)
print("Puntuaciones de B (propagadas):", scores_B)

# Función para calcular SGO(A,B) usando la fórmula dada
def SGO(graph, terms_A, terms_B, scores_A, scores_B):
    # Intersección de términos
    common_terms = set(terms_A).intersection(set(terms_B))
    print("Términos comunes:", common_terms)
    
    # Sumar las puntuaciones de los términos comunes
    numerator = sum(scores_A.get(t, 0) + scores_B.get(t, 0) for t in common_terms)
    
    # Sumar todas las puntuaciones de A y B
    total_score_A = sum(graph.nodes[t]['score_A'] for t in terms_A)
    total_score_B = sum(graph.nodes[t].get('score_B', 0) for t in terms_B)
    denominator = total_score_A + total_score_B
    
    return numerator / denominator

# Calcular SGO(A,B)
terms_A = ['t1', 't2', 't3']
terms_B = ['t2', 't3', 't4']
sgo_value = SGO(G, terms_A, terms_B, scores_A, scores_B)
print("SGO(A,B):", sgo_value)
