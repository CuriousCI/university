# Vectors & Matrices

## Endianness

The MIPS architecture allows both **big-endian** and **little-endian** byte ordering, but the **little-endian** one is most commonly used. Endianness has to do on how **bytes** are **addressed** in memory, and it's related to how the access of each individual byte is made.

## Vectors 

There are many types of vectors you can handle in MIPS:

```armasm
.data
    byte: .byte 29, 8, 1, 29, 2, -3
    half: .half 10, -4, 20, -8, 22, 12
    word: .word 2, 29012, 29, 5, -12905, -290125

    # decimal 

    float: .float 2.5, -1.2, 21.90, -5.0
    double: .double 2.5, -1.2, 21.90, -5.0

    # strings

    string: .asciiz "Holy Moly, who ate my Canoli?"

```

Note that `.asciiz` stands for _"zero terminated string"_, which means it has a `'\0'` nullchar at the end.

## Vector Iterations 


You can iterate vectors and matrices in two ways:

### Index

- useful if you need the **index** of each element
- the increment of the index doesn't depend on the size of the elements
- you have to convert the index each time, according to the size of the elements

```armasm
.data
    vector: .word 10, 2, 980, 29, 1992, -2, 59, 280, 99
    size: .word 9
.text
    la $s0, vector #; s0 = vector address
    la $t1, size #; t1 = address of size
    lw $t1, ($t1) #; t1 = size

    li $t0, 0 #; t0 is the index i

    for:
        bge $t0, $t1, end #; if i == size, end loop

        sll $t2, $t0, 2 #; offset = i * 4 (shift logic left by 2)
        addi $t2, $t2, $s0 #; t2 = current address = offset + address

        lw $t7, ($t2) #; load value from current address, and maybe use it

        #; rest of the code ...

        addi $t0, $t0, 1 #; i = i + 1
        j for #; loop again
    end:
```

> TODO: check if it works 


### Pointer

- you work directly with the address
- less calculations to do in the cycle
- you don't have the index of the element
- the increment depends on the size of the elements
- you must calculate the index after the last element

```armasm
.data
    vector: .word 10, 2, 980, 29, 1992, -2, 59, 280, 99
    size: .word 9
.text
    la $t0, vector #; t0 = vector address

    la $t1, size #; t1 = address of size
    lw $t1, ($t1) #; t1 = size
    sll $t1, $t1, 2 #; size = size * 4 (we are handling words)
    add $t1, $t0, $t1 #; t1 = end address = vector address + size * 4 (this is the address after the last one in the vector)

    for:
        bge $t0, $t1, end #; if current address == vector end address, end loop

        lw $t7, ($t0) #; load value from current address, and maybe use it

        #; rest of the code ...

        addi $t0, $t0, 4 #; current address = current address + 4 (we move by 4 bytes, because we are using words) 
        j for #; loop again
    end:
```

> TODO: check if it works

## Matrices

If you want a 7 _(rows)_ x 13 _(columns)_ matrix, you need enough space for 91 elements:

```armasm
.data
    matrix: .word 0:91
```

Matrixes are stored in memory like vectors, each row is laid one after the other. To work with **n-sized** matrices, you just lay out one matrix after the other in memory _(you can have a 3-dimensional matrix, for example, where the z coordinate dictates the layer, or the matrix, you are working with)_
