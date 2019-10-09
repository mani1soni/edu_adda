package java_OOP;

public abstract class Animal {
    private Habitat habitat;
    private int averageLifetime;
    private Type typeOfFood;

    public Animal(final Habitat habitat, final int averageLifetime, final Type typeOfFood) {
        this.habitat = habitat;
        this.averageLifetime = averageLifetime;
        this.typeOfFood = typeOfFood;
    }

    public Habitat getHabitat() {
        return habitat;
    }

    public void setHabitat(final Habitat habitat) {
        this.habitat = habitat;
    }

    public int getAverageLifetime() {
        return averageLifetime;
    }

    public void setAverageLifetime(final int averageLifetime) {
        this.averageLifetime = averageLifetime;
    }

    public Type getTypeOfFood() {
        return typeOfFood;
    }

    public void setTypeOfFood(final Type typeOfFood) {
        this.typeOfFood = typeOfFood;
    }
}
