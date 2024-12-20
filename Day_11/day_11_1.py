
def solve(stones:list[int]) -> int:
    print(f"Stones: {stones}")
    for i in range(25):
        new_stones:list[int] = []
        for stone in stones:
            if stone == 0:
                new_stones.append(1)
            elif len(str(stone)) % 2 == 0: #even digits
                left,right = split_stone(stone)
                new_stones.append(left)
                new_stones.append(right)
            else:
                new_stones.append(stone*2024)
        print(f"Lenght: {len(new_stones)}")
        stones = new_stones
    print(f"Final: {stones}")
    return len(stones)

def split_stone(stone:int)->tuple[int, int]:
    num_digits:int = len(str(stone))
    str_stone:str = str(stone)
    return (int(str_stone[:num_digits//2]), int(str_stone[num_digits//2:]))
    



if __name__ == '__main__':
    # stones:list[int] =  [int(x) for x in [_.rstrip() for _ in open("input.txt",'r').readlines()][0].split()]
    stones = [2024]
    total:int = solve(stones)
    print(total)