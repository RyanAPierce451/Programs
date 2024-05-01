/*******************************************************************
@Title:		Pierce_Ryan_FileReader
@Purpose:	To input and output files
@Author:    (Pierce Ryan)
@Date:   	(March 4th, 2021)
@Version:	1.0
********************************************************************/

import java.io.File;
import java.util.Scanner;
import java.io.IOException;
import java.io.PrintWriter;
import java.io.*;

public class Pierce_Ryan_FileReader
{
	public static void main(String[] args)
	{
		File file = new File("name.txt");

		//All The Names being written to name.txt
		try
		{
			PrintWriter output =  new PrintWriter(file);
			output.println("Lilliana Sheley");
			output.println("Vincenza Teamer");
			output.println("Theron Beckler");
			output.println("Kacie Velazquez");
			output.println("Ione Exum");
			output.println("Mel Lade");
			output.println("Fernando Boxx");
			output.println("Leonila Discher");
			output.println("Sophie Pospisil");
			output.println("Verlene Knapik");
			output.close();
		}
		catch (IOException ex)
		{
			System.out.printf("ERROR: %s\n", ex);
		}
//---------------------------------------------------------------------------------------------------------------------------------------------------------------------

		File file2 =  new File("output.txt");

		// Getting the Names From the File name.txt
		try
		{
			PrintWriter output =  new PrintWriter(file2);
			Scanner input = new Scanner(file);
			// The names inside the File by Line
			String name1 = input.nextLine();
			String name2 = input.nextLine();
			String name3 = input.nextLine();
			String name4 = input.nextLine();
			String name5 = input.nextLine();
			String name6 = input.nextLine();
			String name7 = input.nextLine();
			String name8 = input.nextLine();
			String name9 = input.nextLine();
			String name10 = input.nextLine();
			// substring containing the needed Characters for the names
			String Chars1 = "";
			String Chars2 = "";
			String Chars3 = "";
			String Chars4 = "";
			String Chars5 = "";
			String Chars6 = "";
			String Chars7 = "";
			String Chars8 = "";
			String Chars9 = "";
			String Chars10 = "";


				if (name1.length() > 1)
				{
					// Lilliana Sheley
					Chars1 = name1.substring(0,10);
					//Vincenza Teamer
					Chars2 = name2.substring(0,10);
					//Theron Beckler
					Chars3 = name3.substring(0,8);
					//Kacie Velazquez
					Chars4 = name4.substring(0,7);
					//Ione Exum
					Chars5 = name5.substring(0,6);
					//Mel Lade
					Chars6 = name6.substring(0,5);
					// Fernando Boxx
					Chars7 = name7.substring(0,10);
					//Leonila Discher
					Chars8 = name8.substring(0,9);
					//Sophie Pospisil
					Chars9 = name9.substring(0,8);
					//Verlense Knapik
					Chars10 = name10.substring(0,9);
				}
				else
				{
					Chars1 = name1;
					Chars2 = name2;
					Chars3 = name3;
					Chars4 = name4;
					Chars5 = name5;
					Chars6 = name6;
					Chars7 = name7;
					Chars8 = name8;
					Chars9 = name9;
					Chars10 = name10;
				}
			// Putting The new Names into output.txt
			output.println(Chars1);
			output.println(Chars2);
			output.println(Chars3);
			output.println(Chars4);
			output.println(Chars5);
			output.println(Chars6);
			output.println(Chars7);
			output.println(Chars8);
			output.println(Chars9);
			output.println(Chars10);
			output.close();
		}
		catch (FileNotFoundException ex)
		{
			System.out.printf("ERROR: %s\n", ex);
		}
		System.out.println("The files have been uploaded into the computer.\n");
	}


}