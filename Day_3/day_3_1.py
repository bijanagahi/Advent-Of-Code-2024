import re

if __name__ == '__main__':
    # We doin regex matching boiiiii
    lines =  [_.rstrip() for _ in open("input.txt",'r').readlines()]
    total = 0
    for line in lines:
        mults = re.findall("mul\\([0-9]{1,3},[0-9]{1,3}\\)",line)
        for mult in mults:
            x,y = re.findall("[0-9]{1,3},[0-9]{1,3}",mult)[0].split(',')
            total += int(x)*int(y)
    print(total)