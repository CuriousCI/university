.data 
    vector: .word 4, -1, 5, 500, 0, 10000, -256
    size: .word 5
    sums: .word 0, 0

.text
    #; find max value in vector

    la $t0, vector #; t0 = current address
    la $t1, vector #; t1 = end of vector

    la $t2, size #; t2 = address of vector size
    lw $t2, ($t2) #; t2 = vector size
    sll, $t2, $t2, 2 #; t2 *= 4, to accomodate words

    add $t1, $t1, $t2 #; t1 = end of vector + vector size

    li $t2, 0 #; t2 = parity 
    li $t4, 0 #; t4 = even 
    li $t5, 0 #; t5 = odd 

    for:
        bgt $t0, $t1, endFor #; if current address > end of vector, end for 

        lw $t3, ($t0) #; load value from current address
        beq $t2, 1, ifIsOdd #; check if current parity is odd

        ifIsEven:
            add $t4, $t4, $t3 #; even += current value
            li $t2, 1 #; parity = odd
            j nextIteration
        ifIsOdd:
            add $t5, $t5, $t3 #; odd += current value
            li $t2, 0 #; parity = even

        nextIteration:
            addi $t0, $t0, 4 #; current address = next address
            j for #; repeat cycle

    endFor:

    la $t6, sums #; t6 = address of the result
    sw $t4, ($t6) #; t6[0] = even 
    sw $t5, 4($t6) #; t6[1] = odd; 4 is used instead of 1 because a word is 4 bytes long
