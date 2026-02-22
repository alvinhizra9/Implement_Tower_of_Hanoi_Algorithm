# Tower of Hanoi Solver (Python)

This project demonstrates a clean recursive solution to the classic **Tower of Hanoi** problem, implemented in Python. The solver outputs the **state of all three rods after every move**, making the algorithm easy to trace and verify.

## What the Code Does

- Starts with `n` disks stacked on **Rod 0** (largest at the bottom).
- Uses recursion to move the full stack to **Rod 2**, using **Rod 1** as an auxiliary rod.
- Records the **exact configuration** of the rods after each disk move.
- Returns the full move history as a single formatted string.

## Why This Shows Strong Skills

### 1) Recursive Problem Solving
The solution uses the optimal recursive approach:

- Move `n-1` disks to the auxiliary rod
- Move the largest disk to the destination rod
- Move `n-1` disks from auxiliary to destination

This reflects understanding of:
- divide-and-conquer recursion
- base and recursive cases
- call stack flow and correctness

### 2) Correct State Management
Instead of only printing moves, the code maintains a real model:

- `rods` is a structured in-memory representation of the puzzle
- Each move is performed using `pop()` and `append()` to enforce stack behavior

This shows ability to:
- represent a problem with appropriate data structures (lists as stacks)
- mutate state safely and predictably

### 3) Use of Closures and `nonlocal`
The code uses nested functions and captures outer variables cleanly:

- `get_state()` reads from `rods` without global variables
- `hanoi()` updates the output log via `nonlocal out`

This demonstrates:
- understanding of Python scoping rules
- ability to organize code into small, reusable inner functions

### 4) Traceable Output (Debug-Friendly)
Logging every rod state after each move makes the algorithm transparent:

- easy to test
- easy to compare expected vs. actual behavior
- useful for teaching, debugging, and verification

## Complexity

- **Moves:** `2^n - 1` (optimal for Tower of Hanoi)
- **Time Complexity:** `O(2^n)`
- **Space Complexity:** `O(n)` due to recursion depth

## Usage

```python
print(hanoi_solver(3))
