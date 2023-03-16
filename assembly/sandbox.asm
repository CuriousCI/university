.data
    bytes: .byte 1, 2, 9, 8, 7, 3
    text: .asciiz "Sopra la panca, la capra campa"
    words: .word 0:100
.text
   li $v0, 4 # print
   la $a0, text
   syscall
    
