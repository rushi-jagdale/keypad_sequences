## Problem Statement

You are given a 4x5 keypad with specific letter and number assignments. The goal is to find the total number of unique 10-key sequences that adhere to the following rules:
1. **Starting Point**: The sequence can begin with any key on the keypad.
2. **Knight's Move**: Each subsequent key press must be a valid knight's move from the previous key. A knight's move is defined as:
   - One step vertically and two steps horizontally, **or**
   - One step horizontally and two steps vertically.
3. **Repetition Allowed**: A key can be used multiple times within a sequence.
4. **Vowel Limit**: Each sequence can contain a maximum of two vowels (`A`, `E`, `I`, `O`).

---

## How It Works

The solution is implemented in Python and consists of the following components:
1. **Keypad Layout**: The keypad is represented as a dictionary where each key maps to its coordinates `(row, column)`.
2. **Knight's Move Validation**: A function checks if a move from one key to another is a valid knight's move.
3. **Recursive Solver**: A recursive function counts all valid sequences, using memoization to optimize performance.
4. **Main Function**: The main function iterates over all starting keys, initializes the vowel count, and calls the recursive solver to compute the total number of valid sequences.


# How to Run

### Prerequisites
- Python 3.x installed on your system.

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/rushi-jagdale/keypad_sequences.git
   cd keypad_sequences

   python run_solver.py
