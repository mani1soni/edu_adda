package java_OOP;

public class Bird extends Animal {
    private double wingspan;
    private boolean isMigratory;
    private double maxFlightHeight;

    public Bird(final Habitat habitat,
                final int averageLifetime,
                final Type typeOfFood,
                final double wingspan,
                final boolean isMigratory,
                final double maxFlightHeight) {
        super(habitat, averageLifetime, typeOfFood);
        this.wingspan = wingspan;
        this.isMigratory = isMigratory;
        this.maxFlightHeight = maxFlightHeight;
    }

    public double getWingspan() {
        return wingspan;
    }

    public void setWingspan(final double wingspan) {
        this.wingspan = wingspan;
    }

    public boolean isMigratory() {
        return isMigratory;
    }

    public void setMigratory(final boolean migratory) {
        isMigratory = migratory;
    }

    public double getMaxFlightHeight() {
        return maxFlightHeight;
    }

    public void setMaxFlightHeight(final double maxFlightHeight) {
        this.maxFlightHeight = maxFlightHeight;
    }
}
