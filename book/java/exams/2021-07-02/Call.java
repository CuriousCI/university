import java.lang.module.FindException;
import java.util.ArrayList;
import java.util.List;

public class Call {
    public static void main(String[] args) {
        Phonebook phonebook = new Phonebook();
        phonebook.addContact(new Contact("Marco", "Polo", "3246307158"));
        phonebook.addContact(new Contact("Sara", "Amarilli", "8210821018"));
        phonebook.addContact(new Contact("Siliva", "Pompinelli", "2810821009"));
        phonebook.addContact(new Contact("Marco", "Folli", "2801019291"));

        System.out.println(phonebook);

        phonebook.removeContact("Marco", "Folli");
        try {
            System.out.println(phonebook.getPhoneNumber("Sara", "Amarilli"));
        } catch (FindException e) {
            System.err.println("Contact not found!");
        }

        try {
            System.out.println(phonebook.getPhoneNumber("Marco", "Foli"));
        } catch (FindException e) {
            System.err.println("Contact not found!");
        }

        System.out.println();
        System.out.println(phonebook);

    }
}

class Phonebook {
    private List<Contact> contacts;

    public Phonebook() {
        this.contacts = new ArrayList<>();
    }

    public void addContact(Contact contact) {
        this.contacts.add(contact);
    }

    public void removeContact(String firstName, String lastName) {
        int index = 0;
        for (Contact c : this.contacts) {
            if (c.getFirstName().equals(firstName) && c.getLastName().equals(lastName)) {
                break;
            }
            index++;
        }

        this.contacts.remove(index);
    }

    public String getPhoneNumber(String firstName, String lastName)
            throws FindException {

        for (Contact c : this.contacts) {
            if (c.getFirstName().equals(firstName) && c.getLastName().equals(lastName)) {
                return c.getPhoneNumber();
            }
        }

        throw new FindException("Contact Not Found");
    }

    @Override
    public String toString() {
        String out = "Contacts in phonebook:\n";

        for (Contact c : this.contacts) {
            out += "- " + c.toString() + "\n";
        }

        return out;
    }
}

class Contact {
    private String firstName;
    private String lastName;
    private String phoneNumber;

    public Contact(String firstName, String lastName, String phoneNumber) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.phoneNumber = phoneNumber;
    }

    public String getFirstName() {
        return this.firstName;
    }

    public String getLastName() {
        return this.lastName;
    }

    public String getPhoneNumber() {
        return this.phoneNumber;
    }

    @Override
    public String toString() {
        return String.format(
                "fullname: %s %s - phone: %s",
                this.firstName,
                this.lastName,
                this.phoneNumber);
    }
}
