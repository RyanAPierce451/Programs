////////The Program Below Was Entirely My Own Work.////////

import java.util.Scanner;

public class Letter_Grade
{
	public static void main (String[] args)
	{
		int grade_number; //The number the user will provide for their grade
		int i = 0; // The while loop escape integer
		int count = 1; // A extra step to associate when you're on grade 1,2, or 3
		int total = 0; // The sum total of all the grade numbers
		int average; // The integer to create a average for the 3 grades
		Scanner keyboard = new Scanner( System.in );

		while (i != 3 ) //loop system until input is acceptable
			{
				System.out.println("Enter Grade "+count+"(integer 1-100): ");
				grade_number = keyboard.nextInt();
				total = total + grade_number;
				if ((grade_number >= 1) && (grade_number < 60)) // Checks for number between 1-60
				{
					System.out.println("Your Letter Grade is: F "); // Letter Grade
					i++; // allows user to loop 3 times
					count++; // updates the message
				}
				else if ((grade_number >= 60) && (grade_number < 70)) // Checks for number between 60-70
				{
					System.out.println("Your Letter Grade is: D ");
					i++;
					count++;
				}
				else if ((grade_number >= 70) && (grade_number < 80)) // Checks for number between 70-80
				{
					System.out.println("Your Letter Grade is: C ");
					i++;
					count++;
				}
				else if ((grade_number >= 80) && (grade_number < 90)) // Checks for number between 80-90
				{
					System.out.println("Your Letter Grade is: B ");
					i++;
					count++;
				}
				else if ((grade_number >= 90) && (grade_number <= 100)) // Checks for number between 90-100
				{
					System.out.println("Your Letter Grade is: A ");
					i++;
					count++;
				}
				else
				{
					System.out.println("Not a valid input: Try again"); // message to let user know input is incorrect
				}
		}

		average = total/3; // calculates the final grade average
		System.out.println("The average for these 3 grades is: " +average);
	}

}
