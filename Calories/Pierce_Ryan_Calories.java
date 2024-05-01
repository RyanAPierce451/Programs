/***********************************************************************
@Title:		Pierce_Ryan_Calories
@Purpose:	To get familiar with primitive arithmetic data types in Java
@Author:    (Pierce Ryan)
@Date:   	(February 11th, 2021)
@Version:	1.0
************************************************************************/

import java.util.Scanner;

public class Pierce_Ryan_Calories
{

   public static void main(String[] args)
   {
		double Cookies, weight, Eachcookie_calories;
		double hours;

      	Scanner keyboard = new Scanner(System.in);

      	System.out.println("How many oreo cookies did you eat: ");
      	Cookies = keyboard.nextDouble();
      	Eachcookie_calories = 70 * Cookies;
      	System.out.println("Eating that many cookies mean you have " + Eachcookie_calories + " calories to burn.");
		System.out.println("");
		System.out.println("How much do you weight: ");
		weight = keyboard.nextDouble();

		if (weight <= 130)
		{
			hours = Eachcookie_calories / 173;
			System.out.printf("you need to walk for about %1.2f hours. \n", hours);
		}
		else if (weight >= 131 && weight <= 155)
		{
			hours = Eachcookie_calories / 216;
			System.out.printf("you need to walk for about %1.2f hours. \n", hours);
		}
		else if (weight >= 156 && weight <= 180)
		{
			hours = Eachcookie_calories / 255;
			System.out.printf("you need to walk for about %1.2f hours. \n", hours);
		}
		else if (weight >= 181 && weight <= 205)
		{
			hours = Eachcookie_calories / 284;
			System.out.printf("you need to walk for about %1.2f hours. \n", hours);
		}
		else if (weight >= 205)
		{
			hours = Eachcookie_calories / 314;
			System.out.printf("you need to walk for about %1.2f hours. \n", hours);
		}
  	}

}