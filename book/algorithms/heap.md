# Heap Sort

## Heap

To code a `heap_sort` function, we need to implement the `heap` data structure on an array.

```rust
{{#include ./src/algorithms/heap.rs:3:6}}
```

Looks simple enough... now we need a way to create a heap _(ideally from a boxed slice)_ or just create an empty one in which to insert values later.


```rust
{{#include ./src/algorithms/heap.rs:8:18}}
```

We'll look into the specification of the `Heap::build` method later, to see what does it do, and why it requires `Copy` and `Ord` traits.

```rust
{{#include ./src/algorithms/heap.rs:20:27}}
```

## Heap Methods 

`heapify` is the most important method to make a heap work: it basically rearranges in \\(O(\log{n})\\) a `Heap` in which **only the root is out of order**.

```rust
#impl<T: Ord + Copy> Heap<T> {
{{#include ./src/algorithms/heap.rs:34:43}}
#}
```

Now that we have the `heapify` method, to `build` the `Heap`, we just need to run `heapify` on the left side of the array.

```rust
#impl<T: Ord + Copy> Heap<T> {
{{#include ./src/algorithms/heap.rs:30:32}}
#}
```

## Indexing a Heap 

In a `Heap`, to get the children of a node at an index `i`, we just need a formula:
- `i * 2 + 1` for the left child
- `i * 2 + 2` for the right child

Knowing this, we can write a `child` method to get the children of a node in a `Heap`, and reuse it in the `heapify` method.

```rust
#impl<T: Ord + Copy> Heap<T> {
{{#include ./src/algorithms/heap.rs:45:53}}
#}
```

## Iterating a Heap

Now that we have the `Heap` setup, we just need to implement the `Iterator` trait to consume the Heap. The `next` method is very simple: we just swap the last element with the root _(in position 0)_, reduce the size of the `Heap`, and run `heapify` again.

```rust
{{#include ./src/algorithms/heap.rs:56:70}}
```

## Heap Sort

Now sorting a `Heap` becomes a very easy task! We just have to run `heapify` until the there are no more elements, and the unerlying buffer will be sorted.

```rust
{{#include ./src/algorithms/heap.rs:72:74}}
```

## Exercises

```rust
{{#include ./src/algorithms/heap.rs:77:139}}
```
