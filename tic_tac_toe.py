import random

def generateSquare(n):
    """Generates a 3x3 magic square."""
    return [[8, 1, 6], [3, 5, 7], [4, 9, 2]]

def printMagicSquareWithMoves(magicSquare, player_moves, computer_moves, player_symbol, computer_symbol):
    """Prints the magic square with the player's and computer's moves."""
    print("Magic Square:")
    for row in magicSquare:
        print(' | '.join(
            f'{player_symbol}' if num in player_moves else
            f'{computer_symbol}' if num in computer_moves else
            f'{num:1}'
            for num in row
        ))
        print('-' * (4 * len(row) - 1))

def checkWin(magicSquare, n, moves):
    """Checks if the given moves result in a win."""
    magic_constant = n * (n * n + 1) // 2
    for i in range(n):
        if sum(magicSquare[i][j] for j in range(n) if magicSquare[i][j] in moves) == magic_constant:
            return True
        if sum(magicSquare[j][i] for j in range(n) if magicSquare[j][i] in moves) == magic_constant:
            return True
    if sum(magicSquare[i][i] for i in range(n) if magicSquare[i][i] in moves) == magic_constant:
        return True
    if sum(magicSquare[i][n - i - 1] for i in range(n) if magicSquare[i][n - i - 1] in moves) == magic_constant:
        return True
    return False

def findWinningMove(magicSquare, n, moves, available_numbers):
    """Finds a winning move for the current player, if available."""
    for number in available_numbers:
        temp_moves = moves + [number]
        if checkWin(magicSquare, n, temp_moves):
            return number
    return None

def tossForFirstPlayer():
    """Simulates a coin toss and returns the result."""
    return random.choice([0, 1])

def tossing():
    """Handles player input for the coin toss."""
    while True:
        try:
            human_choice = int(input("Enter your choice (0 or 1): "))
            if human_choice in [0, 1]:
                return human_choice
            else:
                print("Invalid choice. Please enter 0 or 1.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def playGame(magicSquare, n):
    """Main function to play the game."""
    available_numbers = [num for row in magicSquare for num in row]
    player_moves = []
    computer_moves = []

    printMagicSquareWithMoves(magicSquare, player_moves, computer_moves, " ", " ")

    human_choice = tossing()
    toss_result = tossForFirstPlayer()

    if human_choice == toss_result:
        print("Human won the toss!")
        player_symbol = 'X'
        computer_symbol = 'O'
        current_player = 'X'
    else:
        print("Computer won the toss!")
        player_symbol = 'O'
        computer_symbol = 'X'
        current_player = 'O'

    for turn in range(n * n):
        if current_player == player_symbol:
            while True:
                try:
                    player_move = int(input("Select number from the board: "))
                    if player_move not in available_numbers:
                        raise ValueError("Invalid choice. Choose from the available numbers.")
                    break
                except ValueError as e:
                    print(e)
            player_moves.append(player_move)
            available_numbers.remove(player_move)
            current_player = computer_symbol
        else:
            winning_move = findWinningMove(magicSquare, n, computer_moves, available_numbers)
            if winning_move is not None:
                computer_move = winning_move
            else:
                blocking_move = findWinningMove(magicSquare, n, player_moves, available_numbers)
                if blocking_move is not None:
                    computer_move = blocking_move
                else:
                    computer_move = random.choice(available_numbers)
            print(f"Computer's choice: {computer_move}")
            computer_moves.append(computer_move)
            available_numbers.remove(computer_move)
            current_player = player_symbol

        printMagicSquareWithMoves(magicSquare, player_moves, computer_moves, player_symbol, computer_symbol)

        if checkWin(magicSquare, n, computer_moves):
            print("Computer wins!")
            return
        elif checkWin(magicSquare, n, player_moves):
            print("Player wins!")
            return

    print("It's a draw!")

def main():
    """Main function to run the game loop."""
    while True:
        magicSquare = generateSquare(3)
        playGame(magicSquare, 3)
        play_again = input("Would you like to play again? (yes/no): ").lower()
        if play_again == 'no':
            print("Thanks for playing!")
            break
        elif play_again != 'yes':
            print("Enter a correct choice.")

if __name__ == "__main__":
    main()
