using System;
class TechnologyEncroyable {
    public static bool checkEquality(int[] arr1,int[] arr2){
        int len1 = arr1.Length;
        int len2 = arr2.Length;
        
        if(len1!=len2)
          return false;
          
        Array.Sort(arr1);
        Array.Sort(arr2);
        
        for(int i=0;i<len1;i++)
          if(arr1[i]!=arr2[i])
            return false;
        return true;
    }
  static void Main() {
        int[] arr1 = {10, 30, 50, 20, 100};
        int[] arr2 = {30, 10, 100, 20, 60};
        if(checkEquality(arr1,arr2))
           Console.WriteLine("Equal");
        else
           Console.WriteLine("Not Equal");
        
  }
}
