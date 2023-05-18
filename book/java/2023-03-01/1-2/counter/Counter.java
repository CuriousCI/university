package counter;

// import java.lang.Math;

public class Counter {
    private int value;

    public Counter() {
        this.value = 0;
    }

    public void click() {
        value++;
    }

    public void reset() {
        value = 0;
    }

    public void undo() {
        if (value > 0)
            value--;

        // value = Math.max(value - 1, 0);
    }

    public int getValue() {
        return value;
    }
}
