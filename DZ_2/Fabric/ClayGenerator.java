package Fabric;

import Interface.iGameItem;
import Product.ClayReward;

public class ClayGenerator extends ItemGenerator {
    @Override
    public iGameItem createItem() {
        return new ClayReward();
    }
}
