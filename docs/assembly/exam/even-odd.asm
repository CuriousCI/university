##########################################
# INSERIRE I PROPRI DATI QUI
# Nome:
# Cognome:
# Matricola:
##########################################

# NON MODIFICARE QUESTA PARTE
.data
    buffer: .space 20

.text

main:
    li $v0, 8       # Codice per input stringa
    la $a0, buffer  # Carica indirizzo base in $a0
    li $a1, 20      # Alloca al massimo 20 caratteri
    syscall         # $a0 contiene l'indirizzo base della stringa


##########################################
## INSERIRE IL CODICE QUI
    
    jal count # Call "count" function

    move $v0, $a0 # Set mod2 in out
    li $v0, 1 # Print mod2 count
    syscall

    li $a0, 10 # Move mod4 count to printing
    li $v0, 11 # Print int
    syscall

    move $v1, $a0 # Move mod4 count to printing
    li $v0, 1 # Print int
    syscall

    li $a0, 0 # Exit
    li $v0, 17 # 0
    syscall 


# In $a0 there is an address
# In $v0 return even
# In $v1 return mod4
count: 
    lb $t1, ($a0) # Load char in parameter address
    li $v0, 0 # Set $v0 return to 0
    li $v1, 0 # Set $v1 return to 0

    beqz $t1, return # If byte == '\0': return 

    subi $t1, $t1, '0' # Subtract ascii of "0" to number  
    beqz $t1, next # If number == 0:  return

    mod2: 
        andi $t2, $t1, 1 # Save number & 1 in $t2
        bne $t2, 0, next # If odd: return, it can't be mod4
        addi $v0, $v0, 1 # Add 1 to mod2 counter

    mod4:
        andi $t2, $t1, 1 # Save number & 1 in $t2
        bne $t2, 0, next # If not mod4: return, it can't be mod4
        addi $v1, $v1, 1 # Add 1 to mod4 counter 

    next:
        subi $sp, $sp, 16 # Move stack pointer
        sw $a0, 12($sp) # Save params
        sw $v0, 8($sp) 
        sw $v1, 4($sp) 
        sw $ra, ($sp) # Save $ra

        addi $a0, $a0, 1 # Next char
        jal count # Call itself on next byte

        lw $a0, 12($sp) # Read param
        lw $t0, 8($sp) # Add mod2
        lw $t1, 4($sp) # Add mod4
        lw $ra, ($sp) # Read $ra
        addi $sp, $sp, 16 # Reset stack pointer


        add $v0, $v0, $t0
        add $v1, $v1, $t1

    return:
        jr $ra

# Use two registers for even or odd 
# If byte != \0
#   return
#
# Convert from ascii to int 
#   If > 0
#       If even & 1:    
#           Add even counter
#       If div4 
#           Add div4 counter
# 
# Call function
# Add function result in $v0, $v1
# Return result 
