package algorithms.struct;

import java.util.List;

public class Heap<T extends Comparable<? super T>> {
    List<T> heap;
    Integer heapSize;

    public Heap(List<T> list) {
        heap = list;
        heapSize = list.size();

        // Build Heap
        for (var root = heapSize / 2; root >= 0; root--)
            heapify(root);
    }

    Boolean hasLeft(Integer index) {
        return (2 * index) + 1 < heapSize;
    }

    Integer left(Integer index) throws IndexOutOfBoundsException {
        var left = (2 * index) + 1;

        if (left >= heapSize)
            throw new IndexOutOfBoundsException();

        return left;
    }

    Boolean hasRight(Integer index) {
        return (2 * index) + 2 < heapSize;
    }

    Integer right(Integer index) throws IndexOutOfBoundsException {
        var right = (2 * index) + 2;

        if (right >= heapSize)
            throw new IndexOutOfBoundsException();

        return right;
    }

    Boolean hasParent(Integer index) {
        return index < heapSize && index != 0;
    }

    Integer parent(Integer index) throws IndexOutOfBoundsException {
        if (index >= heapSize || index == 0)
            throw new IndexOutOfBoundsException();

        return (int) Math.floor((index - 1) / 2);
    }

    void heapify(Integer index) {
        var root = heap.get(index);

        if (hasLeft(index) && hasRight(index)) {
            T l = heap.get(left(index)), r = heap.get(right(index));
            if (root.compareTo(l) < 0 || root.compareTo(r) < 0)
                if (l.compareTo(r) > 0) {
                    var temp = heap.get(index);
                    heap.set(index, l);
                    heap.set(left(index), temp);

                    heapify(left(index));
                } else {
                    var temp = heap.get(index);
                    heap.set(index, r);
                    heap.set(right(index), temp);

                    heapify(right(index));
                }
        } else if (hasLeft(index)) {
            T l = heap.get(left(index));

            if (root.compareTo(l) < 0) {
                var temp = heap.get(index);
                heap.set(index, l);
                heap.set(left(index), temp);

                heapify(left(index));
            }
        }
    }

    public Boolean hasItems() {
        return heapSize > 0;
    }

    public T pop() {
        var root = heap.get(0);

        heap.set(0, heap.get(heapSize - 1));
        heap.set(heapSize - 1, root);
        heapSize--;
        heapify(0);

        return root;
    }

    @Override
    public String toString() {
        var string = "";
        for (var item : heap)
            string += item.toString() + " ";

        return string;
    }
}
