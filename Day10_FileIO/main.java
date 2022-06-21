import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
 
public class Main 
{   
    public static void main(String[] args) 
    {
        BufferedReader reader = null;
        int charCount = 0;
        int wordCount = 0;
        int lineCount = 0;
        
        reader = new BufferedReader(new FileReader("Input.txt"));
        String currentLine = reader.readLine();
             
        while (currentLine != null)
            {
                lineCount++;
                String[] words = currentLine.split(" ");
                
                wordCount+= words.length;
                for (String word : words)
                {
                    charCount += word.length();
                }
                currentLine = reader.readLine();
            }
            
            System.out.println("Chars "+charCount);
            System.out.println("Words "+wordCount);
            System.out.println("Lines "+lineCount); 
    }
}
        
