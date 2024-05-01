/*******************************************************************
@Title:		Pierce_Ryan_Lab_5_1
@Purpose: 	Count vowels and check Rainfall
@Author:    (Pierce Ryan)
@Date:   	(March 5th, 2021)
@Version:	1.0
********************************************************************/
import java.util.Scanner;
import java.io.*;

public class Pierce_Ryan_Lab_5_1
{
	public static void main(String[] args) throws IOException
	{
		Scanner scan = new Scanner(System.in);
		System.out.println("What is the name of the file you want to read from?");
		String fileName = scan.nextLine();

		File textFile = new File(fileName);
		Scanner readText = new Scanner(textFile);

		String month, maxRainfallMonth = "";
		Double rainfall, average = 0.0, max = 0.0;
		int vowels = 0;
		int consonants = 0;


		do
		{

			consonants = 0;
			vowels = 0;
			month = readText.next();
			rainfall = readText.nextDouble();
			average = rainfall + average;
			char chr;

			for(int i = 0; i < month.length(); i++)
			{
				chr = month.charAt(i);
				chr = Character.toLowerCase(chr);
				if(chr == 'a' || chr == 'e' || chr == 'i' || chr == 'o' || chr == 'u')
				{
					vowels++;
				}
				else
				{
					consonants++;
				}
			}

			if(rainfall > max)
			{
				max = rainfall;
				maxRainfallMonth = month;
			}

			System.out.println("\nThere are " + vowels + " vowels in the word  " + month);
			System.out.println("There are " + consonants + " consanants in the word " + month);

		}
		while(readText.hasNext());
		{
		double Overall_Average = average / 12;
		System.out.println("\nThe month with the most rainfall was " + maxRainfallMonth + " with " + max + " inches of rain");
		System.out.println("The average amount of rainfall is " + Overall_Average + " inches of rain\n");


		}
	}
}

// 1. C) Number in the range of 100-500
// 2. D) diskOut.println("Calvin")
// 3. C) while(inputFile.hasNext());
// 4. D) int number = inputFile.nextInt()
// 5. B) File file = new File ("MyFile.txt");