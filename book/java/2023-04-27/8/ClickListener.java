import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class ClickListener implements ActionListener {
	Integer clicks = 0;

	@Override
	public void actionPerformed(ActionEvent e) {
		clicks++;
		System.out.printf("I was clicked %s times\n", clicks);
	}

}
