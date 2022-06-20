public class TechnologyEncroyable
{
    public static boolean checkEquality(int arr1[],int arr[2]){
        int len1 = arr1.length;
        int len2 = arr2.length;
        
        if(len1!=len2)
          return false;
        Arrays.sort(arr1);
        Arrays.sort(arr2);
        
        for(int i=0;i<len1;i++)
          if(arr1[i]!=arr2[i])
            return false;
        return true;
    }
    
    // Driver Code 
    
	public static void main(String[] args) {
	    int arr1 = {10, 30, 50, 20, 100};
        int arr2 = {30, 10, 100, 20, 50};
        int arr3 = {50, 60, 80, 10, 69};
        
        boolean equality1 = checkEquality(arr1,arr2);
        boolean equality2 = checkEquality(arr1,arr3);
        if(equality1)
		   System.out.println("arr1 & arr2 are Equal.");
		if(equality2)
		   System.out.println("arr1 & arr3 are Equal.");
	}
}
