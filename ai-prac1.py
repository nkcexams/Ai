import heapq
import collections

# Define a simple tree structure.
# Here, each node maps to its children with an associated cost (all set to 1).
tree = {
    'A': {'B': 1, 'C': 1},
    'B': {'D': 1, 'E': 1},
    'C': {'F': 1, 'G': 1},
    'D': {},
    'E': {},
    'F': {},
    'G': {}
}

def bfs(graph, start, goal):
    queue = collections.deque([(start, [start])])
    
    visited = set()
    while queue:
        node, path = queue.popleft()
        if node == goal:
            return path
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))
    return None

def dfs(graph, start, goal):
    stack = [(start, [start])]
    visited = set()
    while stack:
        print(stack)
        node, path = stack.pop()
        if node == goal:
            return path
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    stack.append((neighbor, path + [neighbor]))
    return None

def dls(graph, start, goal, limit):
    stack = [(start, [start], 0)]
    visited = set()
    while stack:
        node, path, depth = stack.pop()
        if node == goal:
            return path
        if depth < limit:
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    stack.append((neighbor, path + [neighbor], depth + 1))
    return None

def ids(graph, start, goal, max_depth):
    for depth in range(max_depth):
        result = dls(graph, start, goal, depth)
        if result:
            return result
    return None

def ucs(graph, start, goal):
    queue = [(0, start, [start])]
    visited = set()
    while queue:
        cost, node, path = heapq.heappop(queue)
        if node == goal:
            return path
        if node not in visited:
            visited.add(node)
            for neighbor, weight in graph[node].items():
                if neighbor not in visited:
                    heapq.heappush(queue, (cost + weight, neighbor, path + [neighbor]))
    return None

start_node = 'A'
goal_node = 'G'
print("Breadth-First Search (BFS):", bfs(tree, start_node, goal_node))
print("Depth-First Search (DFS):", dfs(tree, start_node, goal_node))
print("Depth-Limited Search (DLS):", dls(tree, start_node, goal_node, limit=3))
print("Iterative Deepening Search (IDS):", ids(tree, start_node, goal_node, max_depth=5))
print("Uniform Cost Search (UCS):", ucs(tree, start_node, goal_node))
