package java_OOP;

public class Main {
    public static void main(String[] args) {
        Bird sparrow = new Bird(Habitat.AIR,
                3,
                Type.VERBIVORE,
                15,
                false,
                65
        );
        Mammal wolf = new Mammal(Habitat.GROUND,
                15,
                Type.PREDATOR,
                4
        );
        Fish tuna = new Fish(Habitat.WATER,
                5,
                Type.OMNIVORE,
                WaterType.SALT,
                100
        );
    }
}
