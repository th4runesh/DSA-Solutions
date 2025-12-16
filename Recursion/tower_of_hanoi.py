def tower_of_hanoi(n, source, auxiliary, target):
    """
    Solves the Tower of Hanoi problem recursively.
    n: number of disks
    source: source rod
    auxiliary: auxiliary rod
    target: target rod
    """
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    tower_of_hanoi(n - 1, source, target, auxiliary)
    print(f"Move disk {n} from {source} to {target}")
    tower_of_hanoi(n - 1, auxiliary, source, target)

if __name__ == "__main__":
    n = 3
    print(f"Tower of Hanoi solution for {n} disks:")
    tower_of_hanoi(n, 'A', 'B', 'C')
