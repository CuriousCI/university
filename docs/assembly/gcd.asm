.globl main

.data

.text
    main:
        li $v0, 5 # read int
        syscall
        move $a0, $v0 # x of gcd

        li $v0, 5 # read int
        syscall
        move $a1, $v0 # y of gcd

        jal gcd

        move $v0, $a0 # gcd result
        li $v0, 1 # print int
        syscall
    
        li $v0, 17 # exit
        li $a0, 0 # 0 
        syscall

    gcd:
        equals: # if x == y set $v0 = x, return
            bne $a0, $a1, greater
            move $v0, $a0
            j return


        greater: # if x > y, swap $a0, $a1, call gcd
            blt $a0, $a1, lower

            move $t0, $a0 # temp = x
            move $a0, $a1 # x = y
            move $a1, $t0 # y = temp

            subi $sp, $sp, 4 
            sw $ra, ($sp)

            jal gcd

            lw $ra, ($sp)
            addi $sp, $sp, 4

            # $v0 is already set to result!
            j return

        lower: # if x < y, y -= x, gcd
            sub $a1, $a1, $a0

            subi $sp, $sp, 4 
            sw $ra, ($sp)

            jal gcd

            lw $ra, ($sp)
            addi $sp, $sp, 4

            # $v0 is already set to result!

        return:
            jr $ra
