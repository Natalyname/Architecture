import Fabric.GemGenerator;
import Fabric.GoldGenerator;
import Fabric.ItemGenerator;

import java.util.List;
import java.util.Random;
import java.util.concurrent.ThreadLocalRandom;

/*
 * Alter2 -> Альтернативное выполнение 2
 * (вариант, который хотел реализовать на семинаре)
 * Основано на счетчиках -> не отдаем редкую добычу,
 *                          пока не сработал соответствующий счетчик
 * */
public class Alter2 {
    public static void main(String[] args) {

        // Рандомайзер
        Random random = ThreadLocalRandom.current();

        // Инициализация фабрик и их списка из метода в классе Main
        List<ItemGenerator> fabrics = Main.initFabrics();

        // Счетчик ходов -> сколько будем задерживать выпадение
        int holdGem = 0;
        int holdGold = 0;

        for (int i = 0; i < 200; i++) {
            holdGem++;
            holdGold++;
            ItemGenerator reward = fabrics.get(random.nextInt(8));
            if (!(reward instanceof GemGenerator) && !(reward instanceof GoldGenerator)) {
                reward.openReward();
            } else if (reward instanceof GemGenerator && holdGem > 64) {
                reward.openReward();
                holdGem = 0;
            } else if (reward instanceof GoldGenerator && holdGold > 21) {
                reward.openReward();
                holdGold = 0;
            }
        }
    }
}
