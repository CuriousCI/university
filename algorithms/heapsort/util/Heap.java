package util;

import java.util.List;

public class Heap<T extends Comparable<T>> {
    List<T> heap;
    Integer heapSize;

    public Heap(List<T> list) {
        heap = list;
        heapSize = list.size();
    }

    Integer left(Integer index) throws IndexOutOfBoundsException {
        var left = (2 * index) + 1;

        if (left >= heapSize)
            throw new IndexOutOfBoundsException();

        return left;
    }

    Integer right(Integer index) throws IndexOutOfBoundsException {
        var right = (2 * index) + 2;

        if (right >= heapSize)
            throw new IndexOutOfBoundsException();

        return right;
    }

    Integer parent(Integer index) throws IndexOutOfBoundsException {
        var praent = (int) Math.floor((index - 1) / 2);

        return praent;
    }

    public void heapify() {

    }
}
