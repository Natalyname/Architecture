package Fabric;

import Interface.iGameItem;
import Product.LeatherReward;

public class LeatherGenerator extends ItemGenerator {
    @Override
    public iGameItem createItem() {
        return new LeatherReward();
    }
}
