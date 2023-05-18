# MIPS

## RISC vs CISC

**Reduced Instruction Set Computer** vs **Complex Instruction Set Computer**

| RISC | CISC |
|:--|:--|
| **fixed size** instructions | **variable size** instructions _(requires decode before fetch)_ |
| **fixed format** | **variable format**  _(complex decode)_ |
| operations **only with registers** | **in-memory operands** |
| **many registers** | **few of registers** |
| **single access** to memory | **multiple accesses** to memory  | 
| **fixed** instruction **duration** | **variable** instruction **duration** |
| simple **conflicts** | complex **conflicts** |
| faster **pipeline** | complex **pipeline** |

## Registers

| name | number | use | keep |
|--|--|--|:--:|
| $zero | 0 | 0 constant | ? | 
| $at | 1 | reserved for assembler | ? |
| $v0 - $v1 | 2 - 3 | expression evaluation and results of functions | no |
| $a0 - $a3 | 4 - 7 | arguments | no |
| $t0 - $t7 | 8 - 15 | temporary | no |
| $s0 - $s7 | 16 - 23 | saved temporary | yes |
| $t8 - $t9 | 24 - 25 | temporary | no |
| $k0 - $k1 | 26 - 27 | reserved for OS Kernel | ? |
| $gp | 28 | global pointer | yes | 
| $sp | 29 | stack pointer | yes |
| $fp | 30 | frame pointer | yes |
| $ra | 31 | return address | yes |

### Special registers

- **$gp** points into the middle of a **64K block** of memory in the **heap** that holds constants and **global variables**
- **$sp** points to the last location in use on the **stack**
- **$fp** points to the start of the stack frame and does not move for the duration of the subroutine call, and the parameters that are passed into the subroutine remain at a constant spot relative to the frame pointer 
- **$ra**  is written with the return address for a call by the **jal** instruction

## Instructions



### R-type Instructions

Arithmetic Instruction Format _(type to a register)_

```assembly
add $t0, $s1, $s2
```

- add **opcode** \\(\to\\) 000000
- $t0 in **rd** \\(\to\\) 01000
- $s1 in **rs**, \\(\to\\) 10001
- $s2 in **rt**, \\(\to\\) 10010
- add **funct** \\(\to\\)  100000

| op | rs | rt | rd | shamt | funct |
|:--:|:--:|:--:|:--:|:--:|:--:|
| 000000 | 10001 | 10010 | 01000 | 00000 | 100000 |
| 6b | 5b | 5b | 5b | 5b | 6b |
| opcode | first <br/> register <br/> source | second <br/> register <br/> source | register <br/> destination <br/> operand | shift <br/> amount | function <br/> code | 

<!-- | \\(0..5\\) | \\(6..10\\) | \\(11..15\\) | \\(16..20\\) | \\(21..25\\) | \\(26..31\\) | -->

### I-type Instructions

Data Transfer Format _(conditional jumps)_

```assembly
addi $t2, $s2, 4 
```

- addi **opcode** \\(\to\\) 001000
- $t2 in **rt** \\(\to\\) 01010
- $s2 in **rs** \\(\to\\) 10010

| op | rs | rt | constant |
|:--:|:--:|:--:|:--:|
| 001000 | 10010 | 01010 | 0000000000000100 |
| 6b | 5b | 5b | 16b |
| opcode | first <br/> register | target <br/> register | constant value or <br/> address | 

<!-- | \\(0..5\\) | \\(6..10\\) | \\(11..15\\) | \\(16..31\\) | -->

### J-type Instructions

Unconditional Jumps

```assembly
j label
``` 
- PC \\(\leftarrow\\) label \\(\cdot\\) 4

| op | address |
|:--:|:--|
| 001000 | 10010010100000000000000100 |
| 6 bit | 26 bit |
<!-- | \\(0..5\\) | \\(6..31\\) | -->

### FR-type Instructions

MIPS handles floating point instructions like regular 32b instructions. FR-type don't access the memory, and are executed by the **FPU**.

```assembly
add.s $f0, $f1, $f2 ; single precision
div.d $f0, $f2, $f4 ; double precision
```

| op | rs | rt | rd | shamt | funct |
|:--:|:--:|:--:|:--:|:--:|:--:|
| 000000 | 10001 | 10010 | 01000 | 00000 | 100000 |
| 6b | 5b | 5b | 5b | 5b | 6b |
| opcode | first <br/> register <br/> source | second <br/> register <br/> source | register <br/> destination <br/> operand | shift <br/> amount | function <br/> code | 


### FI-type Instructions

FI-type are used for:
- load / store
- conditional jumps

```assembly
lwc1 $f1, indirizzo
bc1f cc, offset
```

| op | rs | rt | constant |
|:--:|:--:|:--:|:--:|
| 001000 | 10010 | 01010 | 0000000000000100 |
| 6b | 5b | 5b | 16b |
| opcode | first <br/> register | target <br/> register | constant value or <br/> address | 


## Interrupts
