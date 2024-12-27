from typing import Callable

class Computer:
    def __init__(self, a:int, b:int, c:int, program:list[int]) -> None:
        # Registers
        self.a:int = a 
        self.b:int = b
        self.c:int = c

        # Program Counter and current state
        self.pc:int = 0
        self.program:list[int] = program

        # output tape
        self.tape:list[int] = []

        # supported opcodes
        self.opcodes:list[Callable[[int], None]] = [self._adv,
                                      self._bxl,
                                      self._bst,
                                      self._jnz,
                                      self._bxc,
                                      self._out,
                                      self._bdv,
                                      self._cdv]
        
        # for part 2, stores all possible answers.
        self.possible_starting_values:list[int] = []
    
    def run(self) -> None:
        '''
        Run the computer.

        We'll perform a loop of fetch, decode, and execute steps; stopping when the pc runs off the list
        '''

        while self.pc < len(self.program)-1:
            # Fetch
            opcode:int = self.program[self.pc]
            operand:int = self.program[self.pc+1]
            # print(f"Executing {opcode},{operand}")
            # Decode/Execute in one step
            self.opcodes[opcode](operand)
            # self.dump_state()

            # Don't increment program counter if we jumped
            if opcode == 3 and self.a != 0:
                continue
            self.pc += 2
    
    def run_part_2(self) -> int:
        '''
        Continuously run the computer, looking for a starting value of reg_a
        that results in the same program being output.

        Return that intial value

        Note from the future - this absolutely does NOT work. I'm keeping it in still because
        it was useful as a data exploration tool but dear god don't try to brute force this problem.
        '''
        mapper:dict[int,list[int]] = {}
        init_value:int = -1 # start at 0 i guess.
        lol:list[list[int]] = [] # list of lists
        
        for i in range(0,2**16):
            self._reset(i)
            self.run()
            mapper[i] = self.tape.copy()
            lol.append(self.tape.copy())
        for key,value in mapper.items():
            print(f"[{key}] = {value}")
        lol.sort()
        for line in lol:
            print(line)
        return 0
    
    def explore(self, answer:int, cur_index:int, program:list[int]) -> None:
        '''
        We're going to build the target value backwards.
        For each value in the reversed program input, we figure out what 3 bits will satisfy it
        
        Unfortunately, this solution is custom-built for my input so you'll have to change the logic
        if you're using this in the future.

        This is a recursive function because of all the possiblities, so we also need to know what the 
        current answer and current location within the loop we are.
        '''
        # Base case: we're done with the input and want to check our work
        if cur_index >= len(program):
            try:
                # this is guarded because it's possible a bad input throws when decoding the combo operand.
                self._reset(answer)
                self.run()
            except ValueError as e:
                print(f"Program errored out: {e}")
                return

            if self.tape == self.program:
                # print(f"Possible Answer:{answer}")
                self.possible_starting_values.append(answer)
            return
        
        # Grab all valid values to hit this target:
        target:int = program[cur_index]
        cur_index += 1
        valid_values:list[int] = self.solve_for_target(answer,target)
        
        if len(valid_values) == 0:
            return # we can't find a valid value here, so break out of this logic
        
        # All these values _could_ work, so we'll have to recurse
        for valid_value in valid_values:
            self.explore( ((answer << 3) | valid_value),cur_index, program)

    def solve_for_target(self,answer_so_far:int, target:int) -> list[int]:
        '''
        Given an integer, determine what 3-bit value will cause the program to output our target.
        '''
        valid_values:list[int] = []
        for i in range(8):
            # Do the operations
            # Remember - these are custom to my input so if you're trying to use this it might not work.
            a_reg:int = (answer_so_far << 3) | i
            b_reg = i
            b_reg ^= 7
            c_reg = a_reg >> b_reg
            b_reg = b_reg ^ c_reg
            b_reg ^= 0b0100
            b_reg = b_reg % 8
            
            # Check if we got the desired result
            if b_reg == target:
                valid_values.append(i) # append i as it was the originally chosen value, not reg_b
        
        return valid_values


    def _adv(self,operand:int) -> None:
        self.a = self.a // 2**self.decode_combo(operand)
    
    def _bxl(self,operand:int) -> None:
        self.b = self.b ^ operand

    def _bst(self,operand:int) -> None:
        self.b = self.decode_combo(operand) % 8
    
    def _jnz(self,operand:int) -> None:
        if self.a == 0:
            return
        self.pc = operand

    def _bxc(self,operand:int) -> None:
        self.b = self.b ^ self.c
    
    def _out(self,operand:int) -> None:
        self.tape.append(self.decode_combo(operand) % 8)

    def _bdv(self,operand:int) -> None:
        self.b = self.a // 2**self.decode_combo(operand)
    
    def _cdv(self,operand:int) -> None:
        self.c = self.a // 2**self.decode_combo(operand)

    def decode_combo(self,operand) -> int:
        if operand <= 3:
            return operand
        match operand:
            case 4:
                return self.a
            case 5:
                return self.b
            case 6:
                return self.c
        raise ValueError(f"Attempted to decode combo operand {operand}, tape at {self.tape}")
    
    def _reset(self, init_value:int) -> None:
        '''Reset all values except the input program, sets reg_a to init_value'''
        self.a = init_value
        self.b = 0
        self.c = 0
        self.pc = 0
        self.tape = []

    def dump_state(self) -> None:
        print(f"**STATE** Reg_A:{self.a} | Reg_B:{self.b} | Reg_C:{self.c} | PC:{self.pc} | Tape:{self.tape}")