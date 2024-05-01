////////The Program Below Was Entirely My Own Work.////////
import java.util.Random;
import java.util.Scanner;

public class YourCar
{
	double gas_total;

	public static void main (String[] args)
	{

		double how_much;
		double miles;
		double total_miles = 0;
		double MPH;
		double total_MPH = 0;;
		double average_MPH;
		int adding_gas;
		int drain_gas = 1;
		int travel_count = 1;
		int i = 0;
		Scanner keyboard = new Scanner (System.in);

		YourCar gas = new YourCar( 0.00 );


		System.out.println("Are you going on a trip today. (1 = Yes  |  Any Other Key = No)");
		String reply = keyboard.next();

			if (reply.equals("1"))
			{
				travel_count++;
				if (gas.getGas_total() < 0)
				{
					System.out.println("hey you remembered to put gas in your car how much did you put again? 1-15");
					adding_gas = keyboard.nextInt();
					gas.add_gas(adding_gas);
				}
			}
			else
			{
				System.out.println("Nothing wrong with staying indoors today, take care.");
						i++;
			}


		while (i != 1)
		{
			if(gas.getGas_total() > 0)
			{
				System.out.println("Great so right now you have "+ gas.getGas_total() + " gallons in your tank");
				System.out.println("(In Miles) How far are you traveling: ");
				miles = keyboard.nextDouble();
				System.out.println("(MPH) What speed are you traveling at: ");
				MPH = keyboard.nextDouble();
				total_MPH = total_MPH + MPH;
				total_miles = total_miles + miles;
				System.out.println("Is there more to your trip? (1 = Yes  |  Any Other Key = No)");
				String reply2 = keyboard.next();

				if (reply2.equals("1"))
				{
					System.out.println("This is the travel trip number " + travel_count);
					gas.remove_gas(drain_gas);
					travel_count++;


				}
				else
				{
					average_MPH = total_MPH / travel_count;
					double time_hours = total_miles / average_MPH;
					System.out.println("You traveled " + total_miles +" miles" );
					System.out.println("For a total an average of  " + average_MPH + " MPH");
					System.out.printf("For %5.2f Hours ", time_hours);
					i++;
				}
			}
			else
			{
				System.out.println("Oh NO! Looks like you ran out of gas");
				average_MPH = total_MPH / travel_count - 1;
				double time_hours = total_miles / average_MPH;
				System.out.println("You traveled " + total_miles +" miles" );
				System.out.println("for a total an average of  " + average_MPH + " MPH");
				System.out.printf("For %5.2f Hours", time_hours);
				i++;
			}
		}
	}

	public YourCar (Double gas_tank)
	{
		Random random = new Random();
		if (gas_tank > -1.0)
		gas_total = random.nextInt(15);
	}
	public void add_gas( double fill_up )
	{
			gas_total = gas_total + fill_up;
	}
	public void remove_gas( double drain )
	 {
			drain = 1;
			gas_total = gas_total - drain;
	 }
	public double getGas_total()
	{
			return gas_total;
    }
}