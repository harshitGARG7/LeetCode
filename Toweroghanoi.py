def improvisedtowerofhanoi(disks, source, peg1, peg2, destination):
    if disks == 1:
        print(f"Disk 1 moved from {source} to {destination}")
        return
    improvisedtowerofhanoi(disks - 1, source, peg1, destination, peg2)
    print(f"Disk {disks} moved from {source} to {destination}")
    improvisedtowerofhanoi(disks - 1, peg2, peg1, source, destination)

disks = int(input("Enter the number of disks: "))

improvisedtowerofhanoi(disks, "T1", "T2", "T3", "T4")


"""
Solves the Tower of Hanoi puzzle using two temporary pegs.
Args:
    disks(int): The number of disks to move.
    source(str): The source peg label - T1
    peg1(str): The first auxiliary peg label - T2
    peg2(str): The second auxiliary peg label - T3
    destination(str): The destination peg label - T4
pseudocode:
# Get number of disks from the user
# Start the solution with the given peg labels
#Call the recursive function with number of disks as argument
    # if number of disks to be moved is 1, return 1 as it can directly be  moved form source to destination
    # Else :
    # First, move the top n-1 disks from source to peg2, using peg1 as the intermediate peg.
    # Move the largest disk from source to destination.
    # Move the n-1 disks from peg2 to destination, using peg1 as the intermediate peg.
    #repeat the steps
"""
