.globl main

.data

.text
    main:

        li $a0, 5
        li $a1, -3
        li $a2, 9
        li $a3, 2
        jal avgOfSquareAbsSub
        
        print:
            move $a0, $v0 #; integer = formula 
            li $v0, 1 #; print integer
            syscall

        return:
            li $v0, 17 #; exit
            li $a0, 0 #; result = 0
            syscall

    avgOfSquareAbsSub:
        subi $sp, $sp, 8 #; ra, first result
        sw $ra, ($sp) 

        jal squareAbsSub #; x, y 
        sw $v0, 4($sp) #; t0: first = (|x|-|y|)^2

        move $a0, $a2
        move $a1, $a3
        jal squareAbsSub #; w, z
        move $t1, $v0 #; t1: second = (|w|-|z|)^2
        lw $t0, 4($sp) #; t0: first = (|x|-|y|)^2

        add $t0, $t0, $t1 #; first += second
        srl $v0, $t0, 1 #; numerator /= 2
        
        returnAvg:
            lw $ra, ($sp)
            addi $sp, $sp, 8
            jr $ra

    squareAbsSub:
        subi $sp, $sp, 4 #; ra
        sw $ra, ($sp)

        jal abs #; |x|
        move $t0, $v0 #; t0: abs_x = |x|

        move $a0, $a1 #; number = y
        jal abs #; |y|
        move $t1, $v0 #; t1: abs_y = |y|

        sub $t0, $t0, $t1 #; difference = |x| - |y|
        mul $v0, $t0, $t0 #; result = (|x| - |y|)^2
        
        returnSub:
            lw $ra, ($sp)
            addi $sp, $sp, 4
            jr $ra

    abs:
        bge $a0, 0, returnAbs #; if number >= 0, return 

        ca2:
            nor $a0, $a0, $zero #; number = bitwise not of number
            addi $a0, $a0, 1 #; number += 1
        
        returnAbs:
            move $v0, $a0 #; result = |number|
            jr $ra
