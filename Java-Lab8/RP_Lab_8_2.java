import java.util.Scanner;

public class RP_Lab_8_2
{
	static int arrNum;
	public static void main (String[] args)
	{
		Scanner scanner = new Scanner(System.in);
		System.out.println("What is the size of the first array?");
		int size1 = scanner.nextInt();
		System.out.println("What is the size of the second array?");
		int size2 = scanner.nextInt();

		int[] arr1 = new int[size1];
		int[] arr2 = new int[size2];

		arrNum = 0;
		arr1 = popArray(arr1, scanner);
		arr2 = popArray(arr2, scanner);

		arr1 = delSecond(arr1);
		arr2 = delSecond(arr2);

		arr1 = reverseArray(arr1);
		arr2 = reverseArray(arr2);

		int[] concArray = concArray(arr1, arr2);
		printArray(concArray);
	}

	public static void printArray(int[] array)
	{
		System.out.println("The final array is: \n");
		for(int i = 0; i < array.length; i++)
		{
			System.out.print(array[i] + ", ");
		}
	}

	public static int[] concArray(int[] array1, int[] array2)
	{
		int[] concArray = new int[array1.length + array2.length];
		for(int i = 0; i < array2.length; i++)
		{
			concArray[i] = array2[i];
		}
		for(int j = 0; j < array1.length; j++)
		{
			concArray[j + array2.length] = array1[j];
		}
		return concArray;
	}

	public static int[] reverseArray(int[] array)
	{
		int left = 0, right = array.length -1;
		while(left < right)
		{
			int temp = array[left];
			array[left] = array[right];
			array[right] = temp;
			left++;
			right--;
		}
		return array;
	}

	public static int[] popArray(int[] array, Scanner scanner)
	{
		arrNum++;
		for(int i = 0; i < array.length; i++)
		{
			System.out.println("Enter a number for array " + arrNum);
			array[i] = scanner.nextInt();
		}
		return array;
	}

	public static int[] delSecond(int[] array)
	{
		int[] delArray = new int[array.length - 1];
		int delNum = 1;
		delArray[0] = array[0];
		for(int i = delNum; i < array.length - 1; i++)
		{
			delArray[i] = array[i + 1];
		}
		return delArray;
	}
}