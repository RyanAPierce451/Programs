import java.util.*;
 public class RyanPierce_Digits
 {
 public static void main(String[] args)
    {
        Scanner input = new Scanner(System.in);
        System.out.print("Input the first number : ");
        int a = input.nextInt();
		System.out.print("Input the second number: ");
		int b = input.nextInt();
		System.out.print("Input the third number : ");
        int c = input.nextInt();
        System.out.print("Input the fourth number : ");
        int d = input.nextInt();
        System.out.print("The result is: "+test_last_digit(a, b, c, d));
		System.out.print("\n");
    }

   public static boolean test_last_digit(int p, int q, int t, int r)
        {
   	     return ((p % 10 == q % 10) || (p % 10 == r % 10) || (q % 10 == r % 10) || (t % 10 == r % 10) || (p % 10 == t % 10) || (q % 10 == t % 10));
        }
}

/* Exercise 3 DIY (40 Points):
Given four ints, a b c, and d, return true if two or more of them have the same rightmost digit. The ints are non-negative.
(Note: the % "mod" operator provides the remainder, e.g. 12 % 10 is 2).
*/
