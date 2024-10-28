from collections import deque

def Water_Jug_problem(X, Y, target):
    # Create a queue for BFS
    queue = deque()
    visited = set()  # To keep track of visited states
    path = {}  # To reconstruct the path
    actions = {}  # To keep track of which action is applied for each state

    # Start from the initial state
    queue.append((0, 0))
    visited.add((0, 0))
    path[(0, 0)] = None
    actions[(0, 0)] = "Start with both jugs empty"

    while queue:
        current = queue.popleft()
        current_j1, current_j2 = current

        # Check if we reached the target in either jug
        if current_j1 == target or current_j2 == target:
            # Reconstruct the path
            result_path = []
            applied_rules = []
            while current:
                result_path.append(current)
                applied_rules.append(actions[current])
                current = path[current]
            return result_path[::-1], applied_rules[::-1]  # Return reversed path and applied rules

        # Generate all possible states with corresponding actions
        next_states = [
            ((X, current_j2), "Fill jug1"),  # Fill jug1
            ((current_j1, Y), "Fill jug2"),  # Fill jug2
            ((0, current_j2), "Empty jug1"),  # Empty jug1
            ((current_j1, 0), "Empty jug2"),  # Empty jug2
            ((current_j1 - min(current_j1, Y - current_j2), current_j2 + min(current_j1, Y - current_j2)), "Pour jug1 to jug2 until it fills and let the remaining to remain same"),  # Pour jug1 to jug2
            ((current_j1 + min(current_j2, X - current_j1), current_j2 - min(current_j2, X - current_j1)), "Pour jug2 to jug1 until it fills and let the remaining to remain same")   # Pour jug2 to jug1
        ]

        # Process next states
        for state, action in next_states:
            if state not in visited:
                visited.add(state)
                queue.append(state)
                path[state] = current
                actions[state] = action

    return None, None

# Remove the GCD check from this function, only check if both jugs are smaller than the target.
def check(j1, j2, target):
    if j1 < target and j2 < target:
        print("Not possible: Both jugs are smaller than the target.")
        return True
    return False

# Function to get a valid positive integer input
def get_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Invalid input. Please enter a positive integer.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a valid numeric value.")

# Main Code
J1 = get_positive_integer("Enter the volume of the first jug (positive integer): ")
J2 = get_positive_integer("Enter the volume of the second jug (positive integer): ")
L = get_positive_integer("Enter the target volume (positive integer): ")

if check(J1, J2, L):
    print("Not possible to measure the target volume.")
else:
    path, applied_rules = Water_Jug_problem(J1, J2, L)
    if path:
        print("Path is as follows:")
        for i, state in enumerate(path):
            print(f"Jug1: {state[0]}, Jug2: {state[1]} -> {applied_rules[i]}")
        print(f"Solution found: One of the jugs contains the target volume of {L}.")
    else:
        print("No solution found.")
