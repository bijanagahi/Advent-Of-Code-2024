from enum import Enum

class Type(Enum):
    FILE = 1
    SPACE = 2

class Block():
    def __init__(self, type:Type, id:int, start:int, size:int) -> None:
        self.type:Type = type
        self.id:int = id
        self.size:int = size
        self.start:int = start
    
    def __str__(self) -> str:
        # return f"{self.type.name}{':'+str(self.id) if self.type == Type.FILE else ''}@{self.start}->{self.start+self.size}"
        return f"{self.type.name}[{str(self.id) if self.type == Type.FILE else ''}]:{self.start}->{self.start+self.size}({self.size})"
    def __repr__(self) -> str:
        return self.__str__()

class Disk():
    def __init__(self) -> None:
        self.files:list[Block] = [] # all the file blocks,  in order
        self.free_memory:list[Block] = [] # All the space blocks, in order
        self.defragged_memory:list[Block] = [] # the final memory arrangement 
        self.memory:list[Block] = [] # Unused, just for debugging

    def defrag_part_1(self) -> None:
        # pop the left-most space off, set chunk size to it's size
        # pop the right-most file off, see if we can chunk it
        self.defragged_memory.append(self.files.pop(0)) #start with the first file
        
        while self.files:
            space:Block = self.free_memory.pop(0)
            chunk:int = space.size # how much space we have to work with
            while chunk > 0:
                if not self.files:
                    break # we ran out of files, just break
                
                next_file:Block = self.files.pop() # grab the last file
                
                if chunk >= next_file.size:
                    # if this chunk is bigger or equal to the file, we can move the whole thing
                    self.defragged_memory.append(next_file)
                    chunk -= next_file.size
                else:
                    # we have to frag this file, only move as much as is available
                    to_save:int = next_file.size - chunk # Remainder of file
                    file_to_move:Block = Block(Type.FILE, next_file.id, 0,chunk) # start doesn't matter here
                    file_to_save:Block = Block(Type.FILE, next_file.id, 0, to_save) # start doesn't matter here
                    self.defragged_memory.append(file_to_move)
                    self.files.append(file_to_save) # push this file back on the stack
                    chunk = 0
            
            # now add the next file
            if self.files:
                self.defragged_memory.append(self.files.pop(0))
        
        # self.dump_defragged_memory()
    
    def defrag_part_2(self) -> None:
        '''
        Start with the right-most file. Attempt to find a space for it. Repeat.
        '''
        for file in self.files[::-1]: # go backwards through the list.
            # print(f"Looking at {file}")
            space:Block|None = self.find_first_valid_space(file)
            # print(f"\tValid Space: {space}")
            if space is None:
                continue # we couldn't find a space for this file, move on.

            # since we're moving this file, create a new space Block in it's place.
            self.free_memory.append(Block(Type.SPACE, 0, file.start,file.size))
            # print(f"\t\tAdding space block to index {file.start} with size {file.size}")

            # Now move the file
            file.start = space.start

            # Finally, check if the space should be updated and put back into the list
            if file.size < space.size:
                self.free_memory.append(Block(Type.SPACE, 0, space.start+file.size,space.size-file.size))
        
        self.compute_memory()
    
    def compute_memory(self)->None:
        '''
        Merge the free memory and files arrays and put them in order.
        '''
        self.memory = self.free_memory+self.files
        self.memory.sort(key=lambda x:x.start)

    def find_file_index_for_size(self, size:int) -> int|None:
        '''
        Returns the first file that is less than or equal to the given size.
        Returns None if no file for that size was found
        '''
        for i,file in enumerate(self.files[::-1]): # reverse order (last file first)
            if file.size <= size:
                return len(self.files)-i-1
        return None # couldn't find a file that fits.


    def find_first_valid_space(self, file:Block) ->Block|None:
        '''
        Removes and returns the Block containing the left-most space that is >= the given size.
        Returns None if no space is found
        '''
        self.free_memory.sort(key=lambda x:x.start)
        for i,space in enumerate(self.free_memory):
            if space.size >= file.size and space.start < file.start:
                return self.free_memory.pop(i) # remove it from the list
        return None


    def calcualte_checksum(self) -> int:
        total:int = 0
        file_ids:list[int] = []
        for item in self.defragged_memory:
            file_ids.extend([item.id]*item.size)

        for i,id in enumerate(file_ids):
            total += i*id
        return total
    
    def calcualte_checksum_2(self) -> int:
        total:int = 0
        file_ids:list[int] = []
        for item in self.memory:
            file_ids.extend([item.id]*item.size)

        for i,id in enumerate(file_ids):
            total += i*id
        return total
    
    def add_file(self, file:Block) -> None:
        self.files.append(file)
        self.memory.append(file)
    
    def add_space(self, space:Block) -> None:
        self.free_memory.append(space)
        self.memory.append(space)
    
    def dump_defragged_memory(self) -> None:
        builder:str = ''
        for item in self.defragged_memory:
            builder += '.'*item.size if item.type == Type.SPACE else str(item.id)*item.size
        print(builder)        
    
    def __str__(self) -> str:
        builder:str = ''
        for item in self.memory:
            builder += '.'*item.size if item.type == Type.SPACE else str(item.id)*item.size
        return builder