using System;
class TechnologyEncroyable {
  static void Main() {
    string org = "Technology Encroyable";
    string newStr = "";
    for(int i = 0;i<org.Length;i++){
        if(i%2==1)
           continue;
        newStr += org[i];   
        
    }
    Console.WriteLine(newStr);
  }
}
