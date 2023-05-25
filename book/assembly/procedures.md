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
| read string | 8 | $a0 = address of input buffer; $a1 = maximum number of characters to read | |
| sbrk (allocate heap memory) | 9 | $a0 = number of bytes to allocate | $v0 contains address of allocated memory |
| exit | 10 | | |
| print character | 11 | $a0 = character to print | See note below table |
| read character | 12 | | $v0 contains character read |

### Files

| service | $v0 | arguments | output |
|--|--|--|--|
| open file	| 13 |$a0 = address of null-terminated string containing filename; $a1 = flags; $a2 = mode | $v0 contains file descriptor (negative if error). See note below table |
| read from file | 14 | $a0 = file descriptor; $a1 = address of input buffer; $a2 = maximum number of characters to read | $v0 contains number of characters read (0 if end-of-file, negative if error). See note below table |
| write to file | 15 | $a0 = file descriptor; $a1 = address of output buffer; $a2 = number of characters to write | $v0 contains number of characters written (negative if error). See note below table |
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



<!-- `jal` `j $ra` `$sp` etc... -->
