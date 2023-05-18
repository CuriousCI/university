import java.util.Arrays;
import java.util.Comparator;
import java.util.stream.Stream;

public class Data {
    /**
     * Computes the average of the measures of the given objects.
     * 
     * @param objects an array of Measurable objects
     * @return the average of the measures
     */
    public static double average(Measurable[] objects) {
        double sum = 0;
        for (Measurable obj : objects) {
            sum = sum + obj.getMeasure();
        }
        if (objects.length > 0) {
            return sum / objects.length;
        } else {
            return 0;
        }
    }

    /**
     * Computes the maximum of the measures of the given objects.
     * 
     * @param objects an array of Measurable objects
     * @return the maximum of the measures, null if array is empty
     */
    public static <T extends Measurable> Measurable max(T[] objects) {
        return Arrays.stream(objects).max(Comparator.comparing(T::getMeasure)).get();
        // if (objects.length == 0) {
        // return null;
        // }
        // Measurable max = objects[0];
        // for (Measurable obj : objects) {
        // if (obj.getMeasure() > max.getMeasure()) {
        // max = obj;
        // }
        // }
        //
        // return max;
    }
}
