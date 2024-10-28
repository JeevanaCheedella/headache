from collections import deque
def is_valid(state, total_missionaries, total_cannibals):
    lM, lC, rM, rC = state
    if lM < 0 or lC < 0 or rM < 0 or rC < 0:  
        return False
    if lM > total_missionaries or lC > total_cannibals or rM > total_missionaries or rC > total_cannibals:  
        return False
    if (lM > 0 and lC > lM) or (rM > 0 and rC > rM):  
        return False
    return True
def is_goal(state, total_missionaries, total_cannibals):
    _, _, rM, rC = state
    return rM == total_missionaries and rC == total_cannibals
def get_next_states(state, boat_on_left, total_missionaries, total_cannibals, boat_capacity):
    lM, lC, rM, rC = state
    next_states = []
    
    for m in range(0, boat_capacity + 1):
        for c in range(0, boat_capacity + 1):
            if m + c > 0 and m + c <= boat_capacity:  
                if boat_on_left:
                    if lM >= m and lC >= c:  
                        next_states.append((lM - m, lC - c, rM + m, rC + c))
                else:
                    if rM >= m and rC >= c:  
                        next_states.append((lM + m, lC + c, rM - m, rC - c))
    return [state for state in next_states if is_valid(state, total_missionaries, total_cannibals)]
def solve_missionaries_and_cannibals(total_missionaries, total_cannibals, boat_capacity):
    initial_state = (total_missionaries, total_cannibals, 0, 0)  
    boat_on_left = True  
    queue = deque([(initial_state, boat_on_left, [])])  
    visited = set()  
    while queue:
        current_state, boat_on_left, path = queue.popleft()
        if is_goal(current_state, total_missionaries, total_cannibals):
            return path + [(current_state, boat_on_left)]
        if (current_state, boat_on_left) in visited:
            continue
        visited.add((current_state, boat_on_left))
        next_states = get_next_states(current_state, boat_on_left, total_missionaries, total_cannibals, boat_capacity)
        for next_state in next_states:
            queue.append((next_state, not boat_on_left, path + [(current_state, boat_on_left)]))
    return None  
def describe_step(current_state, next_state, boat_on_left):
    cM, cC, _, _ = current_state
    nM, nC, _, _ = next_state
    missionaries_moved = abs(cM - nM)
    cannibals_moved = abs(cC - nC)
    if boat_on_left:
        direction = "from left to right"
    else:
        direction = "from right to left"
    description = f"Moved {missionaries_moved} missionary(ies) and {cannibals_moved} cannibal(s) {direction}."
    return description
def print_solution(total_missionaries, total_cannibals, boat_capacity):
    solution = solve_missionaries_and_cannibals(total_missionaries, total_cannibals, boat_capacity)
    if solution:
        print(f"Initial state:\nLeft: M:{total_missionaries}, C:{total_cannibals}, B:1 | Right: M:0, C:0, B:0")
        print(f"Solution path for {total_missionaries} Missionaries, {total_cannibals} Cannibals, and Boat capacity {boat_capacity}:\n")
        for i in range(len(solution) - 1):
            current_state, boat_on_left = solution[i]
            next_state, _ = solution[i + 1]
            lM, lC, rM, rC = current_state
            boat_status_left = "B:1" if boat_on_left else "B:0"
            boat_status_right = "B:0" if boat_on_left else "B:1"
            print(f"Left: M:{lM}, C:{lC}, {boat_status_left} | Right: M:{rM}, C:{rC}, {boat_status_right}")
            print()
            description = describe_step(current_state, next_state, boat_on_left)
            print(f"Step {i + 1}:")
            print(description)
        final_state, boat_on_left = solution[-1]
        lM, lC, rM, rC = final_state
        boat_status_left = "B:1" if boat_on_left else "B:0"
        boat_status_right = "B:0" if boat_on_left else "B:1"
        print(f"Left: M:{lM}, C:{lC}, {boat_status_left} | Right: M:{rM}, C:{rC}, {boat_status_right}")
        print("\nSolution found")
    else:
        print("No solution found.")
def get_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Invalid input. Please enter a positive integer.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")
if __name__ == "__main__":
    missionaries = get_positive_integer("Enter the number of missionaries: ")
    cannibals = get_positive_integer("Enter the number of cannibals: ")
    boat_capacity = get_positive_integer("Enter the boat capacity: ")
    print_solution(missionaries, cannibals, boat_capacity)
