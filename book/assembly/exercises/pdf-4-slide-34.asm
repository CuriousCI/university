.data 
    vector: .word 11, 35, 2, 7, 29, 95
    size: .word 6

.text
    #; find max value in vector

    la $t0, vector #; t0 = current address
    la $t1, vector #; t1 = end of vector

    la $t2, size #; t2 = address of vector size
    lw $t2, ($t2) #; t2 = vector size
    sll, $t2, $t2, 2 #; t2 *= 4, to accomodate words

    add $t1, $t1, $t2 #; t1 = end of vector + vector size

    lw $t2, ($t0) #; t2 = max value

    for:
        bgt $t0, $t1, endFor #; if current address > end of vector, end for 

        lw $t3, ($t0) #; load value from current address
        ble $t3, $t2, elseSmaller #; if current value <= max value, continue

        ifBigger:
            move $t2, $t3 #; max value = current value

        elseSmaller:

        addi $t0, $t0, 4 #; current address = next address
        j for #; repeat cycle

    endFor:
