package Models;

public class Bus {

    private final int id;
    private String gosNumber;
    private final int placesCap;
    private boolean isReady;

    public Bus(int id, int placesCap) {
        this.id = id;
        this.placesCap = placesCap;
    }

    public void setGosNumber(String gosNumber) {
        this.gosNumber = gosNumber;
    }

    public void setReady(boolean ready) {
        isReady = ready;
    }

    public String getGosNumber() {
        return gosNumber;
    }

    public int getId() {
        return id;
    }

    public int getPlacesCap() {
        return placesCap;
    }

    public boolean getReady() {
        return isReady;
    }

}
