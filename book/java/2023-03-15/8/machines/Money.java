package machines;

public enum Money {
    TWENTYFIVE(.25),
    FIFTY(.50),
    ONE(1),
    FIVE(5),
    TEN(10);

    public final double dollars, pennies;

    private Money(double dollars) {
        this.dollars = dollars;
        this.pennies = dollars * 100;
    }
};
