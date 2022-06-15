using System;
class HelloWorld {
  static void Main() {
        string str = "Technology Encroyable";
		string[] strArr = str.Split(" ");
		
		string rev = "";
		for(int i = strArr.Length-1;i>=0;i--)
		{
		    rev += strArr[i] + " ";
		}
		Console.WriteLine(rev);
  }
}
