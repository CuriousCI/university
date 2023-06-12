import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.InputMismatchException;
import java.util.List;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        try {
            Bank bank = new Bank(getFilename());
            Account max = bank.getMaxBalanceAccount();
            double average = bank.getAverageBalance();
            List<Account> negative = bank.getNegativeAccounts();

            System.out.println("The account with the highest balance is " + max);
            System.out.println("The average balance is " + average);
            System.out.println("The accounts with negative balance are:");

            for (Account account : negative) {
                System.out.println("- " + account);
            }
        } catch (FileNotFoundException e) {
            System.err.println("File not found!");
        } catch (InputMismatchException e) {
            System.err.println("Incorrect file format!");
        }
    }

    public static String getFilename() throws InputMismatchException {
        Scanner stdin = new Scanner(System.in);

        System.out.print("Input filename > ");
        String filename = "";

        try {
            filename = stdin.next();
        } finally {
            stdin.close();
        }

        return filename;
    }

}

class Bank {
    private List<Account> accounts;

    public Bank(String filename) throws FileNotFoundException, InputMismatchException {
        this.accounts = new ArrayList<>();

        Scanner file = new Scanner(new File(filename));

        try {

            while (file.hasNextLine()) {
                Scanner line = new Scanner(file.nextLine());

                String accountId = line.next();
                String name = line.next();
                String surname = line.next();
                double balance = line.nextDouble();

                this.accounts.add(new Account(accountId, name, surname, balance));
            }
        } finally {
            file.close();
        }
    }

    public Account getMaxBalanceAccount() {
        double maxBalance = 0;
        Account result = null;

        for (Account account : this.accounts) {
            if (account.getBalance() > maxBalance) {
                maxBalance = account.getBalance();
                result = account;
            }
        }

        return result;
    }

    public double getAverageBalance() {
        double totalBalance = 0;
        double accountsNumber = 0;

        for (Account account : this.accounts) {
            if (account.getBalance() > 0) {
                totalBalance += account.getBalance();
                accountsNumber += 1;
            }
        }

        if (accountsNumber == 0)
            return 0;

        return totalBalance / accountsNumber;
    }

    public List<Account> getNegativeAccounts() {
        List<Account> negativeAccounts = new ArrayList<>();

        for (Account account : this.accounts) {
            if (account.getBalance() < 0) {
                negativeAccounts.add(account);
            }
        }

        return negativeAccounts;
    }
}

class Account {
    private String accountId;
    private String name;
    private String surname;
    private double balance;

    public Account(String accountId, String name, String surname, double balance) {
        this.accountId = accountId;
        this.name = name;
        this.surname = surname;
        this.balance = balance;
    }

    public String getAccountId() {
        return this.accountId;
    }

    public String getName() {
        return this.name;
    }

    public String getSurname() {
        return this.surname;
    }

    public double getBalance() {
        return this.balance;
    }

    @Override
    public String toString() {
        return String.format(
                "account %s, owner %s %s, has %.2f balance",
                this.getAccountId(),
                this.getName(),
                this.getSurname(),
                this.getBalance());
    }
}
