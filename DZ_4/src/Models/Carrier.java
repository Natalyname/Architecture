package Models;

import java.util.ArrayList;
import java.util.List;

/**
 * Модель перевозчика
 */
public class Carrier {

    private int id;
    private long cardNumber;
    private List<Integer> zones;

    public Carrier(int id, long cardNumber) {
        this.id = id;
        zones = new ArrayList<Integer>();
        zones.add(0);
        zones.add(1);
        this.cardNumber = cardNumber;
    }

    public long getCardNumber() {
        return cardNumber;
    }

    public int getId() {
        return id;
    }

}
