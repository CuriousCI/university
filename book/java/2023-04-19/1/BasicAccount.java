public class BasicAccount extends BankAccount {
    public BasicAccount(double balance) {
        super(balance);
    }

    @Override
    public void withdraw(double amount) throws IllegalAccessError {
        if (amount > getBalance())
            throw new IllegalAccessError("There isn't enough money");

        super.withdraw(amount);
    }
}
