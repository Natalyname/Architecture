package Models;

/**
 * Модель банковского аккаунта
 */
public class BankAccount {

    private long card;
    private int balance;
    private static long oldCard;

    public BankAccount() {
        this.card = oldCard + 1;
        balance = 1000;
        oldCard = this.card;
    }

    @Override
    public String toString() {
        return "BankAccount {" +
                " card= " + (String.format("%016d", card)) +
                ", balance= " + balance +
                " }";
    }

    public long getCard() {
        return card;
    }

    public int getBalance() {
        return balance;
    }

    public void setBalance(int i) {
        this.balance = i;
    }
}
