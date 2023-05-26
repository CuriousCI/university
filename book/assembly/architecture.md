# Single Clock Cycle Architecture

## ALU Control

[R-type](./mips.md#r-type-instructions) instructions have 6 bits in the `funct` field to control the ALU. The first two bits are the `ALUOp` to indicate 1 of 3 selection codes. Based on the selection code, the next 4 bits could have a different meaning.

| opcode | ALUOp | funct field | operation | ALUControl |
|--|--|--|--|--|
| lw / sw | 00 | don't care <br/> always a sum | sum | 0010 |
| beq | 01 | don't care <br/> always a subtraction | sub | 0110 |
| R-type | 10 | 10_0000 | ALUControl decides <br/> based on last 4 bits | 0010 |

Based on the instruction type, we have different behaviours for the funct field and the ALUControl.

| # | func | function |
|--|--|--|
| 0 | 0000 | AND |
| 1 | 0001 | OR |
| 2 | 0010 | add |
| 6 | 0110 | subtract |
| 7 | 0111 | slt |
| 12 | 1100 | NOR |


## Control Unit Signals

| signal | on false | on true |
|--|--|--| 
| RegDst | write register number comes from rt | write register number comes from rd |
| RegWrite | | the data is written in in the write register |
| ALUSrc | data comes from register 2 | data comes from sign extender (immediate part) |
| PCSrc | next instruction is PC + 4 | next instruction is PC + 4 + immediate |
| MemRead | | read from memory and put in read data value at address | 
| MemWrite | | data at address calculated from ALU, is overwritten by data in register 2 |
| MemToReg | data to write in register file comes from ALU | data to write in register file comes from memory |

### Exercise

> Based on the following instructions, write the truth table for the Control Unit, having as input 6 bits _(opcode)_ and as output 9 bits _(control signals)_

| op | opcode | RegDst | ALUSrc | MemtoReg | RegWrite | MemRead | MemWrite | Branch | ALUOp |
|--|--|--|--|--|--|--|--|--|--|
| R | 000000 | 1 | 0 | 0 | 1 | X | 0 | 0 | 10 |
| lw | 100011 | 0 | 1 | 1 | 1 | 1 | 0 | 0 | 00 |
| sw | 101011 | 0 | 1 | 0 | 0 | X | 1 | 0 | 00 |
| beq | 000100 | 0 | 0 | X | 0 | X | 0 | 1 | 01 |

Note: the exercise is correct, but there are some places in which we can use don't cares instead of actual values. From here, we can create a **PLA** with the necessary functions.
