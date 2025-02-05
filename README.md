## How It Works

The solution is implemented in Python and consists of the following components:
1. **Keypad Layout**: The keypad is represented as a dictionary, where each key is mapped to its position (row, column).
2. **Knight's Move Validation**: A function checks if a move from one key to another is a valid knight's move.
3. **Recursive Solver**: A recursive function counts all valid sequences, using memoization to optimize performance.
4. **Main Function**: The main function starts the process, iterates over all possible starting keys, and calculates the total number of valid sequences.


# How to Run

### Prerequisites
- Python 3.x installed on your system.

### Steps
1. Clone the repository:

   git clone https://github.com/rushi-jagdale/keypad_sequences.git
   cd keypad_sequences

   python run_solver.py
