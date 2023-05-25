.data
    dest: .word case0, case1, case2
.text
    #; sll $t0, $t0, 2 #; choose the case

    li $t0, 0 #; first case 
    addi $t0, $t0, 4 #; jump one case
    #; addi $t0, $t0, 8 #; jump two cases

    lw $t1, dest($t0) #; load case address to $t1
    jr $t1 #; Jump to the case address in $t1 (case0, case1 etc...)

    li $t2, 0
    case0:
        addi $t2, $zero, 0x10
        j break 
    case1:
        addi $t2, $zero, 0x20
        j break 
    case2:
        addi $t2, $zero, 0x30
        j break 
    break:
