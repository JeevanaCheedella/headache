from collections import defaultdict

def dfs_traversal(tree, start, search):
    visited = set()
    stack = [start]
    traversal = []

    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        traversal.append(node)
        if node == search:
            return traversal
        # Add neighbors to stack in reverse order to maintain correct order in traversal
        stack.extend(reversed(tree[node]))
    
    return traversal

def print_tree(tree, start):
    def get_level(node, level=0, levels=None):
        if levels is None:
            levels = defaultdict(list)
        levels[level].append(node)
        for child in sorted(tree[node]):
            get_level(child, level + 1, levels)
        return levels
    
    levels = get_level(start)
    max_width = len(levels[max(levels)]) * 4
    
    for level in sorted(levels):
        level_nodes = levels[level]
        spacing = max_width // (2 ** (level + 1))
        line = (" " * spacing).join(f"{node:4}" for node in level_nodes)
        print(" " * (max_width // 2 - len(line) // 2) + line)

def main():
    while True:
        try:
            n = int(input("Enter the number of nodes: "))
            if n <= 0:
                raise ValueError("Enter positive integers only!")
            tree = defaultdict(list)
            nodes = set()
            break
        except ValueError:
            print("Please enter a valid positive integer.")
    
    print("Enter each node and its adjacent nodes (space-separated) in each line:")
    
    for _ in range(n):
        while True:
            line = input().strip()
            if not line:
                print("Please enter the node and its adjacent nodes.")
                continue
            
            parts = line.split()
            if len(parts) < 1:
                print("Invalid input. A node must be specified.")
                continue

            node = parts[0]
            children = parts[1:]
            tree[node].extend(children)
            nodes.add(node)
            nodes.update(children)
            break

    if not nodes:
        print("No nodes were entered.")
        return
    
    l = list(tree.keys())
    start_node = l[0]
    print("\nAvailable nodes:")
    print(l)
    
    while True:
        search_node = input("\nEnter the search node: ")
        if search_node in l:
            # Perform DFS traversal and path finding
            dfs_traversal_result = dfs_traversal(tree, start_node, search_node)
            
            if dfs_traversal_result:
                print("Path: ",' -> '.join(dfs_traversal_result))
            else:
                print("Node not found in traversal.")
            break
        else:
            print(f"Node {search_node} not found in the tree. Please try again.")
    
    print("\nTree Structure:")
    print_tree(tree, start_node)

if _name_ == "_main_":
    main()
