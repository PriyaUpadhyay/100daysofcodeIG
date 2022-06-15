public class TechnologyEncroyable
{
	public static void main(String[] args) {
		String str = "Technology Encroyable";
		String[] strArr = str.split(" ");
		
		String rev = "";
		for(int i = strArr.length-1;i>=0;i--){
		    rev += strArr[i] + " ";
		}
		System.out.println(rev);
	}
}
