public class TechnologyEncroyable
{
	public static void main(String[] args) {
		String s = "Technology Encroyable";
		String r = "";
		for(int i = 0;i<s.length();i++){
		    if(i%2==0){
		        r += s.charAt(i);
		    }
		}
	    System.out.println(r);
	}
}
