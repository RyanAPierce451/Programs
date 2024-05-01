import java.util.Scanner;
import java.util.Arrays;

public class RP_Lab_8_1
{
	public static void main (String[] args)
	{
		Scanner scanner = new Scanner(System.in);
		System.out.println("How large should the array be?");
		int size = scanner.nextInt();
		int[] arr = new int[size];

		for(int i = 0; i < arr.length; i++)
		{
			System.out.println("Enter a number: ");
			arr[i] = scanner.nextInt();
		}

		Arrays.sort(arr);
		System.out.println("The array in ascending order: ");
		ascendingOrder(arr);
		System.out.println("The array in descending order: ");
		descendingOrder(arr);
	}

	public static void ascendingOrder(int[] array)
	{
		for(int i = 0; i < array.length; i++)
		{
			System.out.println(array[i]);
		}
	}

	public static void descendingOrder(int[] myArray)
	{
		for(int i = myArray.length - 1; i >= 0; i--)
		{
			System.out.println(myArray[i]);
		}
	}
}