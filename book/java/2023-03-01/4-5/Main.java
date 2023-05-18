import circuit.Circuit;

class Main {
    public static void main(String[] args) {

        var cir = new Circuit();

        cir.toggleFirstSwitch();
        System.out.println(cir.getFirstSwitchState());
        System.out.println(cir.getLampState());

        System.out.println();

        cir.toggleSecondSwitch();
        System.out.println(cir.getSecondSwitchState());
        System.out.println(cir.getLampState());

        System.out.println();

        cir.toggleFirstSwitch();
        System.out.println(cir.getFirstSwitchState());
        System.out.println(cir.getSecondSwitchState());
        System.out.println(cir.getLampState());
    }
}
