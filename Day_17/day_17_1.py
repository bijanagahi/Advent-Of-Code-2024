from computer import Computer

def solve(lines:list[str]) -> int:
    reg_a:int = int(lines[0].split(' ')[2])
    reg_b:int = int(lines[1].split(' ')[2])
    reg_c:int = int(lines[2].split(' ')[2])
    program:list[int] = [int(x) for x in lines[4].split(' ')[1].split(',')]
    
    computer = Computer(reg_a, reg_b, reg_c, program)
    computer.run()
    print(','.join([str(x) for x in computer.tape]))
    return 0

if __name__ == '__main__':
    lines:list[str] =  [_.rstrip() for _ in open("input.txt",'r').readlines()]
    total:int = solve(lines)
    print(total)