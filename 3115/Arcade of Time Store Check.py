"""Arcade of Time : Store Check"""
def main():
    """Number of stores open at each given time"""
    num, check = input().split()
    num = int(num)
    check = int(check)
    time = [0] * 1441
    for _ in range(num):
        start, stop = input().split()
        start = int(start)
        stop = int(stop)
        time[start] += 1
        time[stop] -= 1

    # Calculate number of stores open at each minute
    for minute in range(1, 1441):
        time[minute] += time[minute - 1]
    queries = input().split()
    result = []
    for i in range(check):
        minute = int(queries[i])
        result.append(str(time[minute]))
    print(" ".join(result))
main()
