.globl main

.data
	M: .word 0, 6, 7, 8, 8, 8, 6
	N: .word 7
.text
	main:
		la $a0, M
		lw $a1, N
		jal sommaContaUgualiPrec	
	
		# print sum
		move $a0, $v0
		li $v0, 1
		syscall
		
		# print new line
		li $a0, '\n'
		li $v0, 11
		syscall
		
		# print count
		move $a0, $v1
		li $v0, 1
		syscall
	
		# return 0
		li $v0, 17
		li $a0, 0
		syscall
		
	sommaContaUgualiPrec:
		subi $sp, $sp, 4
		sw $ra, ($sp)
		
		subi $a2, $a1, 1
		jal sommaContaUgualiPrecRec
		
		lw $ra, ($sp)
		addi $sp, $sp, 4
		
		jr $ra

	sommaContaUgualiPrecRec:
		# a0 array address
		# a1 array size
		# a2 current index
			
		beq $a2, 0, baseCase # if current index is 0, there is no previous element, so return
		
		# initialize values to 0
		li $v0, 0
		li $v1, 0
		
		sll $t0, $a2, 2 # t0 = index * 4 (we are using words)
		add $t0, $t0, $a0 # current address = base address + index * 4
		lw $t0, ($t0) # current value = mem[current address]
		
		subi $t1, $a2, 1 # t1 = previous index = current index - 1
		sll $t1, $t1, 2 # previous index * 4 (we are using words)
		add $t1, $t1, $a0 # previous address = base address + previous index * 4
		lw $t1, ($t1) # previous value = mem[previous value]
		
		bne $t0, $t1, next # if the current value != previous value, go to next element
		
		# else add up and count
		add $v0, $v0, $t0 # sum up value
		addi $v1, $v1, 1 # count += 1
		
		next:
		
		subi $sp, $sp, 12 # I need to store just the current calculated value
		sw $ra, 8($sp)
		sw $v1, 4($sp)
		sw $v0, ($sp)
		
		subi $a2, $a2, 1 # a2 = index - 1
		jal sommaContaUgualiPrecRec
		
		lw $ra, 8($sp)
		lw $t1, 4($sp) # load count 
		lw $t0, ($sp) # load sum
		addi $sp, $sp, 12 # I need to store just the current calculated value
		
		add $v0, $t0, $v0 # v0 = current sum + calculated sum
		add $v1, $t1, $v1 # v1 = current count + calculated count
		
		jr $ra
		
		baseCase:
			# Already out of array, so return (0, 0)
			li $v0, 0
			li $v1, 0 
			jr $ra
		
		# v0 sum of elements with value equal to previous
		# v1 count of elements with value equal to previous
