import java.util.LinkedList;
import java.util.Queue;

public class Airport {
    public static void main(String[] args) {

    }
}

class Simulation {
    private Queue<String> takingOff;
    private Queue<String> landing;

    public Simulation() {
        this.takingOff = new LinkedList<String>();
        this.landing = new LinkedList<String>();
    }

    public void takeoff(String flightCode) {
        takingOff.add(flightCode);
    }

    public void land(String flightCode) {
        landing.add(flightCode);
    }

    public void next() {
        if (landing.size() > 0) {
            System.out.printf("flight {} is landing\n", landing.remove());
        } else if (takingOff.size() > 0) {
            System.out.printf("flight {} is takingOff\n", takingOff.remove());
        }
    }

    public void quit() {
        takingOff.clear();
        landing.clear();
    }
}
