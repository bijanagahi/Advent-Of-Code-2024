def solve(left, right):
    total_dist = 0
    for l in left:
        if l in right:
            total_dist += l*right[l]
    print(total_dist)
    


if __name__ == '__main__':
    left = []
    right = {}
    for l,r in [_.rstrip().split() for _ in open("input.txt",'r').readlines()]:
        left.append(int(l))
        r = int(r)
        right[r] = 1 if r not in right else right[r]+1
    solve(left, right)