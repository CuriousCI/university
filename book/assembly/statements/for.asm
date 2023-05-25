.data

.text
    li $t0, 0 #; x = 0
    li $t1, 0 #; i = 0

    for:
        add $t0, $t0, $t1 #; x += i
        addi $t1, $t1, 1 #; i += 1 
        blt $t1, 10, for #; if i <= 10, repeat 

