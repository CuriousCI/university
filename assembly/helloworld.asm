.globl main

.data
    string: .asciiz "Hello World!"

.text
    main: 
        li $v0, 4
        la $a0, string

        syscall

