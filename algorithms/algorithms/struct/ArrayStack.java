package algorithms.struct;

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

    public Object pop() throws IllegalAccessException {
        if (top == 0)
            throw new IllegalAccessException();

        var result = stack[top];
        top--;
        return result;
    }

    @Override
    public String toString() {
        var result = "";

        for (var value : stack)
            result += value + " ";

        return result;
    }
}
