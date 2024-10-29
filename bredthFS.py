from collections import defaultdict, deque

def bfs(tree, start, search):
    visited, queue, path = set(), deque([start]), []
    while queue:
        node = queue.popleft()
        if node in visited:
            continue
        visited.add(node)
        path.append(node)
        if node == search:
            return path
        queue.extend(n for n in tree[node] if n not in visited)
    return path

def print_tree(tree, start):
    def get_level(node, level=0, levels=defaultdict(list)):
        levels[level].append(node)
        for child in sorted(tree[node]):
            get_level(child, level + 1, levels)
        return levels
    levels, max_width = get_level(start), max(map(len, get_level(start).values())) * 4
    for level in sorted(levels):
        spacing = max_width // (2 ** (level + 1))
        print(" " * (max_width // 2 - len(levels[level]) * 2) + (" " * spacing).join(f"{node:4}" for node in levels[level]))

def main():
    while True:
        try:
            n = int(input("Enter the number of nodes: "))
            if n > 0:
                break
            print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a valid positive integer.")

    tree = defaultdict(list)
    print("Enter each node and its adjacent nodes (space-separated):")
    for _ in range(n):
        node, *children = input().strip().split()
        tree[node].extend(children)

    start_node = list(tree.keys())[0]
    print("\nAvailable nodes:", list(tree.keys()))
    
    search_node = input("\nEnter the search node: ")
    if search_node in tree:
        path = bfs(tree, start_node, search_node)
        print("Path:", ' -> '.join(path))
    else:
        print(f"Node {search_node} not found in the tree.")
    
    print("\nTree Structure:")
    print_tree(tree, start_node)

if __name__ == "__main__":
    main()
