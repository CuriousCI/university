import algorithms.Exam;
import algorithms.Tree;

public class Main {
    public static void main(String[] args) {
        var tree = new Tree<Integer>(
                1000,
                new Tree<Integer>(
                        200,
                        new Tree<Integer>(
                                5,
                                new Tree<Integer>(2)),
                        new Tree<Integer>(12)),
                new Tree<Integer>(209,
                        new Tree<Integer>(
                                11,
                                new Tree<Integer>(1)),
                        new Tree<Integer>(2)));

        // Ex 1
        Exam.visit(tree);
        // Ex 2
        Exam.visit(Exam.addUp(tree, tree));
        // Ex 3
        System.out.println(Exam.areChildrenSmaller(tree));
        // Ex 4
        System.out.println(Exam.minimalHeight(tree));
    }

}
