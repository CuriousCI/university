.globl main

.data
    matrix: .word 2, -10, -10, -10, 2, -10, -10, -10, 2 
    length: .word 3 

.text
    main: 
        la $t0, matrix #; t0: matrix_address = matrix
        la $t1, length #; t1: matrix_length_address = length 
        lw $t1, ($t1) #; t1: matrix_length = *length
        move $t2, $t1 #; t2: jumps_to_do = matrix_length (to count how many jumps are needed to reach the end)

        addi $t1, $t1, 1 #; t1: jump_length = matrix_length += 1 (to jump to next diagonal cell)
        sll $t1, $t1, 2 #; t1: jump_length = jump_length * 4 (because words are 4 bytes long)

        li $t3, 0 #; t3: sum = 0 

        while:
            beq $t2, 0, end #; if jumps_to_do == 0 { end loop }

            lw $t4, ($t0) #; t4: value = *matrix_address
            add $t3, $t3, $t4 #; sum += value

            subi $t2, $t2, 1 #; jumps_to_do -= 1
            add $t0, $t0, $t1 #; matrix_address = matrix_address = jump_length
            j while
        end:

        print: 
            li $v0, 1 #; print integer
            move $a0, $t3 #; integer = sum
            syscall

        return: 
            li $v0, 17 #; exit
            li $a0, 0 #; result = 0
            syscall
