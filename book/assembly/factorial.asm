.data
    number: .word 5
.text
    lw $t0 number # 
    li $t1, 1 # result

    while:
        beqz $t0, endWhile
        mul $t1, $t1, $t0
        sub $t0, $t0, 1
        j while
    endWhile:
