import heapq

def is_valid_input(matrix):
    """Check if the matrix contains 9 characters and no duplicates."""
    flat_matrix = [char for row in matrix for char in row]

    
    if len(flat_matrix) != 9:
        return False, "The matrix must contain exactly 9 characters."
    
    
    blanks = {' '}
    non_blanks = [char for char in flat_matrix if char not in blanks]
    
    if len(set(non_blanks)) != len(non_blanks):
        return False, "Invalid input. Please ensure no duplicates, except for the blank space."
    
    return True, ""
def get_matrix_input(prompt):
    """Function to get a valid 3x3 matrix input from the user."""
    while True:
        print(prompt)
        input_str = input().strip()
        flat_input = [char.strip() if char.strip() else ' ' for char in input_str.split(",")]
        if len(flat_input) != 9:
            print("Invalid input. Please enter exactly 9 valid characters (use 1-8 numbers and symbols and ' ' for blank space).")
            continue
        matrix = [flat_input[i:i + 3] for i in range(0, 9, 3)]
        valid, message = is_valid_input(matrix)
        if not valid:
            print(message)
            continue
        return matrix
def misplaced_tiles(state, goal):
    return sum(1 for i in range(9) if state[i] != goal[i] and state[i] not in {' ', '0', '_'})

def print_chessboard(matrix):
    """Print the 3x3 matrix in a chessboard-like format."""
    for j in range(3):
        print(" | ".join(f"{matrix[k + j * 3]:2s}" for k in range(3)))
        if j < 2:  
            print("-----------")

# Input for Source Matrix
s = get_matrix_input("Enter Source States (9 characters separated by commas, use ' ' for blank space):")

# Input for Destination Matrix
des = get_matrix_input("Enter Destination States (9 characters separated by commas, use ' ' for blank space):")

# Convert to tuple and normalize blank space representation to ' '
s = tuple(' ' if char in {' ', '0', '_'} else char for row in s for char in row)
des = tuple(' ' if char in {' ', '0', '_'} else char for row in des for char in row)

# Directions for movement
directions = {0: "up", 1: "down", 2: "left", 3: "right"}

# Print the initial state before processing
print("Initial State:")
print_chessboard(s)

# Priority queue for A* search
pq = []
# Dictionary to store states
d = {}
g = {}  # Dictionary to store g(x) cost
d[s] = (s, -1, None)  # (state, move_number, direction)
g[s] = 0
heapq.heappush(pq, (misplaced_tiles(s, des), s, 0))

f = 0

# A* search
while pq:
    _, cur, move_num = heapq.heappop(pq)
    
    if cur == des:
        f = 1
        break

    # Find the position of the blank (' ')
    for i in range(9):
        if cur[i] in {' ', '0', '_'}:
            idx = i
            break

    temp = list(cur)

    # Check the possible moves and directions
    if idx >= 3:  # Can move up
        a = temp[:]
        a[idx], a[idx - 3] = a[idx - 3], a[idx]
        a = tuple(a)
        if a not in g or g[a] > g[cur] + 1:
            g[a] = g[cur] + 1
            f_cost = g[a] + misplaced_tiles(a, des)
            heapq.heappush(pq, (f_cost, a, move_num + 1))
            d[a] = (cur, move_num + 1, 0)  # 0 is "up"

    if idx <= 5:  # Can move down
        a = temp[:]
        a[idx], a[idx + 3] = a[idx + 3], a[idx]
        a = tuple(a)
        if a not in g or g[a] > g[cur] + 1:
            g[a] = g[cur] + 1
            f_cost = g[a] + misplaced_tiles(a, des)
            heapq.heappush(pq, (f_cost, a, move_num + 1))
            d[a] = (cur, move_num + 1, 1)  # 1 is "down"

    if idx % 3 != 2:  # Can move right
        a = temp[:]
        a[idx], a[idx + 1] = a[idx + 1], a[idx]
        a = tuple(a)
        if a not in g or g[a] > g[cur] + 1:
            g[a] = g[cur] + 1
            f_cost = g[a] + misplaced_tiles(a, des)
            heapq.heappush(pq, (f_cost, a, move_num + 1))
            d[a] = (cur, move_num + 1, 3)  # 3 is "right"

    if idx % 3 != 0:  # Can move left
        a = temp[:]
        a[idx], a[idx - 1] = a[idx - 1], a[idx]
        a = tuple(a)
        if a not in g or g[a] > g[cur] + 1:
            g[a] = g[cur] + 1
            f_cost = g[a] + misplaced_tiles(a, des)
            heapq.heappush(pq, (f_cost, a, move_num + 1))
            d[a] = (cur, move_num + 1, 2)  # 2 is "left"
if f == 0:
    print("No solution found")
else:
    ans = []
    while d[cur][1] != -1:
        ans.append((cur, d[cur][1], d[cur][2]))  # (state, move_number, direction)
        cur = d[cur][0]
    
    print("Solution found!")
    print(f"Total moves to reach the goal: {len(ans)}\n")
    ans.reverse()
    for step, move_number, move_direction in ans:
        print(f"Move number: {move_number}")
        print(f"Move direction: {directions[move_direction]}")
        print("States after the move:")
        print_chessboard(step)
        g_x = g[step]  
        h_x = misplaced_tiles(step, des)  
        f_x = g_x + h_x  # f(x) = g(x) + h(x)
        print(f"f(x) = g(x) + h(x) = {g_x} + {h_x}")
        
        print("-" * 10)  

    # Final state
    print(f"Final state after {len(ans)} moves:")
    print_chessboard(des)
