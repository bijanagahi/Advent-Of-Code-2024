from classes.helper import Loc

test:bool = False
width:int = 11 if test else 101
height:int = 7 if test else 103

def solve(lines:list[str]) -> int:
    quads:list[int] = [0, 0, 0, 0, 0]
    for line in lines:
        position:Loc = Loc(*[int(_) for _ in line.split()[0][2:].split(',')]) # don't @ me.
        velocity:Loc = Loc(*[int(_)*100 for _ in line.split()[1][2:].split(',')])
        # We should just be able to multiply the velocities by 100 and add the position
        # then mod by the grid size.
        final_pos:Loc = Loc.add(position,velocity)
        final_pos = Loc(final_pos.x%width,final_pos.y%height)
        quads[get_quad(final_pos)]+=1
    print(quads)
    return quads[1]*quads[2]*quads[3]*quads[4]

def get_quad(pos:Loc) -> int:
    mid_x:int = width//2
    mid_y:int = height//2
    if pos.x == mid_x or pos.y == mid_y:
        return 0 # in the middle
    if pos.x < mid_x and pos.y < mid_y:
        return 1
    if pos.x < mid_x and pos.y > mid_y:
        return 2
    if pos.x > mid_x and pos.y > mid_y:
        return 3
    if pos.x > mid_x and pos.y < mid_y:
        return 4
    return 0

if __name__ == '__main__':
    lines:list[str] =  [_.rstrip() for _ in open(f"{'test' if test else 'input'}.txt",'r').readlines()]
    total:int = solve(lines)
    print(total)