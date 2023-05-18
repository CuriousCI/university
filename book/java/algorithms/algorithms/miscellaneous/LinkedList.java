package algorithms.miscellaneous;

import java.util.Optional;

public class LinkedList<T> {
    public final T value;
    public Optional<LinkedList> next;

    public LinkedList(T value, Optional<LinkedList<T>> next) {
        this.value = value;
        this.next = next;
    }
}
