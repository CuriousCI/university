# Algorithms & Data Structures I

Implementations and exercises for [Algo I 2022/2023](https://twiki.di.uniroma1.it/twiki/view/Intro\_algo/AD/WebHome) 
course at Sapienza Universita' di Roma _(Computer Science Bachelor's degree)_ in Rust 🦀, cos it's more fun!

## Table of contents

The content in the checked boxes was summarized / implemented / completed.
If you need explanations on some content, just open an issue, and I'll be happy to help 😄.

_(Completed in Rust 56 out of 149 ~ 38%)_

1. [ ] [Introduction](https://twiki.di.uniroma1.it/pub/Intro\_algo/AD/Dispense/01\_Introduzione\_2023.pdf) 
2. [ ] [Big O notation](https://twiki.di.uniroma1.it/pub/Intro\_algo/AD/Dispense/02\_Notazione\_asintotica\_2023.pdf)
    1. [ ] [Big O]()
    2. [ ] [Omega]()
    3. [ ] [Teta]()
    4. [ ] [Formulas]()
    5. [ ] [Ex 1]()
    6. [ ] [Ex 2]()
3. [ ] [Cost](https://twiki.di.uniroma1.it/pub/Intro\_algo/AD/Dispense/03\_Costo\_computazionale2023.pdf)
    1. [ ] [Formulas]()
    2. [ ] [Ex 1]()
    3. [ ] [Ex 2]()
    4. [ ] [Ex 3]()
4. [x] [Searching Algorithms](https://twiki.di.uniroma1.it/pub/Intro\_algo/AD/Dispense/04\_Ricerca2023.pdf)
    1. [x] [Linear Search](./src/algorithms/search.rs)
    2. [x] [Binary Search](./src/algorithms/search.rs) _(iterative)_
    3. [x] [Ex 1](./src/algorithms/search.rs) _(TODO: test again)_
5. [x] [Recursion](https://twiki.di.uniroma1.it/pub/Intro\_algo/AD/Dispense/05\_Ricorsione2023.pdf)
    1. [x] [Ex 1](./src/algorithms/recursion.rs)
    2. [x] [Ex 2](./src/algorithms/recursion.rs)
    3. [x] [Ex 3](./src/algorithms/recursion.rs)
    4. [ ] [Ex 4](./src/algorithms/recursion.rs)
    5. [x] [Ex 5](./src/algorithms/recursion.rs)
    6. [x] [Ex 6](./src/algorithms/recursion.rs)
    7. [ ] [Ex 7](./src/algorithms/recursion.rs) _(Hanoi)_
    8. [x] [Linear Search](./src/algorithms/recursion.rs)
    9. [x] [Binary Search](./src/algorithms/recursion.rs)
    10. [x] [Factorial](./src/algorithms/recursion.rs)
    11. [x] [Fibonacci](./src/algorithms/recursion.rs)
    12. [ ] [Binomial](./src/algorithms/recursion.rs)
    13. [x] [GCD](./src/algorithms/recursion.rs)
6. [ ] [Let's just not... pt.1](https://twiki.di.uniroma1.it/pub/Intro\_algo/AD/Dispense/06\_EquazioniRicorrenza2023.pdf)
    1. [ ] [Iterative]()
    2. [ ] [Substitution]()
    3. [ ] [Tree]()
    4. [ ] [Main]()
7. [ ] [Let's just not... pt.2](https://twiki.di.uniroma1.it/pub/Intro\_algo/AD/Dispense/06\_EquazioniRicorrenza2023.pdf)
8. [x] [Naive Sorting](https://twiki.di.uniroma1.it/pub/Intro\_algo/AD/Dispense/08\_Ordinamento1\_2023.pdf)
    1. [x] [Insertion Sort](./src/algorithms/naive.rs)
    2. [x] [Selection Sort](./src/algorithms/naive.rs)
    3. [x] [Bubble Sort](./src/algorithms/naive.rs)
    4. [x] [Ex 1](./src/algorithms/naive.rs)
    5. [x] [Ex 2](./src/algorithms/naive.rs)
9. [x] [Merge Sort](https://twiki.di.uniroma1.it/pub/Intro\_algo/AD/Dispense/09\_Ordinamento2\_2023.pdf)
    1. [x] [Merge](./src/algorithms/merge.rs)
    2. [x] [Merge Sort](./src/algorithms/merge.rs)
    3. [x] [Ex 1](./src/algorithms/merge.rs)
    4. [x] [Ex 2](./src/algorithms/merge.rs)
    5. [ ] [Ex 3](./src/algorithms/merge.rs)
    6. [ ] [Ex 4](./src/algorithms/merge.rs)
    7. [ ] [Ex 5](./src/algorithms/merge.rs)
10. [x] [Quick Sort](https://twiki.di.uniroma1.it/pub/Intro\_algo/AD/Dispense/10\_Ordinamento3\_2023.pdf)
    1. [x] [Quick Sort](./src/algorithms/quick.rs)
    2. [x] [Ex 1](./src/algorithms/quick.rs)
    3. [x] [Ex 2](./src/algorithms/quick.rs)
11. [x] [Heap Sort](https://twiki.di.uniroma1.it/pub/Intro\_algo/AD/Dispense/11\_Ordinamento4\_2023.pdf)
    1. [x] [Heap](./src/algorithms/heap.rs)
    2. [x] [Ex 1](./src/algorithms/heap.rs)
    3. [x] [Ex 2](./src/algorithms/heap.rs)
    4. [x] [Ex 3](./src/algorithms/heap.rs)
12. [x] [Linear Sorting](https://twiki.di.uniroma1.it/pub/Intro\_algo/AD/Dispense/12\_Ordinamento5\_2023.pdf)
    1. [x] [Counting Sort](./src/algorithms/linear.rs)
    2. [x] [Stable Counting Sort](./src/algorithms/linear.rs)
    3. [ ] [Bucket Sort](./src/algorithms/linear.rs)
    4. [x] [Ex 1](./src/algorithms/linear.rs)
    5. [x] [Ex 2](./src/algorithms/linear.rs)
    6. [x] [Ex 3](./src/algorithms/linear.rs)
13. [ ] [Linked List](https://twiki.di.uniroma1.it/pub/Intro\_algo/AD/Dispense/13\_StruttureDati1\_2023.pdf)
    1. [ ] [Array Operations]()
    2. [ ] [Linked List]()
    3. [ ] [Double Linked List]()
    4. [ ] [Ex 1]()
    5. [ ] [Ex 2]()
    6. [ ] [Ex 3]()
14. [x] [Queue & Stack](https://twiki.di.uniroma1.it/pub/Intro\_algo/AD/Dispense/14\_StruttureDati2\_2023.pdf)
    1. [x] [Queue](./src/algorithms/queue.rs)
    2. [x] [Stack](./src/algorithms/stack.rs)
    3. [ ] [Queue on LinkedList]()
    4. [ ] [Stack on LinkedList]()
    5. [ ] [Priority Queue]()
    6. [x] [Ex 1](./src/algorithms/queue.rs)
    7. [x] [Ex 2](./src/algorithms/stack.rs)
15. [ ] [Linked List exercises ](https://twiki.di.uniroma1.it/pub/Intro\_algo/AD/Dispense/15\_Soluzioni\_esercizi\_liste\_2023.pdf)
    1. [ ] [Ex 1]()
    2. [ ] [Ex 2]()
    3. [ ] [Ex 3]()
    4. [ ] [Ex 4]()
    5. [ ] [Ex 5]()
    6. [ ] [Ex 6]()
    7. [ ] [Ex 7]()
    8. [ ] [Ex 8]()
    9. [ ] [Ex 9]()
    10. [ ] [Ex 10]()
16. [x] [Tree](https://twiki.di.uniroma1.it/pub/Intro\_algo/AD/Dispense/16\_Alberi2023.pdf)
    1. [ ] [Graph Theory]()
    2. [x] [TreeNode](./src/algorithms/tree/tree\_node.rs) _(Tree built with Records)_
    3. [x] [Positional Binary Tree](./src/algorithms/tree/binary\_tree.rs) _(Basically a Heap)_
    4. [x] [ParentTree](./src/algorithms/tree/parent\_tree.rs) _(Tree built with Two Arrays)_
    5. [ ] [Operations](./src/algorithms/tree/operations.rs)
    6. [x] [Ex 1](./src/algorithms/tree/binary\_tree.rs)
    6. [x] [Ex 2](./src/algorithms/tree/parent\_tree.rs)
17. [ ] [DFS/BFS](https://twiki.di.uniroma1.it/pub/Intro\_algo/AD/Dispense/17\_VisiteAlberi\_2023.pdf)
    1. [ ] [Preorder]()
    2. [ ] [Inorder]()
    3. [ ] [Postorder]()
    4. [ ] [Ex 1]()
    5. [ ] [Ex 2]()
    6. [ ] [Ex 3]()
18. [ ] [Dictionary](https://twiki.di.uniroma1.it/pub/Intro\_algo/AD/Dispense/18\_Dizionari1\_2022.pdf)
    1. [ ] [Insert]()
    2. [ ] [Search]()
    3. [ ] [Delete]()
    4. [ ] [Direct Address Table](./src/algorithms/dict/direct\_address.rs) _([GeeksForGeeks](https://www.geeksforgeeks.org/direct-address-table/))_
    5. [ ] [Hash Table](./src/algorithms/dict/hash\_table.rs)
19. [x] [Binary Search Tree](https://twiki.di.uniroma1.it/pub/Intro\_algo/AD/Dispense/19\_Dizionari2\_2022.pdf)
    1. [x] [Binary Search Tree](./src/algorithms/dict/binary\_search\_tree.rs)
    2. [x] [Min](./src/algorithms/dict/binary\_search\_tree.rs)
    3. [x] [Max](./src/algorithms/dict/binary\_search\_tree.rs)
    4. [x] [Operations](./src/algorithms/dict/binary\_search\_tree.rs)
    5. [ ] [Ex 1]()
    6. [ ] [Ex 2]()
    7. [ ] [Ex 3]()
    8. [ ] [Ex 4]()
20. [ ] [Black-Red Tree](https://twiki.di.uniroma1.it/pub/Intro\_algo/AD/Dispense/20\_Dizionari3\_2022.pdf)
    1. [ ] [Rotate]()
    2. [ ] [Insert]()
    3. [ ] [Delete]()
    4. [ ] [Ex 1]()
21. [ ] [Exercises pt.1](https://twiki.di.uniroma1.it/pub/Intro\_algo/AD/Dispense/21\_EserciziVari1\_2022.pdf)
    1. [ ] [Ex 1]()
    2. [ ] [Ex 2]()
    3. [ ] [Ex 3]()
    4. [ ] [Ex 4]()
    5. [ ] [Ex 5]()
    6. [ ] [Ex 6]()
    7. [ ] [Ex 7]()
    8. [ ] [Ex 8]()
22. [ ] [Exercises pt.2](https://twiki.di.uniroma1.it/pub/Intro\_algo/AD/Dispense/22\_EserciziVari2\_2022.pdf)
    1. [ ] [Ex 1]()
    2. [ ] [Ex 2]()
    3. [ ] [Ex 3]()
    4. [ ] [Ex 4]()
    5. [ ] [Ex 5]()
    6. [ ] [Ex 6]()
23. [ ] [Exercises pt.3](https://twiki.di.uniroma1.it/pub/Intro\_algo/AD/Dispense/infgen.pdf)
24. [ ] [Other]()
    1. [ ] [Tim Sort]()
    2. [ ] [Has Duplicates in Merge Sort]()
    3. [ ] [Merge Sort on Linked List]() _(iterative)_
    4. [ ] [Python List]() _(TODO: look info about it's implementation)_
25. [Pytohn Utils](https://twiki.di.uniroma1.it/pub/Intro\_algo/AD/Dispense/METODI\_UTILI\_IN\_PYTHON.pdf