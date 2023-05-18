class Grid {
    public static void main(String[] args) {
        String row = "+--+--+--+\n|  |  |  |",
                lastRow = "+--+--+--+";

        for (int r = 0; r < 3; r++)
            System.out.println(row);
        System.out.println(lastRow);
    }
}
