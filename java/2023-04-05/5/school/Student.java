package school;

public class Student {
    Double[] scores;
    Integer scoresSize;

    public Student(Integer size) {
        scores = new Double[size];
        scoresSize = 0;
    }

    public Boolean addScore(Double score) {
        if (scoresSize >= scores.length)
            return false;

        scores[scoresSize] = score;
        scoresSize++;
        return true;
    }

    public Double sum() {
        var sum = 0.0;
        for (var index = 0; index < scoresSize; index++)
            sum += scores[index];
        return sum;
    }

    public Double minimum() {
        var min = scores[0];
        for (var index = 0; index < scoresSize; index++)
            if (scores[index] < min)
                min = scores[index];
        return min;
    }

    public Double finalScore() {
        return sum() - minimum();
    }

    public void removeMin() {
        var min = minimum();

        for (var index = 0; index < scoresSize; index++)
            if (scores[index] == min) {
                if (index != scoresSize - 1)
                    scores[index] = scores[scoresSize - 1];
                scoresSize--;
                return;
            }
    }
}
