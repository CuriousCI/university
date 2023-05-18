.data
    matrix: .word 0:400 # 0-399, 20x20 matrix
    size: .word 20
.text
    main:
        li $t0, 0 # x
        li $t1, 0 # y
        li $t2, 0 # sum
        li $t3, size # size

        rows: bge $t1, $t3, end
            columns: bge $t0, $t3, nextRow
                bne $t0, $t1, continue
                mul $t4, $t1, $t3 # y * x, index
                add $t4, $t4, $t0 # y * x + x
                sll $t4, $t4, 2 # word => molt. x 4, because of word size in MIPS
                lw $t4, matrix($t4) # load matrix[x][y]
                add $t2, $t4, $t2 # sum diagonal
            continue: 
                addi $t0, $t0, 1 # x++
                j columns
        nextRow:
            li $t0, 0
            addi $t1, $t1, 1 # y++
            j rows

        end:
            move $a0, $t2
            li $v0, 1 # syscall 1 = print int
            syscall
            li $v0, 10 # syscall 10 = stop, used for example when window is closed
            syscall 

# It's better if we use just one for (x is equal to y, always)
# Multiplications & sums in this code are heavy on 







