package shop;

public class Register {
    private double purchase, payment, salesTotal;
    private int salesCount;
    private String history;

    public Register() {
        purchase = 0;
        payment = 0;
        salesTotal = 0;
        salesCount = 0;
        history = "";
    }

    public void recordPurchase(double price) {
        purchase += price;
        history += price + " ";
        salesTotal += price;
    }

    public void receivePayment(double payment) {
        this.payment += payment;
    }

    public double giveChange() {
        var change = payment - purchase;
        payment = 0;
        purchase = 0;
        salesTotal += 1;
        return change;
    }

    public void printReceipt() {
        System.out.println(history);
        System.out.println("Total: " + purchase);
    }

    public double getSalesTotal() {
        return salesTotal;
    }

    public int getSalesCount() {
        return salesCount;
    }

    public void reset() {
        salesCount = 0;
        salesTotal = 0;
    }
}
