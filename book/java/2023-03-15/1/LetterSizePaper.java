
/**
 * E4_1:
 * Print characteristics of an 8-1/2 x 11 inch sheet of paper in millimeters
 * where there are 25.4 mm /inch
 */
public class E4_1
{

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args)
    {
        System.out.println ("This program prints the characteristics of an 8-1/2 x 11 in paper in mm\n");
        final double INCH_TO_MM = 25.4;
        double length = 11 * INCH_TO_MM;   // length of paper in mm
        double width = 8.5 * INCH_TO_MM;  // width of paper in mm
        double perimeter = 2 * (length + width); // distance in mm around paper
        // Use Pythagorean theorem to compute the diagonal in mm
        double diagonal = Math.sqrt(width * width + length * length);
        System.out.println("Characteristics of an 8.5 x 11 in sheet in mm:");
        System.out.printf("Width:              %5.2f mm\n", width);
        System.out.printf("Length:             %5.2f mm\n", length);
        System.out.printf("Perimeter:          %5.2f mm\n", perimeter);
        System.out.printf("Length of diagonal: %5.2f mm\n", diagonal);
    }

}

