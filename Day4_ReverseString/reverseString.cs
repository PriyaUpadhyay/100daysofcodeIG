using System;

class TechnologyEncroyable {
  static void Main()
  {
    string word = "Technology Encroyable"; 
    
    char[] stringArray = word.ToCharArray();
    Array.Reverse(stringArray);
    
    Console.WriteLine(new string(stringArray));
  }
}
