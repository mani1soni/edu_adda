package java_OOP;

public class Mammal extends Animal {
    private int pawsQuantity;

    public Mammal(final Habitat habitat, final int averageLifetime, final Type typeOfFood, final int pawsQuantity) {
        super(habitat, averageLifetime, typeOfFood);
        this.pawsQuantity = pawsQuantity;
    }

    public int getPawsQuantity() {
        return pawsQuantity;
    }

    public void setPawsQuantity(final int pawsQuantity) {
        this.pawsQuantity = pawsQuantity;
    }
}
