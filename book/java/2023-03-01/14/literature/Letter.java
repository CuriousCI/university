package literature;

public class Letter {
    private String sender, recipient, body;

    public Letter(String sender, String recipient) {
        this.sender = sender;
        this.recipient = recipient;
        this.body = "";
    }

    public void addLine(String line) {
        body += "\n" + line;
    }

    public String getText() {
        return "Caro " + recipient + ",\n" + body + "\nTuo,\n" + sender;
    }
}
