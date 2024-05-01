////////The Program Below Was Entirely My Own Work.////////
import java.util.Random;
import java.util.Scanner;

public class Bank_Account
{
	double balance;

	public static void main (String[] args)
	{
		double deposit_amount;
		double withdrawl_amount;
		int i = 0;
		Scanner keyboard = new Scanner (System.in);

		Bank_Account account1 = new Bank_Account( 0.00 );
		Bank_Account account2 = new Bank_Account( 0.00 );

		System.out.println( "Thank you for choosing Edge Holding Company as your financial institution" );
		System.out.println( "Which account are you looking to use today?" );
		System.out.println( "");
		System.out.println( "To access account 1 please type in 1	To access account 2 please type in 2" );


		while (i != 1)
		{
			String reply = keyboard.next();
			if (reply.equals("1") )
			{
				System.out.printf( "account1 balance: $%.2f\n", account1.getBalance() );
				System.out.println( "Are you looking to Deposit or Withdrawl? " );
				System.out.println( "To Deposit type 1	To Withdrawl type 2 " );

				String reply2 = keyboard.next();

					if (reply2.equals("1"))
					{
						System.out.println( "Enter deposit amount for account1: " );
						deposit_amount = keyboard.nextDouble();
						System.out.printf( "\n adding %.2f to account1's balance\n\n",deposit_amount);
						account1.credit(deposit_amount);
						System.out.printf( "account1 balance: $%.2f\n", account1.getBalance() );
						System.out.println("Would you like to continue with to use continue?");
						System.out.println("Type 1 to continue	Type any other key to end your transaction");
						String reply3 = keyboard.next();
							if (reply3.equals("1"))
							{
								System.out.println( "To access account 1 please type in 1	To access account 2 please type in 2" );
							}
							else
							{
								System.out.println( "Thanks again for choosing Edge Holding Company as your financial institution." );
								i++;
							}

					}
						else if (reply2.equals("2"))
						{
							System.out.println( "Enter your withdrawl amount for account1: " );
							withdrawl_amount = keyboard.nextDouble();

							if (account1.getBalance() < withdrawl_amount)
							{
								System.out.println( "Invalid. Amount Exceeded Available Funds." );
								System.out.println( "To access account 1 please type in 1	To access account 2 please type in 2" );
							}
							else
							{
								System.out.printf( "\n removing %.2f from account1's balance\n\n",withdrawl_amount);
								account1.remove(withdrawl_amount);
								System.out.printf( "account1 balance: $%.2f\n", account1.getBalance() );
								System.out.println("Would you like to continue with to use continue?");
								System.out.println("Type 1 to continue	Type any other key to end your transaction");
								String reply4 = keyboard.next();
									if (reply4.equals("1"))
									{
										System.out.println( "To access account 1 please type in 1	To access account 2 please type in 2" );
									}
									else
									{
										System.out.println( "Thanks again for choosing Edge Holding Company as your financial institution." );
										i++;
									}
							}

						}

			}
				else if (reply.equals("2"))
				{
					System.out.printf( "account2 balance: $%.2f\n", account2.getBalance() );
					System.out.println( "Are you looking to Deposit or Withdrawl? " );
					System.out.println( "To Deposit type 1	To Withdrawl type 2 " );

					String reply5 = keyboard.next();

					if (reply5.equals("1"))
					{
						System.out.println( "Enter deposit amount for account2: " );
						deposit_amount = keyboard.nextDouble();
						System.out.printf( "\n adding %.2f to account1's balance\n\n",deposit_amount);
						account2.credit(deposit_amount);
						System.out.printf( "account2 balance: $%.2f\n", account2.getBalance() );
						System.out.println("Would you like to continue with to use continue?");
						System.out.println("Type 1 to continue	Type any other key to end your transaction");
						String reply6 = keyboard.next();
							if (reply6.equals("1"))
							{
								System.out.println( "To access account 1 please type in 1	To access account 2 please type in 2" );
							}
							else
							{
								System.out.println( "Thanks again for choosing Edge Holding Company as your financial institution." );
								i++;
							}
					}
						else if (reply5.equals("2"))
						{
							System.out.println( "Enter your withdrawl amount for account2: " );
							withdrawl_amount = keyboard.nextDouble();
							if (account2.getBalance() < withdrawl_amount)
							{
								System.out.println( "Invalid. Amount Exceeded Available Funds." );
								System.out.println( "To access account 1 please type in 1	To access account 2 please type in 2" );
							}
							else
							{
								System.out.printf( "\n removing %.2f from account1's balance\n\n",withdrawl_amount);
								account2.remove(withdrawl_amount);
								System.out.printf( "account1 balance: $%.2f\n", account2.getBalance() );
								System.out.println("Would you like to continue with to use continue?");
								System.out.println("Type 1 to continue	Type any other key to end your transaction");
								String reply7 = keyboard.next();
									if (reply7.equals("1"))
									{
										System.out.println( "To access account 1 please type in 1	To access account 2 please type in 2" );
									}
									else
									{
										System.out.println( "Thanks again for choosing Edge Holding Company as your financial institution." );
										i++;
									}
							}

						}

				}
			else
			{
				System.out.println("Invalid Case.");
				System.out.println( "To access account 1 please type in 1	To access account 2 please type in 2" );
			}
		}

	}

	public Bank_Account (double initial_balance)
	{
		Random random = new Random();
		if (initial_balance > -1.0)
		balance = random.nextInt(1000);
	}

	public void credit( double amount )
	{
		balance = balance + amount;
	}

	 public void remove( double amount )
	 {
		balance = balance - amount;
	 }

	public double getBalance()
	{
		return balance;
    }
}