import networkx as nx
import heapq

# ======================================================================
# 1. ПРЕДСТАВЛЕННЯ ГРАФА (Варіант №13)
# ======================================================================

# Створення неорієнтованого зваженого графа
G = nx.Graph()

# Додавання ребер та їх ваг відповідно до Варіанту 13:
# (1,2)w=2, (1,4)w=7, (1,7)w=5, (2,5)w=9, (3,4)w=5, (3,6)w=4, 
# (3,7)w=9, (4,5)w=2, (4,6)w=5, (5,6)w=3, (6,8)w=1, (7,8)w=6.
edges_13 = [
    (1, 2, 2), (1, 4, 7), (1, 7, 5), 
    (2, 5, 9), (3, 4, 5), (3, 6, 4), 
    (3, 7, 9), (4, 5, 2), (4, 6, 5), 
    (5, 6, 3), (6, 8, 1), (7, 8, 6)
]

G.add_weighted_edges_from(edges_13)

# ======================================================================
# 2. АЛГОРИТМ ПРІМА (З покроковим виводом)
# ======================================================================

def prim_steps_print(graph, start_node=1):
    """
    Алгоритм Прима для пошуку МКД з покроковим виводом.
    Використовує чергу з пріоритетом (heapq).
    """
    print("\n--- Запуск Алгоритму Пріма ---")
    
    # Ініціалізація
    visited = {v: False for v in graph.nodes()}
    dist = {v: float('inf') for v in graph.nodes()} # Мінімальна вага ребра до вершини
    parent = {v: None for v in graph.nodes()}       # Батьківська вершина в МКД
    
    dist[start_node] = 0
    pq = [(0, start_node)]  # (Вага, Вершина)
    
    steps = []
    
    while pq:
        d, u = heapq.heappop(pq)
        
        if visited[u]: 
            continue
        
        # Додаємо вершину до МКД
        visited[u] = True
        
        # Додаємо ребро до списку кроків (якщо це не стартова вершина)
        if parent[u] is not None:
            print(f"{len(steps) + 1}. Add edge ({parent[u]} - {u}) weight = {d}")
            steps.append((parent[u], u, d))
        
        # Перевіряємо сусідів
        for v in graph.neighbors(u):
            w = graph[u][v]['weight']
            
            # Якщо сусід не відвіданий і вага менша за поточний dist[v]
            if not visited[v] and w < dist[v]:
                dist[v] = w
                parent[v] = u
                heapq.heappush(pq, (w, v))
                
    total = sum(w for (_, _, w) in steps)
    print("\nTotal Prim MST weight:", total)
    
    return steps, total

# ======================================================================
# 3. АЛГОРИТМ КРУСКАЛА (З DSU та покроковим виводом)
# ======================================================================

class DSU:
    """Структура даних 'Роз'єднані Множини' (Disjoint Set Union)"""
    def __init__(self, n):
        # Ініціалізуємо кожну вершину як корінь власної множини
        self.parent = {i: i for i in range(1, n + 1)}
        self.rank = {i: 0 for i in range(1, n + 1)}

    def find(self, x):
        # Пошук кореня з Path Compression
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        # Об'єднання двох множин з Union by Rank
        ra, rb = self.find(a), self.find(b)
        
        if ra == rb: 
            return False # Ребра утворює цикл
        
        if self.rank[ra] < self.rank[rb]:
            self.parent[ra] = rb
        else:
            self.parent[rb] = ra
            if self.rank[ra] == self.rank[rb]:
                self.rank[ra] += 1
        
        return True # Ребро додане успішно

def kruskal_print(graph):
    """
    Алгоритм Крускала для пошуку МКД з покроковим виводом.
    Використовує DSU.
    """
    print("\n--- Запуск Алгоритму Крускала ---")
    
    # 1. Складаємо список усіх ребер з їх вагами
    edges = []
    for u, v, data in graph.edges(data=True):
        edges.append((data['weight'], u, v)) # (вага, u, v)

    # 2. Сортуємо ребра за зростанням ваги
    edges_sorted = sorted(edges) 
    
    dsu = DSU(graph.number_of_nodes())
    steps = []
    total = 0
    
    # 3. Ітерація по відсортованих ребрах
    for w, u, v in edges_sorted:
        # Перевіряємо, чи не утворює ребро цикл
        if dsu.union(u, v):
            # Якщо не утворює цикл - додаємо до МКД
            print(f"{len(steps) + 1}. Add edge ({u} - {v}) weight = {w}")
            steps.append((u, v, w))
            total += w
        
        # Зупиняємося, коли маємо N-1 ребро
        if len(steps) == graph.number_of_nodes() - 1:
            break
            
    print("\nTotal Kruskal MST weight:", total)
    
    return steps, total

# ======================================================================
# 4. ЗАПУСК ТА ВІДОБРАЖЕННЯ РЕЗУЛЬТАТІВ
# ======================================================================

if __name__ == "__main__":
    
    # Запуск Прима
    prim_steps, prim_total = prim_steps_print(G, start_node=1)
    
    # Запуск Крускала
    kruskal_steps, kruskal_total = kruskal_print(G)
    
    print("\n========================================================")
    print("ФІНАЛЬНИЙ РЕЗУЛЬТАТ (Варіант 13):")
    print(f"Вага МКД (Прім) = {prim_total}")
    print(f"Вага МКД (Крускал) = {kruskal_total}")
    print("========================================================")
