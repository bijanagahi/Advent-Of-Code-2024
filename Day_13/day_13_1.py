import numpy as np
import re

def solve(lines:list[str]) -> int:
    i:int = 0
    total:int = 0
    processed:int = 0
    valid:int = 0
    while i < len(lines):
        processed+=1
        
        # grab the a, b, and target coordinates
        all_coordinates = parse_block(i,lines)
        a_coordinates:tuple[int,int] = all_coordinates[0]
        b_coordinates:tuple[int,int] = all_coordinates[1]
        t_coordinates:tuple[int,int] = all_coordinates[2]
        
        moves = np.array([list(a_coordinates),list(b_coordinates)])
        target = np.array(list(t_coordinates))
        moves_inv = np.linalg.inv(moves)
        ans = np.matmul(target,moves_inv)

        # Numpy floating point math is dumb.
        # Check if the answer is all ints
        if (abs(ans[0] - round(ans[0])) < 0.001) and (abs(ans[1] - round(ans[1])) < 0.001):
            valid+=1
            total += round(ans[0])*3 + round(ans[1])
        
        i += 4 # skip to the next block
    print(f"Processed {processed} commands, {valid} were valid")
    return total

def parse_block(start:int, lines:list[str]) -> list[tuple[int,int]]:
    line:str = lines[start]
    a_coordinates:tuple[int,int] = (int(re.findall(r"X.(\d+)", line)[0]),int(re.findall(r"Y.(\d+)", line)[0]))
    line = lines[start+1]
    b_coordinates:tuple[int,int] = (int(re.findall(r"X.(\d+)", line)[0]),int(re.findall(r"Y.(\d+)", line)[0]))
    line = lines[start+2]
    t_coordinates:tuple[int,int] = (int(re.findall(r"X.(\d+)", line)[0]),int(re.findall(r"Y.(\d+)", line)[0]))
    return [a_coordinates,b_coordinates,t_coordinates]

if __name__ == '__main__':
    lines:list[str] = [_.rstrip() for _ in open("input.txt",'r').readlines()]
    total = solve(lines)
    print(total)