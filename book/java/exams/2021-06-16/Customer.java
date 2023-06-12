public class Customer {
    private double purchasesAmount;

    public Customer() {
        purchasesAmount = 0;
    }

    public void makePurchase(double amount) {
        if (discountReached()) {
            amount -= amount * 0.1;
            purchasesAmount = 0;
        }

        purchasesAmount += amount;
    }

    public boolean discountReached() {
        return purchasesAmount >= 100;
    }
}
