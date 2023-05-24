.data

.text
    li $s0, 1 # u = 1
    li $s1, 0 # v = 0

    # v = u * 256

    sll $s1, $s0, 8 # s1 = s0 * 256

    # which is the first value that breaks?

    #; a word ha 32 bits, multiplying by 256 means shifting by 8 bits
    #; this means that as soon as we have the 25 bit set to 1, the 1 is shifted out of 32
    #; 2^24 = 16777216

    li $s2, 16777216 # 16777215 will work normally
    sll $s0, $s2, 8 # becomes 0


