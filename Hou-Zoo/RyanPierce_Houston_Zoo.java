import java.util.Scanner;
public class RyanPierce_Houston_Zoo
{
	public static void main(String[] args)
	{
		Scanner input = new Scanner(System.in);
		System.out.println("What is the current time?");
		int time = input.nextInt();
		System.out.println("What is the temperature?");
		int temp = input.nextInt();

		if(temp >= 65 && temp <= 90)
		{
			if((time >= 9 && time <= 10) || (time >= 13 && time <= 14) || (time >= 17 && time <=18))
			{
				System.out.println("The baby chimps are having a snack");
			}
			else if (time <= 5 || time >= 22)
			{
				System.out.println("The baby chimps are sleeping");
			}
			else
			{
				System.out.println("The baby chimps are playing outside");
			}
		}
		else
		{
			System.out.println("The temperature is too extreme for the baby chimps to play outside");
		}
	}
}
/* 	Exercise 1 (20 Points): Logical Operators
The baby chimps at the Houston Zoo spend most of the day playing. In particular, they play if the temperature is between 65 and 90 (inclusive). Between 9AM to 10 AM, 1PM to 2 PM, and 5PM to 6PM,
they retreat indoors for the zoo provided tasty food. They tend to sleep between 10 PM and 5 AM.
Using the above logic, write a java program such that with a user provided temperature and hour (time), display appropriate message (if the chimps will play or are having a sumptuous meal or are fast asleep).
*/

// Q(1) - A (-3)
// Q(2) - A (40)
// Q(3) - C (True or False)
// Q(4) - D (you lose the prize)
// Q(5) - B (False)