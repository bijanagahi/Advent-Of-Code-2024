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
        '''
        mapper:dict[int,list[int]] = {}
        init_value:int = -1 # start at 0 i guess.
        lol:list[list[int]] = [] # list of lists
        
        for i in range(0,65):
            self._reset(i)
            self.run()
            mapper[i] = self.tape.copy()
            lol.append(self.tape.copy())
        for key,value in mapper.items():
            print(f"[{key}] = {value}")
        lol.sort()
        for line in lol:
            print(line)
        # print(mapper)
        



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
        raise ValueError(f"Attempted to decode combo operand {operand}")
    
    def _reset(self, init_value:int) -> None:
        '''Reset all values except the input program, sets reg_a to init_value'''
        self.a = init_value
        self.b = 0
        self.c = 0
        self.pc = 0
        self.tape = []

    def dump_state(self) -> None:
        print(f"**STATE** Reg_A:{self.a} | Reg_B:{self.b} | Reg_C:{self.c} | PC:{self.pc} | Tape:{self.tape}")