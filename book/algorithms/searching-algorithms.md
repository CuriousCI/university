# Searching Algorithms

A bunch of searching algorithms on arrays 🔎.

## Linear Search

### Rust

```rust
{{#include ./src/algorithms/search.rs:3:8}}
```

### Java

```java
{{#include ./jdk/algorithms/Search.java:7:13}}
```


## Binary Search

In the course, you will study the **recursive** implementation of the **binary search**, in my code, I've written an iterative one _(I don't "like" recurion)_

### Rust 

```rust
{{#include ./src/algorithms/search.rs:10:34}}
```

### Java

```java
{{#include ./jdk/algorithms/Search.java:15:35}}
```

## Exercise

> Given $A$, an `array of integers`, and two values $a$ and $b$, with $a \le b$, count how many elements of $A$ are included in the range $[a, b]$

The simplest way to solve the problem is to implement two functions: `lower_bound` and `upper_bound`, which are basically binary searches that don't stop once they find the value in the array. In the case of `lower_bound`, it finds the index of _"the smallest value bigger or equal to $x$"_, and the `upper_bound` is _"the biggest value smaller or equal to $x$"_ with $x$ being the value to find.

This way, we can find the `upper_bound` of $b$, and the `lower_bound` of $a$, and do a subtraction of the two to find the number of elements inbetween. There are a few corner cases to consider both for `upper_bound`, `lower_bound` and `count_in_range` _(the function that solves the exercise)_ for which we return 0 _(open an [ISSUE](https://github.com/CuriousCI/university/issues) if you want me to discuss them)_.

### Rust

```rust
{{#include ./src/algorithms/search.rs:36:63}}
```

```rust
{{#include ./src/algorithms/search.rs:65:90}}
```

```rust
{{#include ./src/algorithms/search.rs:98:110}}
```

### Java

> TODO: make bound functions return Optional, handle corner cases

```java
{{#include ./jdk/algorithms/Search.java:37:48}}
```

```java
{{#include ./jdk/algorithms/Search.java:50:61}}
```

> TODO: write a countInRange method
