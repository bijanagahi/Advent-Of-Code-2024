from typing import Callable
from enum import Enum, auto

class GateType(Enum):
    AND = lambda a,b : a & b
    OR  = lambda a,b : a | b
    XOR = lambda a,b : a ^ b

class Wire:
    def __init__(self,id:str) -> None:
        self.id:str = id
        self.state:bool|None = None
        self.connected_gates:dict[str,Gate] = {}

    

    def add_gate(self, gate:'Gate') -> None:
        '''
        Add a gate for which this wire will count as an input.

        Once this wire's state is resolved, go through all its gates and update them.
        '''
        if gate.id in self.connected_gates:
            return
        self.connected_gates[gate.id] = gate
    
    def set_state(self, state:bool) -> None:
        # print(f"Wire {self.id} is updating to {state}")
        self.state = state
        for gate in self.connected_gates.values():
            # print(f"\tTriggering an update on gate {gate.id}")
            gate.update_input(self)
    
    def __str__(self) -> str:
        return f"[{self.id}]: {self.state}"
    

class Gate:
    def __init__(self, type:str, a:Wire, b:Wire, o:Wire) -> None:
        self.id:str = f'{a.id} {type} {b.id} -> {o.id}'
        self.type:str = type
        self.inputs:dict[str,bool|None] = {a.id:None, b.id:None}
        self.resolved_inputs:list[bool]
        self.output_wire:Wire = o
        self.resolved = False

    def update_input(self, wire:Wire) -> None:
        self.inputs[wire.id] = wire.state
        if wire.state is None:
            self.resolved = False
        if None not in self.inputs.values():
            self.resolved = True
            self.resolved_inputs = list([bool(x) for x in self.inputs.values()])
            self.output()
    
    def output(self) -> None:
        out_value:bool
        match self.type:
            case 'AND':
                out_value = all(self.resolved_inputs)
            case 'OR':
                out_value = any(self.resolved_inputs)
            case 'XOR':
                out_value = self.resolved_inputs[0] ^ self.resolved_inputs[1]
        # print(f'\t\tGate {self.id} is now {out_value}')
        self.output_wire.set_state(out_value)
    
    def __str__(self) -> str:
        return f'{self.id} || resolved: {self.resolved} || output: {self.output_wire}'
        


def solve(lines:list[str]) -> int:
    wires:dict[str, Wire] = {} # mapping from wire names to their objects
    gates:dict[str, Gate] = {} # mapping from gate names to their objects
    # starting_wires:list[tuple[str,bool]] = []
    starting_wires:dict[str,bool] = {}
    output_count:int = 0

    # process the starting wires
    while lines:
        line:str = lines.pop(0)
        if line == '':
            break # move on to gates
        wire_name,wire_value = line.split(': ')
        starting_wires[wire_name]  = bool(int(wire_value))
    
    # process the gates (and init the wires)
    while lines:
        line = lines.pop(0)
        input_1,gate_type,input_2,unused,output = line.split()

        wire_1:Wire = getWire(input_1, wires)
        wire_2:Wire = getWire(input_2, wires)
        output_wire:Wire = getWire(output, wires)
        gate:Gate = Gate(gate_type,wire_1,wire_2,output_wire)
        wire_1.add_gate(gate)
        wire_2.add_gate(gate)
        
        
        wires[output] = wire_1
        wires[input_2] = wire_2
        wires[output] = output_wire
        gates[line] = gate
        if output[0] == 'z':
            output_count+=1
    

    '''
    **** PART 2 SHIT *****
    '''

    starting_wires['x00'] = True
    starting_wires['y00'] = True

    # Start setting the starting wire values
    for wire_name,starting_value in starting_wires.items():
        wires[wire_name].set_state(bool(starting_value))

    print(wires['z00'])
    # for gate in gates.values():
    #     print(gate)


    return 0

def getWire(name:str, wires:dict[str, Wire]) -> Wire:
    if name in wires:
        return wires[name]
    wire:Wire = Wire(name)
    wires[name] = wire
    return wire



if __name__ == '__main__':
    lines:list[str] =  [_.rstrip() for _ in open("input.txt",'r').readlines()]
    total:int = solve(lines)
    print(total)