from keypad_logic.sequence_solver import count_sequences
from keypad_logic.keypad_layout import keypad, vowels
import time

def solve():
    total_sequences = 0
    for start_key in keypad:
        # Initialize vowel count based on the starting key
        initial_vowel_count = 1 if start_key in vowels else 0
        # Count sequences starting with this key (9 more steps to go)
        total_sequences += count_sequences(9, initial_vowel_count, start_key)
    
    return total_sequences

if __name__ == "__main__":
    start_time = time.time()
    result = solve()
    end_time = time.time()
    execution_time = end_time - start_time
    
    print("Total Number of Possible Sequences:", result)
    print("Total Execution Time:", execution_time, "seconds")