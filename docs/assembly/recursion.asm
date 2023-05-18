.globl main

.data
    number: .word 5
    result: .word 0

.text
    main:
        # load parameter and calculate factorial
        lw $a0, number
        jal factorial

        # print result
        move $a0, $v0
        li $v0, 1
        syscall

        # return 0
        li $v0, 17
        li $a0, 0
        syscall


    factorial:
        blez $a0, base # if base case

        recursion:
            subi $sp, $sp, 8 # I need 2 words for $ra & $a0, which holds the value of n
            sw $ra, 0($sp) # store stack pointer
            sw $a0, 4($sp) # store n

            subi $a0, $a0, 1 # set parameter n - 1
            jal factorial # jump & link factorial

            lw $ra, 0($sp) # load $ra from stack
            lw $a0, 4($sp) # load $a0 from stack
            addi $sp, $sp, 8 # reset stack pointer 

            mul $v0, $v0, $a0 # multiply factorial

            jr $ra # return?

        base:
            addi $v0, $zero, 1 # 0! = 1! = 1

            jr $ra # return?
