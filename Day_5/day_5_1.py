
def solve(grid:list[str]) -> int:
    return 0

if __name__ == '__main__':
    lines:list[str] =  [_.rstrip() for _ in open("test.txt",'r').readlines()]
    total:int = solve(lines)
    print(total)