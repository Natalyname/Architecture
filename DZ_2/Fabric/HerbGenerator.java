package Fabric;

import Interface.iGameItem;
import Product.HerbReward;

public class HerbGenerator extends ItemGenerator {
    @Override
    public iGameItem createItem() {
        return new HerbReward();
    }
}
