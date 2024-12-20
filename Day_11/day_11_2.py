
def solve(stones:list[int]) -> int:
    memo:dict[int, int] = {}
    # init the memoization dict
    for stone in stones:
        memo[stone] = 1

    for i in range(75):
        new_memo:dict[int, int] = {}
        
        for stone in memo.keys():
            if stone == 0:
                memo_stone(1, memo[stone], new_memo)
            
            elif len(str(stone)) % 2 == 0: #even digits
                left,right = split_stone(stone)
                memo_stone(left, memo[stone], new_memo)
                memo_stone(right, memo[stone], new_memo)
            
            else:
                memo_stone(stone*2024, memo[stone], new_memo)
       
        memo = new_memo
    
    return sum([x for x in memo.values()])

def memo_stone(stone:int, count:int, memo:dict[int, int]) -> None:
    if stone in memo:
        memo[stone] += count
    else:
        memo[stone] = count

def split_stone(stone:int)->tuple[int, int]:
    num_digits:int = len(str(stone))
    str_stone:str = str(stone)
    return (int(str_stone[:num_digits//2]), int(str_stone[num_digits//2:]))

if __name__ == '__main__':
    stones:list[int] =  [int(x) for x in [_.rstrip() for _ in open("input.txt",'r').readlines()][0].split()]
    total:int = solve(stones)
    print(total)