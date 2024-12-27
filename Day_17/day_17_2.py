from computer import Computer

def solve(lines:list[str]) -> None:
    # Parse input
    reg_a:int = int(lines[0].split(' ')[2])
    reg_b:int = int(lines[1].split(' ')[2])
    reg_c:int = int(lines[2].split(' ')[2])
    program:list[int] = [int(x) for x in lines[4].split(' ')[1].split(',')]
    
    # Initialize the computer
    computer = Computer(reg_a, reg_b, reg_c, program.copy())
    
    # Reverse the program because we're building it backwards.
    program.reverse()
    computer.explore(0,0,program)
    print(f"All possible values: {computer.possible_starting_values}")
    computer.possible_starting_values.sort()
    print(f"Lowest one: {computer.possible_starting_values[0]}")

if __name__ == '__main__':
    lines:list[str] =  [_.rstrip() for _ in open("input.txt",'r').readlines()]
    solve(lines)

'''
2,4 - A%8 -> B (keep bottom 3 bits, write to B)
1,7 - B^7 -> B (flips the bits)
7,5 - A//2**B -> C (right shift A by B bits into C)
4,1 - B^C -> B (xor b and c)
1,4 - B^4 -> B (flip the 3rd bit of B)
5,5 - print B (!)
0,3 - A//2**3 (shift right 3)
3,0 - jump back to start until a is 0
'''