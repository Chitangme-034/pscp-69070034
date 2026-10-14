"""Forward"""
def main():
    """Message"""
    n, s = map(int, input().split())
    forwarding = [0]
    for _ in range(n):
        forwarding.append(int(input()))
    visited = set()
    current = s
    count = 0
    while current and current not in visited:
        visited.add(current)
        count += 1
        current = forwarding[current]
    print(count)
main()
