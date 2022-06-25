
class Main {
	
	int binarySearch(int arr[], int low, int high, int val)
	{
		if (high >= low) {
			int mid = low + (high - low) / 2;
			if (arr[mid] == val)
				return mid;
			if (arr[mid] > val)
				return binarySearch(arr, low, mid - 1, val);
			return binarySearch(arr, mid + 1, high, val);
		}
		return -1;
	}

	public static void main(String args[])
	{
		Main ob = new Main();
		int arr[] = { 2, 3, 4, 10, 40 };
		int n = arr.length;
		int x = 10;
		int result = ob.binarySearch(arr, 0, n - 1, x);
		if (result == -1)
			System.out.println("Element not present");
		else
			System.out.println("Element found at index "
							+ result);
	}
}

