public class FillInQuestion extends Question {
    public FillInQuestion(String question) {
        super(question);
    }

    @Override
    public void display() {
        super.display();
        System.out.println("_______");
    }
}
