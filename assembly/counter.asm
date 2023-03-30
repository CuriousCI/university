.globl main

.data
    buffer: .space 20

.text

    main: 
        la $a0, buffer # address of string
        li $a1, 20 # max chars to read, includes '\0' or not?
        li $v0, 8 # read string
        syscall

        # a0, char address
        jal count

        # $v0 letters count
        # $v1 numbers count
        # $s2 other chars count
        # print each of these

        move $a0, $v0 # letters count
        li $v0, 1 # print int
        syscall

        jal newline

        move $a0, $v1 # numbers count
        li $v0, 1 # print int
        syscall

        jal newline

        move $a0, $s2 # other count
        li $v0, 1 # print int
        syscall

        li $v0, 17 # exit
        li $a0, 0 # 0
        syscall

    newline:
        li $a0, 10 # newline
        li $v0, 11 # print char
        syscall

        jr $ra

    count:
        # reset return registers
        li $v0, 0
        li $v1, 0
        li $s2, 0
        lb $t0, ($a0)

        nullchar:
            beqz $t0, return

        # a-z, A-Z
        a: 
            blt $t0, 'a', A
        z:
            ble $t0, 'z', letter

        A: 
            blt $t0, 'A', zero 
        Z:
            ble $t0, 'Z', letter

        # 0-9
        zero: 
            blt $t0, '0', other
        nine:
            ble $t0, '9', number

        letter:
            addi $v0, $v0, 1
            j next

        number:
            addi $v1, $v1, 1
            j next

        other: 
            addi $s2, $s2, 1

        next: 
            # call count on next
            subi $sp, $sp, 16
            sw $ra, ($sp)
            sw $v0, 4($sp)
            sw $v1, 8($sp)
            sw $s2, 12($sp)

            addi $a0, $a0, 1
            jal count

            move $t0, $v0
            move $t1, $v1
            move $t2, $s2

            lw $ra, ($sp)
            lw $v0, 4($sp)
            lw $v1, 8($sp)
            lw $s2, 12($sp)
            addi $sp, $sp, 16

            # sum $v0, $v1, $s2 
            add $v0, $v0, $t0
            add $v1, $v1, $t1
            add $s2, $s2, $t2

        return:
            jr $ra
