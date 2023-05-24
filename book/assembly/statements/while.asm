.data

.text
    li $t0, 0 # x = 0
    li $t1, 0 # i = 0

    while:
        bge $t1, 10, endWhile # if i >= 0, end the while loop
        addi $t0, $t0, 4 # x += 4
        addi $t1, $t1, 1 # i += 1
        j while # repeat cicle
    endWhile:
    
    addi $t0, $t0, 1
