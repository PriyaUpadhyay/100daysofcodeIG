// count no of occurences
// of chars in a string

using System;
using System.Linq;
class TechnologyEncroyable {
  static void Main() {
    string str = "Technology Encroyable";
    char[] charArr = str.ToCharArray();
    foreach(char ch in charArr){
        int freq = str.Where(c => (c==ch)).Count();
        Console.WriteLine("    "+ ch +" "+freq);
    }
  }
}
