import java.util.ArrayList;

public class Bag {
	ArrayList<String> groceries = new ArrayList<String>();

	public void add(String item) {
		groceries.add(item);
	}

	public int count(String item) {
		return (int) groceries
				.stream()
				.filter(i -> i.compareTo(item) == 0)
				.count();
	}
}
