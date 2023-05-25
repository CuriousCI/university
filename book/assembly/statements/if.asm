.text
    li $t0, 0 #; x = 0

    blez $t0, else #; if x <= 0, goto else

    if:
        addi $t0, $t0, 5 #; add 5 to x if x > 0
        j end #; don't execute else part
    else: 
        addi $t0, $s1, 10 #; add 10 to x if x <= 0
    end:
