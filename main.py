def hanoi_solver(disks):
    # Initialize the three rods:
    # - rod 0 starts with all disks (largest at the bottom, smallest at the top)
    # - rods 1 and 2 start empty
    rods = [[i for i in range(disks, 0, -1)], [], []]

    def get_state():
        # Return a string representation of the current state of all rods
        return f"{rods[0]} {rods[1]} {rods[2]}"

    # Start the output with the initial state
    out = get_state()

    def hanoi(n, source, destination, aux):
        # We want to modify the 'out' variable from the outer scope,
        # so we declare it as nonlocal
        nonlocal out

        # Base case: if there is only one disk, move it directly
        if n == 1:
            val = rods[source].pop()         # Remove the top disk from the source rod
            rods[destination].append(val)    # Place it on the destination rod
            out += "\n" + get_state()        # Record the new state after the move
        else:
            # Step 1: move the top n-1 disks from source to auxiliary rod
            hanoi(n - 1, source, aux, destination)

            # Step 2: move the largest disk (the nth disk) from source to destination
            val = rods[source].pop()
            rods[destination].append(val)
            out += "\n" + get_state()

            # Step 3: move the n-1 disks from auxiliary rod to destination rod
            hanoi(n - 1, aux, destination, source)

    # Solve the puzzle by moving all disks from rod 0 to rod 2 using rod 1 as auxiliary
    hanoi(disks, 0, 2, 1)

    # Return the full log of all rod states after each move
    return out
