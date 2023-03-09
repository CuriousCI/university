.data 
    matrix: .word 0:400
    size: .word 20
.text
    main: 
        la $t0, matrix # load address
        lw $t1, size # load size
        mul $t3, $t1, $t1 # size 
        sll $t3, $t3, 2 # size * 4 for address
        add $t3, $t3, $t0 # initial address + size
        addi $t1, $t1, 1 # size + 1 ?
        sll $t1, $t1, 2 # increment is (n + 1) * 4 

        loop: 
            bge $t0, $t3, end
            lw $t4, ($t0)
            add $t2, $t4, $t2 # add diagonal
            add $t0, $t0, $t1 # move index
            j loop

        end:
            move $a0, $t2 # make register ready for print
            li $v0, 1 # set to print
            syscall # print
            li $v0, 10 # set to stop
            syscall # stop
