.globl main

.data
    # array: .word 98, 19, 22, 12, 8943, 23, 12, 4441, 24, 1244124, 895, 181, 109, 121901, 10001, 2190
    # size: .word 16

    array: .word 7, 8, 9, 12, 2, 4, 8, 10 
    size: .word 8

.text
    main:
        # Print Array
        
        la $a0, array # param1 = array pointer
        lw $a1, size # param2 = array size
        jal print # print(array, size)


        # Insertion Sort
        
        # la $a0, array # start = array pointer
        # lw $a1, size 
        # sll $a1, $a1, 2
        # add $a1, $a1, $a0 # base address + size * 4
        # jal insertionSort
        

        # Merge
        
        # array start pointer
        la $a0, array 

        # array middle pointer
        la $a1, array 
        lw $t0, size # middle = size 
        sll $t0, $t0, 1 # middle = (size * 4) / 2 = size * 2
        add $a1, $a1, $t0 # start pointer + middle

        # array end pointer
        la $a2, array
        lw $t0, size
        sll $t0, $t0, 2 # size = size * 4
        add $a2, $a2, $t0 # end = array + size

        # merge(start, middle, end)
        jal merge


        # Print Array
        
        la $a0, array # param1 = array pointer
        lw $a1, size # param2 = size
        jal print # print(array, size)


        # Return
        
        li $v0, 17 # exit
        li $a0, 0 # 0 
        syscall

    # a0 = array pointer
    # a1 = size 
    print:
    	# TODO: change $s1 to $s0 and $s2 to $s1
        move $s1, $a0 # $s1 = current element address
        move $s2, $a1 # $s2 = size
        subi $s2, $s2, 1 # size -= 1
        sll $s2, $s2, 2 # size *= 4
        add $s2, $s2, $a0 # $s2 = array address + size


        # Print Each Element
	
        whilePrint:
       	    # Print
       	    
            li $v0, 1 # print int
            lw $a0, ($s1) # value to print
            syscall

            li $v0, 11 # print char
            li $a0, ' ' # space 
            syscall

            bge $s1, $s2, returnPrint # out of bounds -> return (put it before?)

            addi $s1, $s1, 4 # address += 4
            j whilePrint


	    # Return
	
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
        move $s2, $a2 # Array end pointer


        # new Array

        li $v0, 9 # allocate in heap
        sub $a0, $s2, $s0 # end - start
        srl $a0, $a0, 2 # div (right end - left start) / 4 to get size
        syscall

        move $s3, $v0 # address of heap allocated space!

        move $t0, $s0 # start pointer, which moves
        move $t1, $s1 # right pointer, which moves
        move $t2, $s3 # moving pointer to current location in array

        sub $s4, $s2, $s1 # start pointer - end pointer
        sll $s4, $s4, 2 # size / 4 to get actual size

        whileBothNotEmpty:
            beq $t0, $s1, whileRightNotEmpty # if left == middle, empty right items
            beq $t1, $s2, whileLeftNotEmpty # if right == end, empty left items

            lw $t3, ($t0)
            lw $t4, ($t1)

            # compare left value
            leftSmaller:
                bgt $t3, $t4, rightSmaller
                sw $t3, ($t2) # store left value in merged array
                addi $t2, $t2, 4 # merged array pointer++
                addi $t0, $t0, 4 # left++
            
            # compare right value
            rightSmaller:
                sw $t4, ($t2)  # store right value in merged array
                addi $t2, $t2, 4 # merged array pointer++
                addi $t1, $t1, 4 # left++
                
            # set value at current heap position
            # increment left ($t0) or right ($t1) by 1
            # increment heap address ($t2) by 1 

            j whileBothNotEmpty

        whileLeftNotEmpty:
            beq $t0, $s1, replaceArray # if left == middle, return 
            lw $t3, ($t0)
            sw $t3, ($t2)
            addi $t2, $t2, 4 # merged array pointer++
            addi $t0, $t0, 4 # left++

            j whileLeftNotEmpty

        whileRightNotEmpty:
            beq $t1, $s2, replaceArray # if right == end, return 
            lw $t4, ($t1)
            sw $t4, ($t2)
            addi $t2, $t2, 4 # merged array pointer++
            addi $t1, $t1, 4 # right++
            
            j whileRightNotEmpty

        replaceArray:
            li $t3, 0 # offset = 0 
            beq $t3, $s4, returnMerge # if offset == size: return

            move $t4, $s2 # heap array 
            add $t4, $t4, $t3 # offset to heap address 
            move $t5, $s0 # array
            add $t5, $t5, $t3 # offset to array

            lw $t6, ($t4) # load value from merge array
            sw $t6, ($t5) # store value to original array

            add $t3, $t3, 4 # offset++

        returnMerge:
            jr $ra

    # array pointer
    # array end?
    # add to .data sqrt of size? Or pass to function?
    timSort:
        # fin k
        # check wheter dimension is good 
        # if dimension is log(n), do an insertionSort
        # else split in two, and merge
