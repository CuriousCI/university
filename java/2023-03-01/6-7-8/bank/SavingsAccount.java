package bank;

public class SavingsAccount extends BankAccount {
    double interestRate, balance;

    public SavingsAccount() {
        balance = 0;
    }

    public SavingsAccount(double balance, double interestRate) {
        this.balance = balance;
        this.interestRate = interestRate;
    }

    public void deposit(double value) {
        balance += value;
    }

    public void withdraw(double value) {
        balance -= value;
    }

    public double getBalance() {
        return balance;
    }

    public void addInterest() {
        balance += (balance * interestRate) / 100;
    }
}
