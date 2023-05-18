.data
    vector: .word 4, -1, 5, 500, 0, 10000, -256
    size: .word 5
    sums: .word 0, 0
.text
    lw $t0, size # size
    li $t2, 0 # even
    li $t3, 0 # odd

    li $t1, 0 # index
    for:
        bge $t1, $t0, exit # if index > size
        sll $t5, $t1, 2 # shift index
        lw $t4, vector($t5) # get value at index
        andi $t6, $t1, 1 # bitmask 0x1

        beqz $t6, even # check even/odd
        odd: 
            add $t3, $t3, $t4 # add to odd
            j endIf 
        even:
            add $t2, $t2, $t4 # add to even
        endIf:
        
        addi $t1, $t1, 1
        j for
    exit:
    li $t7, 4
    sw $t2, sums
    sw $t3, sums($t7)
