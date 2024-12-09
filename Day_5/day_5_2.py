from classes.rulebook import Rulebook

def solve(lines:list[str]) -> int:
    rulebook:Rulebook = Rulebook() #init
    total:int = 0
    start_of_updates:int = 0

    # Start with adding all the rules.
    for i,line in enumerate(lines):
        if line == '':
            start_of_updates = i+1 # next line will start the updates
            break
        rulebook.add_rule(line)
    
    # Process all the updates
    for update in lines[start_of_updates:]:
        if rulebook.validate(update):
            continue # skip valid ones this time
        new_update:list[int] = rulebook.fix_update(update)
        total+=new_update[len(new_update)//2]
    
    return total

def get_middle_page(update_line) -> int:
    pages:list[int] = [int(_) for _ in update_line.split(',')]
    return pages[len(pages)//2]

if __name__ == '__main__':
    lines:list[str] =  [_.rstrip() for _ in open("input.txt",'r').readlines()]
    total:int = solve(lines)
    print(total)