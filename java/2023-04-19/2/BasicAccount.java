public class BasicAccount extends BankAccount {
    public BasicAccount(double balance) {
        super(balance);
    }

    @Override
    public void withdraw(double amount) {
        if (amount > getBalance())
            amount += 30;

        super.withdraw(amount);
    }

}
