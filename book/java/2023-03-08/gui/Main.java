import javax.swing.*;
import java.awt.Color;
import java.awt.Point;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.Rectangle;
import javax.swing.JComponent;
import javax.swing.JFrame;
import util.Picture;

class Main {
    public static void main(String[] args) {
        // Ex 10
        var c = new Color(167, 200, 50);
        System.out.println(c.getRed() + " " + c.getGreen() + " " + c.getBlue());
        var background = c.brighter();
        System.out.println(background.getRed() + " " + background.getGreen() + " " + background.getBlue());

        // Ex 11
        var eleven = new JFrame();
        eleven.setSize(200, 200);
        eleven.getContentPane().setBackground(background);
        eleven.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        // eleven.setVisible(true);

        // Ex 12
        var color = new Color(255, 189, 208);
        System.out.println(color);
        var tmp = color.darker();
        color = new Color(tmp.getRed(), color.getGreen(), color.getBlue());
        System.out.println(color);
        color = color.darker();
        System.out.println(color);

        // Ex 15
        var p1 = new Point(901, 89);
        var p2 = new Point(203, 809);
        System.out.println(p1.distance(p2));

        // Ex 17
        var seventeen = new Picture();
        seventeen.load("/home/cicio/images/Thu Oct 13 12:20:11 PM CEST 2022");
        // seventeen.scale(picture.getWidth() / 2, picture.getHeight() / 2);
        // seventeen.move(picture.getWidth() / 4, picture.getHeight() / 4);

        // Ex 18
        var eighteen = new Picture();
        eighteen.load("/home/cicio/images/Thu Oct 13 12:20:11 PM CEST 2022");
        eighteen.scale(seventeen.getWidth() * 2, eighteen.getHeight() * 2);
        // seventeen.move(picture.getWidth() / 4, picture.getHeight() / 4);

        // Ex 19
        var nineteen = new JFrame();
        nineteen.add(new JComponent() {
            @Override
            public void paintComponent(Graphics g) {
                var g2D = (Graphics2D) g;
                g2D.draw(new Rectangle(10, 23, 200, 50));
                g2D.draw(new Rectangle(20, 30, 30, 30));
            }
        });
        nineteen.setSize(400, 400);
        nineteen.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        // nineteen.setVisible(true);

        // Ex 20
        var twenty = new JFrame();
        twenty.add(new JComponent() {
            @Override
            public void paintComponent(Graphics g) {
                var g2D = (Graphics2D) g;
                g2D.setPaint(Color.PINK);
                g2D.fill(new Rectangle(67, 10, 200, 50));
                g2D.setPaint(Color.YELLOW);
                g2D.fill(new Rectangle(67, 75, 30, 30));
            }
        });
        twenty.setSize(400, 400);
        twenty.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        // twenty.setVisible(true);
    };
}
