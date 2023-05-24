.data
    array: .word 11, 35, 2, 17, 29, 95
    size: .word 6
.text
    lw $t0, array($zero)
    lw $t1, size
    li $t2, 0 # $t2: i = 0

    for: bge $t2, $t1, endFor

        # current value in $t3, compare to next value
        # current value in $t0, compare to next value in $t0 + $t2 << 2

    endFor:
