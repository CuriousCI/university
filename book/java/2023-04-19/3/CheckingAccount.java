public class CheckingAccount extends BankAccount {
    int overdrafts;
    int withdrawals;

    public CheckingAccount(double balance) {
        super(balance);
        overdrafts = 0;
        withdrawals = 0;
    }

    @Override
    public void withdraw(double amount) {
        if (amount > getBalance()) {
            amount += 20;
            if (overdrafts > 1)
                amount += 10;
            overdrafts++;
        }

        if (withdrawals > 3)
            amount++;

        super.withdraw(amount);
        withdrawals++;
    }
}
