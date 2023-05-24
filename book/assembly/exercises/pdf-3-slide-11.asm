.data
    variable: 10
    vector: .word 12, 4, 59, 9, 19, 8, 6, 18, 9, 19, 28, 12, 100

.text
    la $s6, variable # s6 = address of variable
    la $s5, vector # s5 = address of vector

    # vector[12] = vector[6] + variable

    lw $t0, ($s6) # t0 = *s6 (value at address s6, which is the value of the variable)
    lw $t1, 24($s5) # t1 = s5[6] ; s5[6] = *(s5 + 6), but 6 rappresents words, not bytes, so 6 * 4 = 24 (which corresponds to vector[6])

    add $t0, $t0, $t1 # t0 += t1 (which is vector[5])

    sw $t0, 48($s5) # stores result of sum (from t0) to vector[12], but 12 is words, so 48 is bytes
