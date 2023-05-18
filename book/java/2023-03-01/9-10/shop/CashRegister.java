package shop;

public class CashRegister {
    private double purchase, payment;
    private String history;

    public CashRegister() {
        purchase = 0;
        payment = 0;
        history = "";
    }

    public void recordPurchase(double price) {
        purchase += price;
        history += price + " ";
    }

    public void receivePayment(double payment) {
        this.payment += payment;
    }

    public double giveChange() {
        var change = payment - purchase;
        payment = 0;
        purchase = 0;
        return change;
    }

    public void printReceipt() {
        System.out.println(history);
        System.out.println("Total: " + purchase);
    }
}
