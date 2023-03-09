import javax.swing.*;
import java.awt.Color;
import java.awt.Point;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.Rectangle;
import javax.swing.JComponent;
import javax.swing.JFrame;

class Main {
    public static void main(String[] args) {
        // Ex 10
        var c = new Color(167, 200, 50);
        System.out.println(c.getRed() + " " + c.getGreen() + " " + c.getBlue());
        var b = c.brighter();
        System.out.println(b.getRed() + " " + b.getGreen() + " " + b.getBlue());

        // Ex 11
        var frame = new JFrame();
        frame.setSize(200, 200);
        var pane = frame.getContentPane();
        pane.setBackground(b);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        // frame.setVisible(true);

        // Ex 12
        var j = new Color(255, 189, 208);
        System.out.println(j);
        var tmp = j.darker();
        j = new Color(tmp.getRed(), j.getGreen(), j.getBlue());
        System.out.println(j);
        j = j.darker();
        System.out.println(j);

        // Ex 15
        var p1 = new Point(901, 89);
        var p2 = new Point(203, 809);
        System.out.println(p1.distance(p2));

        // Ex 17
        // var window = new JFrame(); // Must import Picture class
        // window.setSize(200, 200);
        // var p = frame.getContentPane();
        // window.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        // frame.setVisible(true);

        // Ex 18
        // var w = new JFrame(); // Must import Picture class
        // window.setSize(200, 200);
        // var pa = frame.getContentPane();
        // window.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        // frame.setVisible(true);

        // Ex 19
        var q = new JFrame();
        q.setSize(400, 400);
        q.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        var n = q.getContentPane();
        var r1 = new Rectangle(10, 23, 200, 15);
        var r2 = new Rectangle(20, 50, 30, 30);
        var g = new Graphics2D();
        g.draw(r1);
        g.draw(r2);
        q.add(g);
    };
}
