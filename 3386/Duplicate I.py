"""Duplicate I"""
def main():
    """Both groups"""
    m = int(input())
    n = int(input())
    group_one = set()
    group_two = set()
    for _ in range(m):
        group_one.add(int(input()))
    for _ in range(n):
        group_two.add(int(input()))
    common = group_one & group_two
    if not common:
        print("Nope")
    else:
        for student_id in sorted(common, reverse=True):
            print(student_id)
main()
