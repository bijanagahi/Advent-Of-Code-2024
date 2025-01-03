from secret import Secret, Xorshift

def solve(lines:list[int]) -> int:
    x:Xorshift
    total:int = 0
    # sliding_window:dict[tuple[int,int,int,int],int] = {}
    sliding_window:dict[str,int] = {}

    for seed in lines:
        seeds:list[int] = []
        diffs:list[int] = []
        seen_windows:set[str] = set()
        x = Xorshift(seed)
        for i in range(2000):
            seeds.append(x.get_ones())
            x.shift()
        # add comment here
        for idx,value in enumerate(seeds[1:]):
            diffs.append(seeds[idx+1] - seeds[idx])
        
        # add comment here
        for i in range(len(diffs)-3):
            key = ''.join([str(_) for _ in diffs[i:i+4]])
            value = seeds[i+4]
            
            if key in seen_windows:
                continue
            seen_windows.add(key)
            
            if key in sliding_window:
                sliding_window[key] += value
            else:
                sliding_window[key] = value
        
    highest:int = 0
    highest_key:str = ''
    for key,value in sliding_window.items():
        highest = max(highest,value)
    for key,value in sliding_window.items():
        if value == highest:
            highest_key = key
    print(highest_key,highest)

            

    total += x.state
    return total

if __name__ == '__main__':
    lines:list[int] =  [int(_.rstrip()) for _ in open("input.txt",'r').readlines()]
    total:int = solve(lines)
    # total:int = solve([123])
    print(total)