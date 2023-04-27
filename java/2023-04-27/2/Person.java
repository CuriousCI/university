public class Person implements Measurable {
	String name;
	int height;

	public Person(String name, int height) {
		this.name = name;
		this.height = height;
	}

	public String getName() {
		return this.name;
	}

	@Override
	public double getMeasure() {
		return this.height;
	}
}
