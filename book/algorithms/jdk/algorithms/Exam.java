package algorithms;

import java.util.Optional;

import algorithms.struct.Stack;

public class Exam {
    public static <T> void visit(Tree<T> tree) {
        var stack = new Stack<Tree<T>>();

        var node = Optional.of(tree);
        while (node.isPresent()) {
            var n = node.get();
            System.out.println(n.value);

            if (n.right.isPresent())
                stack.push(n.right.get());
            if (n.left.isPresent())
                stack.push(n.left.get());

            node = stack.pop();
        }
    }

    public static <T extends Comparable<? super T>> boolean areChildrenSmaller(Tree<T> tree) {
        var isLeftValid = true;
        if (tree.left.isPresent()) {
            var l = tree.left.get();
            if (l.value.compareTo(tree.value) > 0)
                return false;
            isLeftValid = areChildrenSmaller(l);
        }

        var isRightValid = true;
        if (tree.right.isPresent()) {
            var r = tree.right.get();
            if (r.value.compareTo(tree.value) > 0)
                return false;
            isRightValid = areChildrenSmaller(r);
        }

        return isLeftValid && isRightValid;
    }

    public static <T> Integer minimalHeight(Tree<T> tree) {
        var leftHeight = 0;
        if (tree.left.isPresent())
            leftHeight = minimalHeight(tree.left.get());
        else
            leftHeight = -1;

        var rightHeight = 0;
        if (tree.right.isPresent())
            rightHeight = minimalHeight(tree.right.get());
        else
            rightHeight = -1;

        return 1 + Math.min(leftHeight, rightHeight);
    }

    public static Tree<Integer> addUp(Tree<Integer> first, Tree<Integer> second) {
        first.value += second.value;

        if (first.left.isPresent())
            addUp(first.left.get(), second.left.get());
        else if (second.left.isPresent())
            first.left = second.left;

        if (first.right.isPresent())
            addUp(first.right.get(), second.right.get());
        else if (second.right.isPresent())
            first.right = second.right;

        return first;
    }
}
