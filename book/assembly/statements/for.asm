.data

.text
    for:
        add $t0, $t0, $t1 

        addi $t1, $t1, 1 # index++ 
        blt $t1, 23, for # index += 1

