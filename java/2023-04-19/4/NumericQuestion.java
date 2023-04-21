public class NumericQuestion extends Question {
    private double answer;

    NumericQuestion(String question) {
        super(question);
        answer = 0.0;
    }

    public void setAnswer(double answer) {
        this.answer = answer;
    }

    @Override
    public boolean checkAnswer(String answer) {
        return this.answer - Double.valueOf(answer) < 0.01;
    }
}
