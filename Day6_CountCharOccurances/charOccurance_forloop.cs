// count no of occurences
// of chars in a string 
// using for Loop

using System;

class TechnologyEncroyable {
  static void Main() {
    string str = "Technology Encroyable";
    char[] charArr = str.ToCharArray();
    foreach(char ch in charArr)
    {
        int freq = 0;
        foreach(char c in charArr){
            if(c==ch){
                freq++;
            }
        }
        Console.WriteLine(ch+" "+freq);
    }
  }
}
