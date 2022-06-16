// count no of occurences
// of chars in a string 
// using String.Split() method

using System;

class TechnologyEncroyable {
  static void Main() {
    string str = "Technology Encroyable";
    char[] charArr = str.ToCharArray();
    foreach(char ch in charArr){
        int freq = str.Split(ch).Length - 1 ;
        Console.WriteLine("    "+ ch +" "+freq);
    }
  }
}
