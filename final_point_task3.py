import heapq


def dijkstra(graph, start):
    # Нехай відстані для всіх вершин як нескінченність
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0  # Відстань від початкової вершини до себе - 0
    # Бінарна купа для зберігання вершин з їхніми відстанями
    priority_queue = [(0, start)]

    while priority_queue:
        # Вибір вершини за найменшою відстанню
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Якщо поточна відстань до поточної вершини більша, ніж збережена відстань
        # пропускаємо поточну вершину
        if current_distance > distances[current_vertex]:
            continue

        # Прохід до всіх сусідних вершин
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            # Якщо відстань до сусідньої вершини коротша через поточну вершину
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

start_vertex = 'A'
print("Найкоротші відстані від вершини", start_vertex)
print(dijkstra(graph, start_vertex))
