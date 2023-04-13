.globl main

.data
    # array: .word 98, 19, 22, 12, 8943, 23, 12, 4441, 24, 1244124, 895, 181, 109, 121901, 10001, 2190
    # size: .word 16

    array: .word 7, 8, 9, 12, 2, 4, 8, 10 
    size: .word 8

.text
    main:
        # print array
        la $a0, array
        lw $a1, size
        jal print


        # sort array
        # la $a0, array # start = array pointer
        # lw $a1, size 
        # sll $a1, $a1, 2
        # add $a1, $a1, $a0 # base address + size * 4
        # jal insertionSort


        # merge

        la $a0, array # array start 

        la $a1, array # array middle 
        lw $t0, size # mid = size 
        slr $t0, 2 # mid = size / 2
        add $a1, $a1, $t0 # start + mid

        la $a2, array  # array end
        lw $t0, size
        add $a2, $a2, $t0 # end = array + size

        jal merge

        # print array
        la $a0, array
        lw $a1, size
        jal print


        # return 0
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
    # a1 = middle pointer 
    # a2 = right end pointer 
    merge:
        move $s0, $a0 # I need to store the start, for the final merging phase
        move $s1, $a1 # I need to store the end of the left part 
        move $s2, $a2 # end pointer

        li $v0, 9 # allocate in heap
        sub $a0, $s2, $s0 # end - start
        srl $a0, $a0, 2 # div (right end - left start) / 4 to get size
        syscall

        move $s3, $v0 # address of heap allocated space!

        move $t0, $a0 # start pointer, which moves
        move $t1, $a1 # right pointer, which moves
        move $t2, $v0 # moving pointer to current location in array

        whileBothNotEmpty:
            beq $t0, $s1, whileRightNotEmpty # if left == middle, empty right items
            beq $t1, $s2, whileLeftNotEmpty # if right == end, empty left items

            lw $t3, ($t0)
            lw $t4, ($t1)

            # compare left value
            leftSmaller:
                bgt $t3, $t4, rightSmaller
                sw $t2, $t3 # store left value in merged array
                addi $t2, $t2, 1 # merged array pointer++
                addi $t0, $t0, 1 # left++
            
            # compare right value
            rightSmaller:
                sw $t2, $t4 # store right value in merged array
                addi $t2, $t2, 1 # merged array pointer++
                addi $t1, $t1, 1 # left++
                
            # set value at current heap position
            # increment left ($t0) or right ($t1) by 1
            # increment heap address ($t2) by 1 

            j whileBothNotEmpty

        whileLeftNotEmpty:
            beq $t0, $s1, replaceArray # if left == middle, empty right items
            
            j whileLeftNotEmpty

        whileRightNotEmpty:
            beq $t1, $s2, replaceArray # if right == end, empty left items
            
            j whileRightNotEmpty


        replaceArray:
        # allocate empty array
        # create 3 indexes: merge, left, righ 
        # merge operation (while)
        # merge all left remaining 
        # merge all right remaining 

        jr $ra

    timSort:
        # fin k
        # check wheter dimension is good 
        # if dimension is good, do an insertionSort
        # else split in two, and merge
