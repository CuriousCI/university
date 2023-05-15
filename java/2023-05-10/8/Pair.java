public class Pair<T, S> {
    private T first;
    private S second;

    public Pair(T first, S second) {
        this.first = first;
        this.second = second;
    }

    public T getFirst() {
        return first;
    }

    public S getSecond() {
        return second;
    }

    @Override
    public boolean equals(Object otherObject) {
        if (otherObject instanceof Pair<T, S>)
            return false;

        var other = (Pair<T, S>) otherObject;

        return first.equals(otherObject.first) && second.equals(other.second);
    }

    public int hashCode() {
        return first.hashCode();
    }
}
