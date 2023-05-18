package bank;

public class BankAccount {
    double balance;

    public BankAccount() {
        balance = 0;
    }

    public BankAccount(double balance) {
        this.balance = balance;
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

    public void addInterest(double rate) {
        balance += (balance * rate) / 100;
    }

}
