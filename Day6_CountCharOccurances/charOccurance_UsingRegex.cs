// count no of occurences
// of chars in a string 
// using Regex.Matches() method

using System;
using System.Text.RegularExpressions;

class TechnologyEncroyable
{
  static void Main()
  {
    string str = "Technology Encroyable";
    char[] charArr = str.ToCharArray();
    foreach(char ch in charArr)
    {
        int freq = Regex.Matches(str,ch.ToString()).Count;
        Console.WriteLine("    "+ ch +" "+freq);
    }
  }
}
