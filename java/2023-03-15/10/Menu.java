
// Modify this class so that the menu options are 
// labelled A, B, C, etc. instead of 1, 2, 3, etc. 
public class Menu {
   
    private String menuText;
    private int optionCount;
 
    public Menu()
    {
         menuText = "";
         optionCount = 0;
    }
 
    public void display()
    {
         System.out.println(menuText);
    }
 
    public void addOption(String option)
    {
        optionCount = optionCount + 1;
        menuText = menuText + optionCount + ") " + option + "\n";
    }
    
}
