.data
    
.text
    blez $t0, else # Test x <= 0
        addi $t0, $s1, 5 # Add 5 to x if x > 0
        j endIf # Don't execute else part
    else: 
        addi $t0, $s1, 10 # Add 10 to x if x <= 0
    endIf:

