public class Quiz implements Measurable {
	final double score;
	final String grade;

	public Quiz(double score, String grade) {
		this.score = score;
		this.grade = grade;
	}

	public double getScore() {
		return this.score;
	}

	public String getGrade() {
		return this.grade;
	}

	@Override
	public double getMeasure() {
		return this.score;
	}

}
