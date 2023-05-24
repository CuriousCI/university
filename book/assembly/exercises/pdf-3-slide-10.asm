.data

.text
    li $s0, 2 # a = 2
    li $s1, 5 # b = 5
    li $s2, 9 # c = 9
    li $s3, 4 # d = 4
    li $s4, 12 # e = 12
    
    # a = ( b - c ) + ( d - e )

    sub $t0, $s1, $s2 # t0 = b - c
    sub $t1, $s3, $s4 # t1 = d - e
    add $s0, $t0, $t1 # s0 = t0 + t1
