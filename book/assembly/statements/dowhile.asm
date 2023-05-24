.data
    
.text
    li $t0, 0 # x = 0
    li $t1, 0 # i = 0

    do:
        addi $t0, $t0, 4 # x += 4
        addi $t1, $t1, 1 # i += 1
    blt $t1, 10, do # if i < 10, repeat the cicle 
        
