import math

# Constants for the game
PILES = [5, 5, 5]
NUM_PILES = 3
MAX_REMOVAL = 3
MIN_REMOVAL = 1
MINIMAX_DEPTH = 3

# Define player roles
HUMAN = 0
COMPUTER = 1

# Static evaluation function for the Minimax algorithm.
# This heuristic helps the computer choose a good move within its limited search depth.
# The objective in Nim is to avoid taking the last object. This means the player
# who can leave the opponent with a very small number of total objects is in a good position.
# Our simple heuristic is the negative of the total number of objects. The maximizing
# player (the computer) will try to maximize this value, which means it will
# try to leave the opponent with the minimum number of objects possible.
# A high positive value indicates a winning state for the computer, and a high
# negative value indicates a losing state.
def evaluate_state(piles):
    """
    Evaluates the current game state from the perspective of the computer (maximizing player).
    Returns a score based on the remaining objects.
    A score of 100 means the computer wins, -100 means the human wins.
    For non-terminal states, a score is calculated as a negative of the total objects.
    This encourages the computer to make moves that result in fewer total objects,
    guiding it towards a winning end-game state.
    """
    total_objects = sum(piles)
    if total_objects == 0:
        # If the game is over and it's the computer's turn, it means the human took the last
        # object, so the human loses and the computer wins.
        return 100
    
    # A simple heuristic: maximize the negative sum of the objects.
    # This means the computer will choose moves that lead to the lowest possible sum of objects.
    return -total_objects

def get_possible_moves(piles):
    """
    Generates all valid moves from the current game state.
    A move is a tuple (pile_index, objects_to_remove).
    """
    moves = []
    for i in range(len(piles)):
        for j in range(MIN_REMOVAL, min(MAX_REMOVAL, piles[i]) + 1):
            moves.append((i, j))
    return moves

def is_game_over(piles):
    """
    Checks if the game has ended.
    The game ends when all piles are empty.
    """
    return all(p == 0 for p in piles)

def minimax(piles, depth, is_maximizing_player):
    """
    The Minimax algorithm with a fixed depth for decision-making.
    
    Args:
        piles (list): The current state of the game piles.
        depth (int): The current search depth.
        is_maximizing_player (bool): True if it's the computer's turn, False for human.
        
    Returns:
        int: The best score for the current player.
        tuple: The best move (pile_index, objects_to_remove).
    """
    # Base case: if depth is 0 or the game is over, return the evaluated score.
    if depth == 0 or is_game_over(piles):
        return evaluate_state(piles), None

    possible_moves = get_possible_moves(piles)
    if not possible_moves:
        # If no moves are possible, the current player loses.
        return evaluate_state(piles), None

    best_move = None

    if is_maximizing_player:
        # Computer's turn (maximize the score)
        best_score = -math.inf
        for move in possible_moves:
            new_piles = piles[:]
            new_piles[move[0]] -= move[1]
            
            score, _ = minimax(new_piles, depth - 1, False)
            
            if score > best_score:
                best_score = score
                best_move = move
        return best_score, best_move
    else:
        # Human's turn (minimize the score)
        best_score = math.inf
        for move in possible_moves:
            new_piles = piles[:]
            new_piles[move[0]] -= move[1]
            
            score, _ = minimax(new_piles, depth - 1, True)
            
            if score < best_score:
                best_score = score
                best_move = move
        return best_score, best_move

def play_game():
    """
    Main function to run the Nim game.
    """
    current_piles = PILES[:]
    current_player = HUMAN  # Human starts first

    print("Welcome to Nim!")
    print("The game starts with 3 piles, each with 5 objects.")
    print("Rules: You can remove 1 to 3 objects from any single pile.")
    print("The player who is forced to take the last object loses.")
    
    while not is_game_over(current_piles):
        print(f"\nCurrent Piles: {current_piles}")

        # Check if the current player has any valid moves
        if not get_possible_moves(current_piles):
            if current_player == HUMAN:
                print("Human has no valid moves. You Lose! The Computer Wins!")
            else:
                print("Computer has no valid moves. The Computer Loses! You Win!")
            break

        if current_player == HUMAN:
            # Human's turn
            print("It's your turn.")
            try:
                pile_index = int(input(f"Enter pile number (1 to {NUM_PILES}): ")) - 1
                remove_count = int(input(f"Enter number of objects to remove (1 to {MAX_REMOVAL}): "))
                
                # Validate the human's move
                if (0 <= pile_index < NUM_PILES and 
                    MIN_REMOVAL <= remove_count <= MAX_REMOVAL and 
                    current_piles[pile_index] >= remove_count):
                    
                    current_piles[pile_index] -= remove_count
                    print(f"You removed {remove_count} objects from pile {pile_index + 1}.")
                    current_player = COMPUTER
                else:
                    print("Invalid move. Please try again.")
            except ValueError:
                print("Invalid input. Please enter numbers.")
        
        else:
            # Computer's turn
            print("It's the computer's turn.")
            
            # Use Minimax to find the best move
            _, best_move = minimax(current_piles, MINIMAX_DEPTH, True)

            if best_move:
                pile_index, remove_count = best_move
                current_piles[pile_index] -= remove_count
                print(f"The computer removed {remove_count} objects from pile {pile_index + 1}.")
            else:
                # Should not be reached if get_possible_moves is checked correctly
                print("Computer has no valid moves. You Win!")
                break
                
            current_player = HUMAN

    if sum(current_piles) == 0:
        # The player who made the last move wins, because the opponent can't move.
        if current_player == HUMAN:
            print("The Computer took the last object. You Win!")
        else:
            print("You took the last object. The Computer Wins!")

if __name__ == "__main__":
    play_game()


