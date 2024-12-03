def solve(left, right):
    total_dist = 0
    for i in range(len(left)):
        total_dist += abs(left[i] - right[i])
    print(total_dist)
    


if __name__ == '__main__':
    left = []
    right = []
    for l,r in [_.rstrip().split() for _ in open("input.txt",'r').readlines()]:
        left.append(int(l))
        right.append(int(r))
    left.sort()
    right.sort()
    solve(left, right)