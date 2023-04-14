import static java.util.Arrays.asList;

import util.Heap;

class Main {
    public static void main(String[] args) {
        // var list1 = asList(new Integer[] { 10, 22, 12, 4901, 9801, 2901, 901, 1980,
        // 9100, 9058879, 28, 2980, -12980,
        // -2980, 2, -1 });
        //
        // var heap = new Heap<Integer>(list1);
        // heapSort(heap);

        // for (var item : list1)
        // System.out.printf("%s ", item);

        var list = asList(new Item[] {
                new Item(2, 0),
                new Item(12, 0),
                new Item(2, 1),
                new Item(-3, 0),
                new Item(-30, 0),
                new Item(1, 0),
                new Item(12, 1),
        });

        heapSort(new Heap<Item>(list));

        for (var item : list)
            System.out.println(item);

    }

    public static <T extends Comparable<? super T>> void heapSort(Heap<T> heap) {
        while (heap.hasItems())
            heap.pop();
    }
}

class Item implements Comparable<Item> {
    Integer first, second;

    Item(Integer first, Integer second) {
        this.first = first;
        this.second = second;
    }

    @Override
    public int compareTo(Item item) {
        return first.compareTo(item.first);
    }

    @Override
    public String toString() {
        return String.format("first: %d - second: %d", first, second);
    }
}
