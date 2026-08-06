"""Bridge"""
def main():
    """Calculate minimum small bricks"""
    small_bricks = int(input())
    big_bricks = int(input())
    goal = int(input())
    use_big = goal // 5             # Use many big bricks as possible
    if use_big > big_bricks:
        use_big = big_bricks
    remaining = goal - use_big * 5  # Calculate remaining length
    if remaining > small_bricks:    # Check if enough small bricks are available
        print(-1)
    else:
        print(remaining)
main()
