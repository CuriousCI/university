import store.Product;

class Main {
    public static void main(String[] args) {
        var detersivo = new Product("ACE", 30);
        System.out.println(detersivo.getPrice());
        detersivo.reducePrice(5);
        System.out.println(detersivo.getPrice());

    }
}
