public class Coin implements Comparable<Coin> {
	double value;
	String name;

	public Coin(double value, String name) {
		this.value = value;
		this.name = name;
	}

	@Override
	public int compareTo(Coin coin) {
		var delta = this.value - coin.value;

		if (delta < 0)
			return -1;
		if (delta > 0)
			return 1;

		return 0;
	}

}
