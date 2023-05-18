import literature.Letter;

class Main {
    public static void main(String[] args) {
        var letter = new Letter("Francesco Petrarca", "Pippo Pluto");
        letter.addLine("I babbuini hanno conquistato la Casa Bianca");
        System.out.println(letter.getText());

    }
}
