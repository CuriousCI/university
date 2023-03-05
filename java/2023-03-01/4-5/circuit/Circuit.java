package circuit;

public class Circuit {
    boolean firstSwitch = false,
            secondSwitch = false,
            lampState = false;

    public boolean getFirstSwitchState() {
        return firstSwitch;
    }

    public boolean getSecondSwitchState() {
        return secondSwitch;
    }

    public boolean getLampState() {
        return lampState;
    }

    public void toggleFirstSwitch() {
        firstSwitch = !firstSwitch;
        lampState = !lampState;
    }

    public void toggleSecondSwitch() {
        secondSwitch = !secondSwitch;
        lampState = !lampState;
    }
}
