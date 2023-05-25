package algorithms.struct;

import java.util.Optional;

public class ArrayStack<T> {
    Object[] stack;
    Integer top;

    public ArrayStack(Integer size) {
        stack = new Object[size];
        top = 0;
    }

    public Boolean isFull() {
        return top == stack.length - 1;
    }

    public void push(T value) throws IndexOutOfBoundsException {
        if (isFull())
            throw new IndexOutOfBoundsException();

        stack[top] = value;
        top++;
    }

    public Optional<Object> pop() {
        if (top == 0)
            return Optional.empty();

        var result = stack[top];
        top--;
        return Optional.of(result);
    }
}
//
// @Override
// public String toString() {
// var result = "";
//
// for (var value : stack)
// result += value + " ";
//
// return result;
// }
