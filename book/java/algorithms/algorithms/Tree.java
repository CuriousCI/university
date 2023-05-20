
package algorithms;

import java.util.Optional;

public class Tree<T> {
    public T value;
    public Optional<Tree<T>> left = Optional.empty(),
            right = Optional.empty();

    public Tree(T value) {
        this.value = value;
    }

    public Tree(T value, Tree<T> left) {
        this(value);
        this.left = Optional.of(left);
    }

    public Tree(T value, Tree<T> left, Tree<T> right) {
        this(value, left);
        this.right = Optional.of(right);
    }

}
