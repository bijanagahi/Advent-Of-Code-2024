from classes.disk import Disk, Block, Type

def solve(line:str) -> int:
    i:int = 0
    disk:Disk = Disk()

    cur_file_id:int = 0
    while i < len(line):
        
        # Create and add the file
        file_size:int = int(line[i])
        disk.add_file(Block(Type.FILE,cur_file_id,file_size))
        cur_file_id+=1

        # create and add the space
        if i+1 < len(line):
            space_length:int = int(line[i+1])
            disk.add_space(Block(Type.SPACE, -1,space_length))
        # Increment i by 2 because we jumped two
        i+=2

    disk.defrag_part_1()
    return disk.calcualte_checksum()

if __name__ == '__main__':
    line:str =  [_.rstrip() for _ in open("input.txt",'r').readlines()][0]
    total:int = solve(line)
    print(total)