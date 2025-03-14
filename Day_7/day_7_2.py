from itertools import product

def solve(lines:list[str]) -> int:
    total:int = 0
    line:str
    for line in lines:
        # Set up, grab the target value and all the operands
        target:int = int(line.split(":")[0])
        operands:list[int] = [int(x) for x in line.split(":")[1].split()]
        calibrated:bool = False # is the equation valid?

        # Now, using a binary mask, iterate all possible combinations,
        # replacing:
        #          0 with '+'
        #          1 with '*'
        #          2 with '|'
        # Eval at all points.
        mask:tuple
        for mask in list(product([0, 1, 2], repeat=len(operands) -1)):
            operators:list[str] = get_operators(mask)
            
            if eval(operands,operators) == target:
                calibrated = True
                break

        if calibrated:
            total += target

    return total

'''
Evaluates an equation from left to right

Takes the first two values in the operands list, applies the next operator in the list,
forwards the result along.
'''
def eval(operands:list[int], operators:list[str]) ->int:
    total:int = operands[0]
    operand:int
    operator:str
    for operand in operands[1:]:
        operator = operators.pop(0)
        match operator:
            case '+':
                total += operand
            case '*':
                total *= operand
            case '|':
                total = int(str(total) + str(operand))
    return total

def get_operators(mask:tuple) -> list[str]:
    operators:list[str] = []
    for bit in mask:
        match bit:
            case 0:
                operators.append('+')
            case 1:
                operators.append('*')
            case 2:
                operators.append('|')
    return operators

if __name__ == '__main__':
    lines:list[str] =  [_.rstrip() for _ in open("input.txt",'r').readlines()]
    total:int = solve(lines)
    print(total)