.globl main

.data
	M: .half 0, 1, 2, 3, 4, 5, 6, 7, 8
	N: .word 3

.text
	main:
		la $a0, M # a0 = matrix address
		la $a1, N # a0 = matrix side address
		lw $a1, ($a1) # a1 = matrix side
		jal sommaScacchiera
		
		# print even
		move $a0, $v0
		li $v0, 1
		syscall
		
		# print odd
		move $a0, $v1
		li $v0, 1
		syscall
	
		# return 0
		li $v0, 17
		li $a0, 0
		syscall
		
	# I'll implement the laziest solution by iterating over all rows and columns
	# (there is a way to use at least half the instructions but I'm not sure I have enough time to implement it)
		
	sommaScacchiera:
		# a0 base address of matrix
		# a1 matrix side
		
		# Initialize registers for results
		li $v0, 0 # even-even sum
		li $v1, 0 # odd-odd sum
		
		# It's convenient to iterate by index
		li $t7, 0 # current row offset
		
		li $t0, 0 # row index = 0
		forRows:
			beq $t0, $a1, endRowsFor # if row == side, break
			
			li $t1, 0 # col index = 0
			forCols:
				beq $t1, $a1, endColsFor # if column == side, go to next row
				
				andi $t2, $t0, 1 # t2 = row oddity
				andi $t3, $t1, 1 # t3 = col oddity
				
				bnez $t2, ifRowOdd # if the row is odd check if the col isOdd, else check if it's even
				ifRowEven:
					bnez $t3, endIf # row is even, col is odd, don't sum
					
					# get actual address
					sll $t6, $t1, 1 # column offset = 2 * column index (due to half word)
					add $t6, $t7, $t6 # position = row offset + column offset
					add $t6, $a0, $t6 # address = matrix base address + position
					
					lh $t6, ($t6) # load value from matrix
					
					add $v0, $v0, $t6 # add value 
				ifRowOdd:
					beqz $t3, endIf # row is odd, col is even, don't sum
					
					# get actual address
					sll $t6, $t1, 1 # column offset = 2 * column index (due to half word)
					add $t6, $t7, $t6 # position = row offset + column offset
					add $t6, $a0, $t6 # address = matrix base address + position
					
					lh $t6, ($t6) # load value from matrix
					
					add $v1, $v1, $t6 # add value 
				endIf:
				
				addi $t1, $t1, 1 # column += 1
				j forCols # repeat cycle for next col
			endColsFor:
			
			addi $t0, $t0, 1 # row += 1
			sll $t6, $a1, 1 # t7: bytes in row = side * 2 (because we are using half words)
			add $t7, $t7, $t6 # row offset += bytes in row 
			# (basically, we add all the bytes in the visited row, to get the start address of the next one)
			
			j forRows # repeat cycle for next row
		endRowsFor:
		
		jr $ra # return (v0, v1) 
		# (v0: sum of elements in even row and even col, v1: sum of elements with odd row and odd coll)