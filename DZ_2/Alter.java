import Fabric.ItemGenerator;

import java.util.List;
import java.util.Random;
import java.util.concurrent.ThreadLocalRandom;


/*
 * Alter -> Альтернативное выполнение
 * Основано на весе шансов
 * Полный хардкод, почти :)
 * */
public class Alter {
    public static void main(String[] args) {

        // Рандомайзер
        Random random = ThreadLocalRandom.current();

        // Инициализация фабрик и их списка из метода в классе Main
        List<ItemGenerator> fabrics = Main.initFabrics();

        // Знаем, что первая в списке фабрика с редким шансом выпадения,
        // вторая со средним шансом и шесть остальных.
        // Таким образом, шансы: (1*1 gem: 3*1 gold: 10*6 others) -> 1/64, 3/64, 60/64

        for (int i = 0; i < 200; i++) {
            double chance = random.nextDouble();
            if (chance <= 1 / 64f) {
                fabrics.get(0).openReward();
            } else if (chance <= 3 / 64f) {
                fabrics.get(1).openReward();
            } else {
                fabrics.get(random.nextInt(fabrics.size() - 2) + 2).openReward();
            }
        }
    }
}
