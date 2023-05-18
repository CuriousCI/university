.globl main

.data
    matrix: .word 1, 2, 3, 9, 21, 214, 11, 22, 9
    size: .byte 3

.text
    main: 
        la $a0, matrix
        lb $a1, size # load byte, not word!


        li $a2, 0 # main diagonal 
        li $a3, 1 # count center

        jal sum_diagonal 
        move $a0, $v0 # save value
        sum $s0, $s0, $v0


        li $a2, 1 # secondary diagonal 
        li $a3, 1 # don't count center

        jal sum_diagonal
        move $a0, $v0
        sum $s0, $s0, $v0


        # print(result)
        li $v0, 1
        move $a0, $s0
        syscall


        # return 0;
        li $v0, 17
        li $a0, 0
        syscall

    sum_diagonal: 
        
