import java.util.Scanner;
import java.util.Arrays;

public class RP_Lab_8_3
{
	public static void main (String[] args)
	{
		Scanner scanner = new Scanner(System.in);
		int n = 5;
		int[] arr = new int[n];

		int total = 0;

		for(int i = 0; i < arr.length; i++)
		{
			System.out.print("Enter Array "+(i + 1)+": ");
			arr[i] = scanner.nextInt();
		}

		scanner.close();

		for(int i = 0; i < arr.length; i++)
		{
			total = total + arr[i];
		}

		int average = total / arr.length;

		System.out.format(" The average of the array is: %d \n ", average);
		int m = 0;
		if(n%2==1)
			{
				m = arr[(n + 1)/2-1];
			}
			else
			{
				m = (arr[n /2 - 1]+ arr[n / 2])/2;
			}

       System.out.println("The median of the array is : "+m);

	}
}

// 1.	We cannot declare an Array without its array size? - True

// 2.
//		a.	We can change the size of an array after creation? - False
//		b.	Was the size of the array changed in the below code? - No, we made a new array list that have values of 0 in all the arrays slots.
//		c.	What is the output of the below code? - 30, 0

// 3.
//		a.	Will the below lines code compile? - True, though it wont show anything since no System.out.print/format has been called to showcase the list.
//		b.	What is the size of the mylist array? - 8

// 4.
//		a. We can pass a negative number as the size of an array? - False
//		b. Do we get a compile-time or run-time error when a negative size is passed to the array? - run-time error "java.lang.NegativeArraySizeException:"
//		c. What is the exception thrown when a negative number is passed as the size of the array? -  Exception in thread "main" java.lang.NegativeArraySizeException:

// 5.	What is the difference between ArrayStoreException and ArrayOutOfBoundsException
//	ArrayOutOfBoundsException - Thrown to indicate that an array has been accessed with an illegal index. The index is either negative or greater than or equal to the size of the array.
//  ArrayStoreException - Thrown when you have created an array of a particular datatype with a fixed size and populating it and you try and store a value other than its datatype.