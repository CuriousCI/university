.globl main

.data
    matrix: .half 9, 8, 1, 12, 21, 18, 19, 28, 3
    side: .word 3

.text
    main:


        li $v0, 17 # exit
        li $a0, 0 # 0 
        syscall
