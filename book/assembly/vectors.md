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

> TODO: add minimal example code

You can iterate vectors and matrices in two ways:
- **by index**:
    - useful if you need the **index** of each element
    - the increment of the index doesn't depend on the size of the elements
    - you have to convert the index each time, according to the size of the elements
- **by pointer**:
    - you work directly with the address
    - less calculations to do in the cycle
    - you don't have the index of the element
    - the increment depends on the size of the elements
    - you must calculate the index after the last element

## Matrices

If you want a 7 _(rows)_ x 13 _(columns)_ matrix, you need enough space for 91 elements:

```armasm
.data
    matrix: .word 0:91
```

Matrixes are stored in memory like vectors, each row is laid one after the other. To work with **n-sized** matrices, you just lay out one matrix after the other in memory _(you can have a 3-dimensional matrix, for example, where the z coordinate dictates the layer, or the matrix, you are working with)_
