import shop.CashRegister;
import shop.Register;

class Main {
    public static void main(String[] args) {

        var register = new CashRegister();
        register.recordPurchase(120.50);
        register.recordPurchase(180.50);
        register.recordPurchase(590.70);
        register.recordPurchase(9.50);

        register.printReceipt();

        register.receivePayment(1000);
        System.out.println("Change " + register.giveChange());

        var reg = new Register();
        reg.recordPurchase(120.50);
        reg.recordPurchase(180.50);
        reg.recordPurchase(590.70);
        reg.recordPurchase(9.50);

        reg.printReceipt();

        reg.receivePayment(1000);
        System.out.println("Change " + reg.giveChange());

        System.out.println(reg.getSalesCount());
        System.out.println(reg.getSalesTotal());

        reg.recordPurchase(120.50);
        reg.recordPurchase(180.50);
        reg.recordPurchase(590.70);
        reg.recordPurchase(9.50);

        reg.printReceipt();

        reg.receivePayment(1000);
        System.out.println("Change " + reg.giveChange());

        System.out.println(reg.getSalesCount());
        System.out.println(reg.getSalesTotal());
    }
}
