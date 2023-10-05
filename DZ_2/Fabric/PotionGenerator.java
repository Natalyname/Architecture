package Fabric;

import Interface.iGameItem;
import Product.PotionReward;

public class PotionGenerator extends ItemGenerator {
    @Override
    public iGameItem createItem() {
        return new PotionReward();
    }
}
