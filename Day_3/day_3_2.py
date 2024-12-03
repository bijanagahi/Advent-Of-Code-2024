import re

if __name__ == '__main__':
    # We doin regex matching boiiiii
    input =  ''.join([_.rstrip() for _ in open("input.txt",'r').readlines()])
    input = re.sub("don't\\(\\).+?do\\(\\)","",input) # delete everything between the don't() and do()
    total = 0
    mults = re.findall("mul\\([0-9]{1,3},[0-9]{1,3}\\)",input)
    for mult in mults:
        x,y = re.findall("[0-9]{1,3},[0-9]{1,3}",mult)[0].split(',')
        total += int(x)*int(y)
    print(total)