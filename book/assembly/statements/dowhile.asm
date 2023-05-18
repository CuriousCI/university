.data
    
.text
    do:
        addi $t0, $t0, 4
        addi $t1, $t1, 1
    blt $t1, 10, do
        
