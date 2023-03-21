.globl main

.data

.text
    main: 
        li $a0, 4 # param1
        li $a1, 3 # param2
        li $a2, 9 # param3
        jal foo

        move $t0, $v0

        # return 0;
        li $v0, 17
        li $a0, 0
        syscall

    foo:
        addi $sp, $sp, -16 # move stack pointer
        sw $a0, 12($sp) # save params
        sw $a1, 8($sp) 
        sw $a2, 4($sp) 
        sw $ra, 0($sp) # save $ra

        # function body
        li $v0, 0
        add $v0, $a0, $a1
        add $v0, $v0, $a2

        lw $a0, 12($sp) # read params
        lw $a1, 8($sp) 
        lw $a2, 4($sp) 
        lw $ra, 0($sp) # read $ra
        addi $sp, $sp, 16 # reset stack pointer

        jr $ra # return
