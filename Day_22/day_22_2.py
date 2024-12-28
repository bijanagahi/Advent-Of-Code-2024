from secret import Secret, Xorshift

def solve(lines:list[int]) -> int:
    x:Xorshift
    total:int = 0
    for seed in lines:
        x = Xorshift(seed)
        for i in range(2000):
            x.shift()
            # print(x.state)
        total += x.state
    return total

if __name__ == '__main__':
    lines:list[int] =  [int(_.rstrip()) for _ in open("input.txt",'r').readlines()]
    total:int = solve(lines)
    print(total)