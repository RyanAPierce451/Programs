/*******************************************************************
@Title:		Pierce_Ryan_Calculator
@Purpose:	Simple to use calulator to solve mathmatic equations
@Author:    (Pierce Ryan)
@Date:   	(March 4th, 2021)
@Version:	1.0
********************************************************************/
import java.util.Scanner;
import java.lang.Math;

public class Pierce_Ryan_Calculator
{
	public static void main(String[] args)
	{
		Scanner keyboard = new Scanner(System.in);
		double num1;
		double num2;
		double answer;
		int operator;    	// this will decide the operations the user performs
		System.out.println("Hello this program is better then any Ti-84 Calculator, except you're using the free trial so you get limited use.");
        System.out.println("");
        System.out.println("Addition = 1");
        System.out.println("Subtraction = 2");
        System.out.println("Multiplication = 3");
        System.out.println("Division = 4");
        System.out.println("Exponent = 5");
        System.out.println("Quit = 6");
         System.out.println("");
//-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        System.out.print("Enter an operation: ");
		operator = keyboard.nextInt();
		System.out.print("Enter the First Operant: ");
		num1 = keyboard.nextDouble();
		System.out.print("Enter the Second Operant: ");
		num2 = keyboard.nextDouble();
//-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
		while(num1 != 0 && num2 != 0)
		{
			if(operator == 1)
			{
				System.out.println(num1 + num2);

				System.out.println("Would you like to do another operation? Yes/No ");
				String reply = keyboard.next();
					if(reply.equals("Yes") )
					{
						System.out.print("Enter an operation: ");
						operator = keyboard.nextInt();
						System.out.print("Enter the First Operant: ");
						num1 = keyboard.nextDouble();
						System.out.print("Enter the Second Operant: ");
						num2 = keyboard.nextDouble();
					}
					else
					{
						System.out.println("Thanks for using the best calulator the world's ever seen"); // Used To get out of the loop in another way
						num1=0;
						num2=0;
					}
			}
			else if (operator == 2)
			{
				System.out.println(num1 - num2);

				System.out.println("Would you like to do another operation? Yes/No ");
				String reply = keyboard.next();
					if(reply.equals("Yes") )
					{
						System.out.print("Enter an operation: ");
						operator = keyboard.nextInt();
						System.out.print("Enter the First Operant: ");
						num1 = keyboard.nextDouble();
						System.out.print("Enter the Second Operant: ");
						num2 = keyboard.nextDouble();
					}
					else
					{
						System.out.println("Thanks for using the best calulator the world's ever seen");
						num1=0;
						num2=0;
					}
			}
			else if (operator == 3)
			{
				System.out.println(num1 * num2);

				System.out.println("Would you like to do another operation? Yes/No ");
				String reply = keyboard.next();
					if(reply.equals("Yes") )
					{
						System.out.print("Enter an operation: ");
						operator = keyboard.nextInt();
						System.out.print("Enter the First Operant: ");
						num1 = keyboard.nextDouble();
						System.out.print("Enter the Second Operant: ");
						num2 = keyboard.nextDouble();
					}
					else
					{
						System.out.println("Thanks for using the best calulator the world's ever seen");
						num1=0;
						num2=0;
					}
			}
			else if (operator == 4)
			{
				System.out.println(num1 / num2);

				System.out.println("Would you like to do another operation? Yes/No ");
				String reply = keyboard.next();
					if(reply.equals("Yes") )
					{
						System.out.print("Enter an operation: ");
						operator = keyboard.nextInt();
						System.out.print("Enter the First Operant: ");
						num1 = keyboard.nextDouble();
						System.out.print("Enter the Second Operant: ");
						num2 = keyboard.nextDouble();
					}
					else
					{
						System.out.println("Thanks for using the best calulator the world's ever seen");
						num1=0;
						num2=0;
					}
			}
			else if (operator == 5)
			{
				System.out.println(Math.pow(num1,num2));

				System.out.println("Would you like to do another operation? Yes/No ");
				String reply = keyboard.next();
					if(reply.equals("Yes") )
					{
						System.out.print("Enter an operation: ");
						operator = keyboard.nextInt();
						System.out.print("Enter the First Operant: ");
						num1 = keyboard.nextDouble();
						System.out.print("Enter the Second Operant: ");
						num2 = keyboard.nextDouble();
					}
					else
					{
						System.out.println("Thanks for using the best calulator the world's ever seen");
						num1=0;
						num2=0;
					}
			}
			else if (operator == 6)
			{
				System.out.println ("Thanks for using the best calulator the world's ever seen");
				num1=0;
				num2=0;
			}
			else if (operator == 42)
			{
							System.out.println ("wow only a skilled hacker could have figured out how to get to this point and here at the FBI");
							System.out.println ("we need skilled people like you");
							System.out.println ("Your new name will be 007 and we'll be seeing you real soon.");
							num1=0;
							num2=0;
			}
			else
			{
				System.out.println("Operation is invalid.");
				System.out.print("Enter an operation: ");
				operator = keyboard.nextInt();
				System.out.print("Enter the First Operant: ");
				num1 = keyboard.nextDouble();
				System.out.print("Enter the Second Operant: ");
				num2 = keyboard.nextDouble();
			}
		}

	}

}