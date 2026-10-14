"""Tile Sound Inspection"""
def main():
    """Defective and Penalty"""
    n, penalty = input().split()
    n = int(n)
    penalty = float(penalty)
    tiles = []
    for _ in range(n):
        tiles.append(list(map(int, input().split())))
    total_tiles = 0
    total_points = 0
    for row in tiles:
        row_tiles = 0
        row_points = 0
        for value in row:
            if value > 0:
                row_tiles += 1
            row_points += value
        total_tiles += row_tiles
        total_points += row_points
        print(*row, row_tiles, row_points)
    for j in range(n):
        column_tiles = 0
        for i in range(n):
            if tiles[i][j] > 0:
                column_tiles += 1
        print(column_tiles, end=" " if j < n - 1 else "\n")
    for j in range(n):
        column_points = 0
        for i in range(n):
            column_points += tiles[i][j]
        print(column_points, end=" " if j < n - 1 else "\n")
    print(total_tiles, total_points, f"{total_points * penalty:.2f}")
main()
