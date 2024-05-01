import java.util.Scanner;

public class BMI
{

   public static void main(String[] args)
   {
	  double weight, height, BMI;

      Scanner keyboard = new Scanner(System.in);

      System.out.print("Input weight in kilogram: ");
      weight = keyboard.nextDouble();

      System.out.print("Input height in meters: ");
      height = keyboard.nextDouble();

      BMI = weight / (height * height);
      System.out.print("The Body Mass Index (BMI) is " + BMI + " " );
  	}

}