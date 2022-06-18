
#include <iostream>

using namespace std;

int
main ()
{
  string original = "Technology Encroyable";
  string result = "";

  for (int i = 0; i < original.length (); i++)
    {
      if (i % 2 == 0)
	{
	  result += original[i];
	}
    }
  cout << "Original String" + original + "\n";
  cout << "New String" + result;

  return 0;
}
