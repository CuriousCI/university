# Syscalls & Procedures

## Syscalls

Syscalls are a powerful tool, which enables interaction with **I/O**, **files**, and **dynamic allocation** of **memory**. The MARS editor supports [59 different syscalls](https://courses.missouristate.edu/kenvollmar/mars/help/syscallhelp.html). Here's a few of useful ones.

To use syscalls, there are some special registers:
- `$v0` is used for the code of the syscall
- `$a0` to `$a3` are used for parameters
- The output is usually saved in `$v0`

By setting these registers to the desired values, and using the `syscall` instruction, the OS will run the operation.

| service | $v0 | arguments | output |
|--|--|--|--|
| print integer | 1 | $a0 = integer to print | |
| print string | 4 | $a0 = address of null-terminated string to print | |
| read integer | 5 | | $v0 contains integer read | |
| read string | 8 | $a0 = address of input buffer <br/> $a1 = maximum number of characters to read | |
| sbrk (allocate heap memory) | 9 | $a0 = number of bytes to allocate | $v0 contains address of allocated memory |
| print character | 11 | $a0 = character to print | |
| read character | 12 | | $v0 contains character read |
| exit | 10 | | |
| exit2 | 17 | $a0 = result | |

### Files

| service | $v0 | arguments | output |
|--|--|--|--|
| open file	| 13 | $a0 = address of null-terminated string containing filename <br/> $a1 = flags <br/> $a2 = mode | $v0 contains file descriptor (negative if error)|
| read from file | 14 | $a0 = file descriptor <br/> $a1 = address of input buffer <br/> $a2 = maximum number of characters to read | $v0 contains number of characters read (0 if end-of-file, negative if error)|
| write to file | 15 | $a0 = file descriptor <br/> $a1 = address of output buffer <br/> $a2 = number of characters to write | $v0 contains number of characters written (negative if error)|
| close file | 16 | $a0 = file descriptor | |


### Hello World!

```armasm
.globl main

.data
    string: .asciiz "Hello World!"

.text
    main: 
        li $v0, 4
        la $a0, string
        syscall
```

## Procedures

Procedures are pieces of code that take parameters, and return a result. They're useful to make the code cleaner and more modular.

```armasm
.globl main

.text
    main:
        li $a0, 5 #; first parameter
        li $a1, 6 #; second parameter
        jal function #; call function

        return:
            li $v0, 17
            li $a0, 0
            syscall #; we have to exit, or the execution will continue

    function:
        subi $sp, $sp, 12 #; we need 4 bytes * 3 registers 
        sw $ra, 8($sp) #; return address
        sw $a0, 4($sp)
        sw $a1, 0($sp)

        #; function body...
        #; I can use jal, because we have saved in memory $ra

        lw $a1, ($sp)
        lw $a0, 4($sp)
        lw $ra, 8($sp)
        addi $sp, $sp, 12 #; reset stack pointer
        
        jr $ra
```

The block the function takes from the **stack** is called **stack frame** or **activation record**. We can use `$fp` to point to the start of the **activation record**, it's rendundant and rarely used.

## Recursions

Functions calling themselves!

> TODO: complete factorial

```armasm
.globl main

.text
    main:
        li $a0, 5
        jal factorial

        print:
            move $a0, $v0 #; integer = result of factorial function
            li $v0, 1 #; print integer
            syscall

        return:
            li $v0, 17
            li $a0, 0
            syscall

    factorial:
        #; jump by 1
        #; recursive step
        #; base case
        returnFactorial:
            lw $ra, ($sp)
            addi $sp, $sp
            jr $ra
```
