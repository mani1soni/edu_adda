package java_OOP;

public class Fish extends Animal{
    private WaterType waterType;
    private double deepness;

    public Fish(final Habitat habitat, final int averageLifetime, final Type typeOfFood,
                final WaterType waterType, final double deepness) {
        super(habitat, averageLifetime, typeOfFood);
        this.waterType = waterType;
        this.deepness = deepness;
    }

    public WaterType getWaterType() {
        return waterType;
    }

    public void setWaterType(final WaterType waterType) {
        this.waterType = waterType;
    }

    public double getDeepness() {
        return deepness;
    }

    public void setDeepness(final double deepness) {
        this.deepness = deepness;
    }
}
