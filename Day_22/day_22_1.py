from secret import Secret

def solve(lines:list[int]) -> int:
    s:Secret
    total:int = 0
    for starting_value in lines:
        s = Secret(starting_value)
        for i in range(2000):
            s.get_next()
        # print(s.secret)
        total += s.secret
    return total

if __name__ == '__main__':
    lines:list[int] =  [int(_.rstrip()) for _ in open("input.txt",'r').readlines()]
    total:int = solve(lines)
    print(total)