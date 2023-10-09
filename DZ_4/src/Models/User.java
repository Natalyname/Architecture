package Models;

import java.util.ArrayList;
import java.util.List;
import java.util.Objects;

/**
 * Модель пользователя
 */
public class User {

    private int id;
    private String userName;
    private int hashPassword;
    private int phone;
    private List<String> benefits;
    private long cardNumber;

    public User(int id, String userName, int hashPassword, int phone, long cardNumber) {
        this.id = id;
        this.userName = userName;
        this.hashPassword = hashPassword;
        this.phone = phone;
        benefits = new ArrayList<>();
        this.cardNumber = cardNumber;
    }


    @Override
    public String toString() {
        return "Client { " +
                "id= " + id +
                ", userName= " + userName +
                ", cardNumber= " + (String.format("%016d", cardNumber)) +
                " }";
    }

    @Override
    public boolean equals(Object o) {
        if (o == null || this.getClass() != o.getClass()) return false;
        User client = (User) o;
        return this.equals(client);
    }


    public boolean equals(User client) {
        return id == client.id && hashPassword == client.hashPassword && cardNumber == client.cardNumber && userName.equals(client.userName);
    }

    @Override
    public int hashCode() {
        return Objects.hash(id, userName, hashPassword, cardNumber);
    }

    public int getHashPassword() {
        return hashPassword;
    }

    public String getUserName() {
        return userName;
    }

    public int getId() {
        return id;
    }

    public long getCardNumber() {
        return cardNumber;
    }
}
