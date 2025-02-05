# Keypad layout with keys and their positions
keypad = {
    'A': (0, 0), 'B': (0, 1), 'C': (0, 2), 'D': (0, 3), 'E': (0, 4),
    'F': (1, 0), 'G': (1, 1), 'H': (1, 2), 'I': (1, 3), 'J': (1, 4),
    'K': (2, 0), 'L': (2, 1), 'M': (2, 2), 'N': (2, 3), 'O': (2, 4),
    '1': (3, 0), '2': (3, 1), '3': (3, 2)
}

# Vowels in the keypad
vowels = {'A', 'E', 'I', 'O'}

# Check if a move is a valid knight's move
def is_valid_move(current_key, next_key):
    if current_key not in keypad or next_key not in keypad:
        return False
    current_row, current_col = keypad[current_key]
    next_row, next_col = keypad[next_key]
    row_diff = abs(current_row - next_row)
    col_diff = abs(current_col - next_col)
    return (row_diff == 1 and col_diff == 2) or (row_diff == 2 and col_diff == 1)

    



   