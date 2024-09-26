def climbStairs(n: int) -> int:
    if n == 1:
        return 1
    if n == 2:
        return 2
    
    # Initialize the base cases
    first = 1
    second = 2
    
    # Use iteration to calculate the number of ways to reach the nth step
    for i in range(3, n + 1):
        third = first + second
        first = second
        second = third
    
    return second

# Example usage
n = 5
print(f"Number of distinct ways to climb {n} stairs: {climbStairs(n)}")
