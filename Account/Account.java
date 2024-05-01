//////////  Account  ///////
// Account.java
// Inputting and outputting floating-point
//numbers with Account objects.
import java.util.Scanner;

public class Account
{
	double balance;
   	// main method begins execution of Java application
   public static void main( String[] args )
   {
      	// create Account objects
	Account account1 = new Account( 50.00 );
	Account account2 = new Account( -7.53 );

      	// display initial balance of each object
      System.out.printf( "account1 balance: $%.2f\n", account1.getBalance() );
      System.out.printf( "account2 balance: $%.2f\n\n", account2.getBalance() );

      	// create Scanner to obtain input from command window
      Scanner input = new Scanner( System.in );
      double depositAmount; 	// deposit amount from user

      System.out.println( "Enter deposit for account1: " );
      depositAmount = input.nextDouble(); 	// user input
      System.out.printf( "\n adding %.2f to account1 balance\n\n",depositAmount );
      account1.credit( depositAmount );	 // add to account1 balance

      	// display balances
      System.out.printf( "account1 balance: $%.2f\n", account1.getBalance() );
      System.out.printf( "account2 balance: $%.2f\n\n", account2.getBalance() );

      System.out.print( "Enter deposit amount for account2: " );
      depositAmount = input.nextDouble(); // obtain user input
      System.out.printf( "\n adding %.2f to account2 balance\n\n",depositAmount );
      account2.credit( depositAmount ); // add to account2 balance

      	// display balances
      System.out.printf( "account1 balance: $%.2f\n",
         account1.getBalance() );
      System.out.printf( "account2 balance: $%.2f\n",
         account2.getBalance() );
   } // end main

      public Account( double initialBalance )
      {
      		// validate that initialBalance is greater than 0.0;
      		// if not, balance is initialized to default value 0.0
         if ( initialBalance > 0.0 )
            balance = initialBalance;
      }// end Account constructor

      // credit (add) an amount to the account
      public void credit( double amount )
      {
         balance = balance + amount; // add amount to balance
      } // end method credit

      // return the account balance
      public double getBalance()
      {
         return balance; // value balance to calling method
      } // end method getBalance



} // end class AccountTest
