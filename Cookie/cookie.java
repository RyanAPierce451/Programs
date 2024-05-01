import java.util.Scanner;

public class cookie
{
	public static void main (String[] args)
	{
		Scanner sc = new Scanner (System.in);

		System.out.println ("Do you want a cookie? (Yes/No)");
		String reply = sc.next();

		if(reply.equals("Yes") )
		{
			System.out.println("Cookie for you");
		}
		else
		{
			System.out.println("No cookie for you");
		}
	}

}