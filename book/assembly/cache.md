# Cache

A cache is divided into blocks

| line # | valid | tag | block |
|--|--|--|--|
| multiple blocks can have the same line | to determine wether the data is valid | distinguishes a block from the others | the block of data itself |
| 0 | 0 | 101 | 01001001\_11010010 |
| 1 | 1 | 011 | 11001011\_01001100 |
| 2 | 1 | 111 | 11010010\_11001011 |
| 3 | 0 | 000 | 01001100\_00100110 |
| 4 | 1 | 010 | 00100110\_00100110 |


### Direct Mapping

The following is an exmple of a cache with **4 words**, with **2 lines**

| # | word | byte1 | byte2 | byte3 | byte4 |
|--|:--:|--|--|--|--|
| 0 | 0 | 00000000 | 00000000 | 00000000 | 00000000 |
| 0 | 1 | 00000000 | 00000000 | 00000000 | 00000000 |
| 0 | 2 | 00000000 | 00000000 | 00000000 | 00000000 |
| 0 | 3 | 00000000 | 00000000 | 00000000 | 00000000 |
||
| 1 | 0 | 00000000 | 00000000 | 00000000 | 00000000 |
| 1 | 1 | 00000000 | 00000000 | 00000000 | 00000000 |
| 1 | 2 | 00000000 | 00000000 | 00000000 | 00000000 |
| 1 | 3 | 00000000 | 00000000 | 00000000 | 00000000 |

Now let's see how to determine where to get a word in the cache, based on its value _(with 4 word blocks, in a 2 line cache)_.

| tag | line # | word | byte |
|--|--|--|--|
| 000000000000000000000000000 | 0 | 10 | 01 |


<!-- |--|--|--|--|--|--| -->


## Associativity

## Policies

### Replacement Policy

- **LRU** _(least recently used)_, it requires a bit to determine how old a block is, to decide which one to replace _(the one used less recently)_

## Misses

- **Cold start** misses
