import heapq
import time

# Simulasi peta kota (2D grid)
grid = [
    ['S', '.', '.', 'T', '.'],
    ['.', 'T', '.', 'T', '.'],
    ['.', '.', '.', '.', '.'],
    ['T', 'T', 'T', '.', 'H']
]

# Ukuran grid
rows = len(grid)
cols = len(grid[0])

# Arah gerakan: atas, bawah, kiri, kanan
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def find_position(symbol):
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == symbol:
                return (i, j)
    return None

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])  # Manhattan distance

def gbfs(start, goal):
    frontier = [(heuristic(start, goal), start)]
    came_from = {start: None}
    explored_nodes = 0
    visited = set()

    while frontier:
        _, current = heapq.heappop(frontier)
        explored_nodes += 1

        if current == goal:
            break

        for d in directions:
            ni, nj = current[0] + d[0], current[1] + d[1]
            neighbor = (ni, nj)

            if 0 <= ni < rows and 0 <= nj < cols:
                if grid[ni][nj] != 'T' and neighbor not in visited:
                    visited.add(neighbor)
                    heapq.heappush(frontier, (heuristic(neighbor, goal), neighbor))
                    came_from[neighbor] = current

    # Rekonstruksi path
    path = []
    node = goal
    while node:
        path.append(node)
        node = came_from.get(node)
    path.reverse()

    return path, explored_nodes

# Cari posisi start dan goal
start = find_position('S')
goal = find_position('H')

# Eksekusi GBFS
start_time = time.time()
path, nodes = gbfs(start, goal)
end_time = time.time()

# Tampilkan hasil
print("Path:", path)
print("Path (visual):")
for i in range(rows):
    row = ""
    for j in range(cols):
        if (i, j) in path and grid[i][j] == '.':
            row += 'o '
        else:
            row += grid[i][j] + ' '
    print(row)

print("Nodes explored:", nodes)
print("Time taken (ms):", (end_time - start_time) * 1000)
