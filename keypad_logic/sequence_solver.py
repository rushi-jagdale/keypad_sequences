from .keypad_layout import keypad, vowels, is_valid_move

# Dictionary to store results of subproblems (memoization)
cache = {}

# Recursive function to count valid sequences
def count_sequences(remaining_steps, vowel_count, current_key):
    # Base case: If no more steps are left, check if the sequence is valid
    if remaining_steps == 0:
        return 1 if vowel_count <= 2 else 0
    
    # Check if the result is already in the cache
    cache_key = (remaining_steps, vowel_count, current_key)
    if cache_key in cache:
        return cache[cache_key]
    
    # Recursive case: Explore all valid moves
    total = 0
    for next_key in keypad:
        if is_valid_move(current_key, next_key):  # Only move to valid keys
            new_vowel_count = vowel_count + (1 if next_key in vowels else 0)
            if new_vowel_count <= 2:  # Only proceed if the vowel count is valid
                total += count_sequences(remaining_steps - 1, new_vowel_count, next_key)
    
    # Store the result in the cache
    cache[cache_key] = total
    return total