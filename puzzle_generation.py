import random


size = 9
subgrid_size = 3
initial_board = []
candidate_list = []

# Initialize the candidate list based on the current board state
def initialize_candidate_list(board):
    global candidate_list
    candidate_list = [[set() for _ in range(size)] for _ in range(size)]

    for row in range(size):
        for col in range(size):
            if board[row][col] == 0:
                for num in range(1, size + 1):
                    if is_valid(board, num, row, col):
                        candidate_list[row][col].add(num)


def update_candidate_list(board, row, col, num, add):
    start_row = (row // subgrid_size) * subgrid_size
    start_col = (col // subgrid_size) * subgrid_size

    for i in range(size):
        candidate_list[row][i].discard(num)
        candidate_list[i][col].discard(num)

    for i in range(subgrid_size):
        for j in range(subgrid_size):
            candidate_list[start_row + i][start_col + j].discard(num)

    if add:
        for i in range(1, size + 1):
            if is_valid(board, i, row, col):
                candidate_list[row][col].add(i)


def is_valid(board, num, row, col):
    # Check if the number is in the given row or column
    for i in range(size):
        if board[row][i] == num or board[i][col] == num:
            return False

    # Check if the number is in the subgrid
    start_row = (row // subgrid_size) * subgrid_size
    start_col = (col // subgrid_size) * subgrid_size
    for i in range(subgrid_size):
        for j in range(subgrid_size):
            if board[start_row + i][start_col + j] == num:
                return False

    return True


def find_empty_cell(board):
    # Find an empty cell (represented by 0)
    for i in range(size):
        for j in range(size):
            if board[i][j] == 0:
                return (i, j)
    return None


def is_solved(board):
    return find_empty_cell(board) is None


def eliminate(board):
    progress = False
    for row in range(size):
        for col in range(size):
            if board[row][col] == 0 and len(candidate_list[row][col]) == 1:
                num = next(iter(candidate_list[row][col]))
                board[row][col] = num
                update_candidate_list(board, row, col, num, False)
                progress = True
    return progress


def only_choice(board):
    progress = False
    for num in range(1, size + 1):
        # Check each row
        for row in range(size):
            candidates = []
            for col in range(size):
                if board[row][col] == 0 and num in candidate_list[row][col]:
                    candidates.append(col)
            if len(candidates) == 1:
                board[row][candidates[0]] = num
                update_candidate_list(board, row, candidates[0], num, False)
                progress = True

        # Check each column
        for col in range(size):
            candidates = []
            for row in range(size):
                if board[row][col] == 0 and num in candidate_list[row][col]:
                    candidates.append(row)
            if len(candidates) == 1:
                board[candidates[0]][col] = num
                update_candidate_list(board, candidates[0], col, num, False)
                progress = True

        # Check each subgrid
        for box_row in range(0, size, subgrid_size):
            for box_col in range(0, size, subgrid_size):
                candidates = []
                for i in range(subgrid_size):
                    for j in range(subgrid_size):
                        row = box_row + i
                        col = box_col + j
                        if board[row][col] == 0 and num in candidate_list[row][col]:
                            candidates.append((row, col))
                if len(candidates) == 1:
                    row, col = candidates[0]
                    board[row][col] = num
                    update_candidate_list(board, row, col, num, False)
                    progress = True

    return progress


def naked_pairs(board):
    progress = False

    # Check rows for naked pairs
    for row in range(size):
        for col in range(size):
            if len(candidate_list[row][col]) == 2:
                pair = list(candidate_list[row][col])
                for other_col in range(col + 1, size):
                    if len(candidate_list[row][other_col]) == 2 and all(num in pair for num in candidate_list[row][other_col]):
                        # Eliminate pair from other cells in the row
                        for i in range(size):
                            if i != col and i != other_col and board[row][i] == 0:
                                for num in pair:
                                    if num in candidate_list[row][i]:
                                        candidate_list[row][i].remove(num)
                                        progress = True

    # Check columns for naked pairs
    for col in range(size):
        for row in range(size):
            if len(candidate_list[row][col]) == 2:
                pair = list(candidate_list[row][col])
                for other_row in range(row + 1, size):
                    if len(candidate_list[other_row][col]) == 2 and all(num in pair for num in candidate_list[other_row][col]):
                        # Eliminate pair from other cells in the column
                        for i in range(size):
                            if i != row and i != other_row and board[i][col] == 0:
                                for num in pair:
                                    if num in candidate_list[i][col]:
                                        candidate_list[i][col].remove(num)
                                        progress = True

    # Check subgrids for naked pairs
    for box_row in range(0, size, subgrid_size):
        for box_col in range(0, size, subgrid_size):
            for i in range(subgrid_size):
                for j in range(subgrid_size):
                    row = box_row + i
                    col = box_col + j
                    if len(candidate_list[row][col]) == 2:
                        pair = list(candidate_list[row][col])
                        for k in range(i, subgrid_size):
                            for l in range(j + 1, subgrid_size):
                                other_row = box_row + k
                                other_col = box_col + l
                                if len(candidate_list[other_row][other_col]) == 2 and all(num in pair for num in candidate_list[other_row][other_col]):
                                    # Eliminate pair from other cells in the subgrid
                                    for m in range(subgrid_size):
                                        for n in range(subgrid_size):
                                            cell_row = box_row + m
                                            cell_col = box_col + n
                                            if (cell_row != row or cell_col != col) and (cell_row != other_row or cell_col != other_col) and board[cell_row][cell_col] == 0:
                                                for num in pair:
                                                    if num in candidate_list[cell_row][cell_col]:
                                                        candidate_list[cell_row][cell_col].remove(num)
                                                        progress = True

    return progress


def shuffle(array):
    for i in range(len(array) - 1, 0, -1):
        j = random.randint(0, i)
        array[i], array[j] = array[j], array[i]
    return array


def solve(board):
    cell = find_empty_cell(board)
    if cell is None:
        return True

    row, col = cell
    numbers = shuffle(list(range(1, size + 1)))  # Shuffle numbers 1-9

    for num in numbers:
        if is_valid(board, num, row, col):
            board[row][col] = num
            if solve(board):
                return True
            board[row][col] = 0

    return False


def generate_solved_board():
    board = [[0] * size for _ in range(size)]
    solve(board)
    return board


def count_solutions(board):
    cell = find_empty_cell(board)
    if cell is None:
        return 1

    row, col = cell
    count = 0

    # Generate candidate list for the current cell
    candidates = []
    for num in range(1, size + 1):
        if is_valid(board, num, row, col):
            candidates.append(num)

    # Try each candidate
    for num in candidates:
        board[row][col] = num
        count += count_solutions(board)
        if count > 1:
            break  # Early exit if more than one solution is found
        board[row][col] = 0

    return count


def remove_numbers(board, difficulty):
    if difficulty == 'easy':
        attempts = 35
    elif difficulty == 'medium':
        attempts = 40
    elif difficulty == 'hard':
        attempts = 45
    else:
        attempts = 50

    max_iterations = 500
    iteration_count = 0

    puzzle = [row[:] for row in board]

    # Create a list of filled cells
    filled_cells = [(row, col) for row in range(size) for col in range(size) if puzzle[row][col] != 0]

    while attempts > 0 and iteration_count < max_iterations:
        iteration_count += 1

        # Randomly select a filled cell
        row, col = random.choice(filled_cells)

        backup = puzzle[row][col]
        puzzle[row][col] = 0

        copy = [row[:] for row in puzzle]
        if count_solutions(copy) != 1:
            puzzle[row][col] = backup
        else:
            # If the cell is successfully cleared, remove it from the list of filled cells
            filled_cells.remove((row, col))
            attempts -= 1

    # print("iteration_count:", iteration_count)
    return puzzle


def deep_copy(board):
    return [row[:] for row in board]


def solve_with_logic(board):
    initialize_candidate_list(board)
    progress = True
    while progress:
        progress = False
        progress = eliminate(board) or progress
        progress = only_choice(board) or progress
        progress = naked_pairs(board) or progress

    return is_solved(board)  # Return True if the puzzle is fully solved by logic


def generate_human_solvable_puzzle(difficulty):
    puzzle = None
    iterations = 0
    while puzzle is None:
        iterations += 1
        solved_board = generate_solved_board()
        puzzle = remove_numbers(solved_board, difficulty)

        # Create a deep copy of the puzzle for the logical solver
        puzzle_copy = deep_copy(puzzle)

        # Check if the puzzle can be solved using logic alone
        if not solve_with_logic(puzzle_copy):
            puzzle = None  # Regenerate if not solvable by logic

    #print(f"Puzzle generated in {iterations} attempt(s)")
    return puzzle, solved_board
