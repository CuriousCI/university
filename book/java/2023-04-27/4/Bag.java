import java.util.ArrayList;
import java.util.Optional;

public class Bag {
    private class Item {
        final String name;
        Integer quantity;

        Item(String name, Integer quantity) {
            this.name = name;
            this.quantity = quantity;
        }

    }

    ArrayList<Item> groceries = new ArrayList<Item>();

    public void add(String item) {
        Optional<Item> it = groceries.stream().filter(i -> i.name.equals(item)).findAny();
        if (it.isPresent())
            it.get().quantity++;
        else
            groceries.add(new Item(item, 1));
    }

    public int count(String item) {
        Optional<Item> it = groceries
                .stream()
                .filter(i -> i.name.equals(item))
                .findAny();

        return it.isPresent() ? it.get().quantity : 0;
    }
}
