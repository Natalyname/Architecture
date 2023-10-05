import Fabric.*;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;
import java.util.concurrent.ThreadLocalRandom;

/*
 * Выполнение
 *
 *
 * */
public class Main {
    public static void main(String[] args) {

        // Рандомайзер
        Random random = ThreadLocalRandom.current();

        // Инициализация фабрик и их списка
        List<ItemGenerator> fabrics = initFabrics();

        // Расчет шансов(веса) выпадения
        Double gemWeight = getWeightsList(fabrics).get(0);
        Double goldWeight = getWeightsList(fabrics).get(1);

        for (int i = 0; i < 200; i++) {
            // Выбрасываем вес шанса (0 <= вес < 1)
            double chance = random.nextDouble();
            // Если шанс меньше, либо равен веса гема, даем гем
            if (chance <= gemWeight) {
                fabrics.get(0).openReward();
                // Если шанс меньше, либо равен веса золота, даем золото
            } else if (chance <= goldWeight) {
                fabrics.get(1).openReward();
                // Иначе даём обычный лут, определяем рандомно (неполучение лута не предусмотрено)
            } else {
                fabrics.get(random.nextInt(fabrics.size() - 2) + 2).openReward();
            }
        }
    }


    /**
     * @return List of generators(fabrics)
     */
    // Фабричный инициализатор
    public static List<ItemGenerator> initFabrics() {
        List<ItemGenerator> fabrics = new ArrayList<>();

        ItemGenerator f1 = new GemGenerator();
        fabrics.add(f1);
        ItemGenerator f2 = new GoldGenerator();
        fabrics.add(f2);
        ItemGenerator f3 = new SilverGenerator();
        fabrics.add(f3);
        ItemGenerator f4 = new ClayGenerator();
        fabrics.add(f4);
        ItemGenerator f5 = new CopperGenerator();
        fabrics.add(f5);
        ItemGenerator f6 = new HerbGenerator();
        fabrics.add(f6);
        ItemGenerator f7 = new LeatherGenerator();
        fabrics.add(f7);
        ItemGenerator f8 = new PotionGenerator();
        fabrics.add(f8);

        return fabrics;
    }


    /**
     * @param fabrics List of generators(fabrics)
     * @return List of weights for [hi, mid, low] chanced items
     * >>> Распределить шансы выпадения (1*gem:3*gold:10*(n*others)) <<<
     */
    private static List<Double> getWeightsList(List<ItemGenerator> fabrics) {
        List<Double> chances = new ArrayList<>();

        // Доля шанса выпадения
        double hiStake = 1;
        double midStake = 3;
        double lowStake = 10;

        // Количество фабрик по шансам выпадения
        double hiStakeFabricsQty = 1;
        double midStakeFabricsQty = 1;
        double lowStakeFabricsQty = fabrics.size() - hiStakeFabricsQty - midStakeFabricsQty;

        // Вес шансов всех фабрик
        double fabricsWeightsOverall = hiStakeFabricsQty * hiStake + midStakeFabricsQty * midStake +
                lowStakeFabricsQty * lowStake;

        // Добавляем вес [hi, mid, low]
        chances.add(hiStake * hiStakeFabricsQty / fabricsWeightsOverall);
        chances.add(midStake * midStakeFabricsQty / fabricsWeightsOverall);
        chances.add(lowStake * lowStakeFabricsQty / fabricsWeightsOverall);

        return chances;
    }


}
