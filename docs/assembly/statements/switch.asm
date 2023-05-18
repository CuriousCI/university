.data
    dest: .word case0, case1, caseN
.text
    # sll $t0, $t0, 2 # Choose the case
    # lw $t0, $zero # First case 
    addi $t0, $t0, 4 # Jump one case
    # addi $t0, $t0, 8 # Jump two cases
    lw $t1, dest($t0) # Load case address to $t1
    jr $t1 # Jump to the case address in $t1 (case0, case1 etc...)

    case0:
        addi $t2, $zero, 0x10
        j endSwitch
    case1:
        addi $t2, $zero, 0x20
        j endSwitch
    caseN:
        addi $t2, $zero, 0x30
        j endSwitch
    endSwitch:
