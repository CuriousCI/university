import bank.BankAccount;
import bank.SavingsAccount;

class Main {
    public static void main(String[] args) {
        var account = new BankAccount(1000);
        System.out.println(account.getBalance());

        account.withdraw(500);
        System.out.println(account.getBalance());

        account.withdraw(400);
        System.out.println(account.getBalance());

        var account2 = new BankAccount(1000);
        account2.addInterest(10);
        System.out.println(account2.getBalance());

        var acc3 = new SavingsAccount(1000, 10);
        acc3.addInterest();
        System.out.println(acc3.getBalance());
    }
}
