.globl main

.data
    array: .word 98, 19, 22, 12, 8943, 23, 12, 4441, 24, 1244124, 895, 181, 109, 121901, 10001, 2190
    size: .word 16

.text
    main:
        # print array
        la $a0, array
        lw $a1, size
        jal print

        # sort array
        la $a0, array # start = array pointer
        lw $a1, size 
        sll $a1, $a1, 2
        add $a1, $a1, $a0 # base address + size * 4
        jal insertionSort

        # print array
        la $a0, array
        lw $a1, size
        jal print


        li $v0, 17 # exit
        li $a0, 0 # 0 
        syscall

    # a0 = array pointer
    # a1 = size 
    print:
        move $s1, $a0 # address of element to print
        move $s2, $a1 # move size
        sll $s2, $s2, 2 # size * 4
        subi $s2, $s2, 4
        add $s2, $s2, $s1 # address + size

        whilePrint:
            li $v0, 1 # print int
            lw $a0, ($s1) # int to print
            syscall

            li $v0, 11 # print char
            li $a0, ' ' # space 
            syscall

            bge $s1, $s2, returnPrint

            addi $s1, $s1, 4 # address += 4
            j whilePrint

        returnPrint:
            li $v0, 11 # print char
            li $a0, 10 # new line 
            syscall

            jr $ra # return
        

    # a0 = from where 
    # a1 = to where 
    insertionSort:
        #  for int i = 0; i < a0 + a2 * 4; i++ 
        #    for j = i; j > 0; j--
        #      if a[j] < a[j - 1]: swap a[j] a[j - 1]
        #      else break


        move $s0, $a0 # start
        move $s1, $a1 # end
        
        addi $s0, $s0, 4 # start from index 1
        forElement:
            bge $s0, $s1, returnInsertionSort # start >= end, return

            move $s3, $s0 # j index

            whileLeftBigger:
                beqz $s3, breakInsertion  # if j == 0, break

                subi $s4, $s3, 4 # j - 1
                lw $t0, ($s3) # load j
                lw $t1, ($s4) # load j - 1

                ble $t1, $t0, breakInsertion # a[j - 1] <= a[j] ? break

                swap:
                    sw $t1, ($s3)
                    sw $t0, ($s4)

                subi $s3, $s3, 4 # j -= 1
                j whileLeftBigger

            breakInsertion:
                addi $s0, $s0, 4
                j forElement
                

        returnInsertionSort: 
            jr $ra


    # a0 = left start pointer 
    # a1 = left end pointer 
    # a2 = right start pointer 
    # a3 = right end pointer
    merge:
        move $s0, $a0 # left start pointer 
        move $s1, $a1 # left end pointer
        move $s2, $a2 # right start pointer
        move $s3, $a3 # right end pointer

        li $v0, 9 # allocate in heap
        sub $a0, $s3, $s0 # right end - left start
        srl $a0, $a0, 2 # div (right end - left start) / 4 to get size
        syscall

        move $s4, $v0 # address of heap allocated space!

        # allocate empty array
        # create 3 indexes: merge, left, righ 
        # merge operation (while)
        # merge all left remaining 
        # merge all right remaining 

    timSort:
        # fin k
        # check wheter dimension is good 
        # if dimension is good, do an insertionSort
        # else split in two, and merge
